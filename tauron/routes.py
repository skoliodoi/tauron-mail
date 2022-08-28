from unicodedata import name
from flask import Blueprint, jsonify, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from tauron.forms import ErzAwaryjnePodlaczenie, ErzWycofanieLubWznowienie, ErzZagrozenieZycia, Incydent
from tauron.maile.erz_podlaczenie_wycofanie_mail import podlaczenie_wycofanie
from tauron.maile.erz_zagrozenie_zycia_mail import zagrozenie_zycia
from tauron.maile.erz_awaryjne_podlaczenie_mail import awaryjne_podlaczenie
from tauron.maile.incydent_mail import zglos_incydent_mail
from .data import oddzialy
from datetime import datetime, time

import yagmail

godzina_15 = time(15, 0)
godzina_19 = time(19, 0)


# mail_awarie = 'tdp.awarie@tauron-dystrybucja.pl'
# mail_991 = 'tauron.991@galluppolska.pl'
# mail_smart = 'tdp.ami.scw@tauron-dystrybucja.pl'
# mail_incydenty = 'incydent@tauron.pl'

mail_incydenty = ['szymon.ulanowski@oex-vcc.com',
                  'szymon.zygaluk@gmail.com']
mail_awarie = ['szymon.ulanowski@oex-vcc.com', 'szymon.zygaluk@gmail.com']
mail_991 = ['szymon.ulanowski@oex-vcc.com', 'szymon.zygaluk@gmail.com']
mail_smart = ['szymon.ulanowski@oex-vcc.com', 'szymon.zygaluk@gmail.com']
reply_mail = ['szymon.ulanowski@oex-vcc.com', 'szymon.zygaluk@gmail.com']

yag = yagmail.SMTP('njootek', 'toutajohntjenkkr')


def ogarnij_podpis():
    db_data = {
        'login': current_user.id,
        'agent': f"{current_user.name} {current_user.last_name}",
        'przelozony': current_user.przelozony,
        'telefon_przelozonego': current_user.numer,
        'mail_przelozonego': current_user.mail
    }
    return db_data


def ogarnij_dotyczenie(form_oddzial, form_lokalizacja):
    now = datetime.now().time()
    if now < godzina_15:
        email_wys = ""
        oddzial = form_oddzial
        lokalizacja = form_lokalizacja
        for key, value in oddzialy.items():
            if key == oddzial:
                for nazwa_miasta, dane in value['lokalizacje'].items():
                    if nazwa_miasta == lokalizacja:
                        email_wys = dane['email']
        mail = email_wys
    elif now >= godzina_15 and now <= godzina_19:
        mail = mail_awarie
    else:
        mail = mail_991
    return mail


def send_mail(recipient, subject, content):
    yag.send(recipient, subject, content, headers={
             "Reply-To": f"{reply_mail}"})


main = Blueprint('main', __name__)


@main.route('/', methods=["POST", "GET"])
@login_required
def index():
    return render_template('main.html', name=current_user.name)


@main.route('/success/<mail>')
@login_required
def success(mail):
    return render_template("success.html", mail=mail)


@main.route('/incydent', methods=["POST", "GET"])
@login_required
def incydent():
    header_text = "Incydenty"
    form = Incydent()
    if request.method == "POST":
        try:
            user_data = ogarnij_podpis()
            mail_wstep = f"Uwaga - {form.rodzaj.data}"
            email = mail_incydenty
            html = zglos_incydent_mail(
                wstep=mail_wstep,
                rodzaj=form.rodzaj.data,
                data=form.data_zgloszenia.data,
                dane_osobowe=form.dane_osobowe.data,
                telefon=form.telefon.data,
                email=form.email.data,
                opis=form.opis.data,
                login=user_data['login'],
                agent=user_data['agent'],
                przelozony=user_data['przelozony'],
                telefon_przelozonego=user_data['telefon_przelozonego'],
                mail_przelozonego=user_data['mail_przelozonego']

            )
            send_mail(email, mail_wstep, html)
            return redirect(url_for('main.success', mail=email))
        except:
            pass
    return render_template("incydenty.html", header_text=header_text, form=form)


@main.route("/erz-awaryjne", methods=["POST", "GET"])
@login_required
def erz_windykacja():
    header_text = "Awaryjne podłączenie energii elektrycznej"
    form = ErzAwaryjnePodlaczenie()
    if request.method == "POST":
        try:
            now = datetime.now().time()
            if now <= godzina_19:
                email = mail_awarie
            else:
                email = mail_991
            mail_wstep = "W załączeniu przesyłamy zlecenie OT na wznowienie energii elektrycznej w trybie alarmowym."
            user_data = ogarnij_podpis()
            html = awaryjne_podlaczenie(
                wstep=mail_wstep,
                rejon_dystrybucji=form.rejon.data,
                lokalizacja=form.lokalizacja.data,
                nr_ot=form.nr_ot.data,
                rodzaj_umowy=form.rodzaj_klienta.data,
                imie=form.imie.data,
                nazwisko=form.nazwisko.data,
                adres=form.adres.data,
                miasto=form.miasto.data,
                kod_pocztowy=form.kod_pocztowy.data,
                nr_ewidencyjny=form.nr_ewidencyjny.data,
                nr_ppe=form.nr_ppe.data,
                nr_licznika=form.nr_licznika.data,
                telefon=form.telefon.data,
                koronawirus=form.koronawirus.data,
                powod=form.powod.data,
                notatka=form.przyczyna.data,
                agent=user_data['agent'],
                przelozony=user_data['przelozony'],
                telefon_przelozonego=user_data['telefon_przelozonego'],
                mail_przelozonego=user_data['mail_przelozonego']
            )
            # print("BOOOF-a!")
            send_mail(email, mail_wstep, html)
            return redirect(url_for('main.success', mail=email))
        except Exception as e:
            print(str(e))
    return render_template("erz_awaryjne_podlaczenie.html", form=form, header_text=header_text)


@main.route("/erz-zagrozenie", methods=["POST", "GET"])
@login_required
def erz_zagrozenie():
    header_text = "Zagrożenie życia"
    form = ErzZagrozenieZycia()
    if request.method == "POST":
        try:
            email = mail_991
            user_data = ogarnij_podpis()
            wstep = "Uwaga! Potencjalna sytuacja zagrożenia życia!"
            html = zagrozenie_zycia(
                wstep=wstep,
                miejscowosc=request.form.get('miejscowosc'),
                gmina=request.form.get('gmina'),
                ulica=request.form.get('ulica'),
                nr_budynku=request.form.get('nr_budynku'),
                kod_pocztowy=request.form.get('kod_pocztowy'),
                nazwisko_firma=request.form.get('nazwisko_firma'),
                telefon=request.form.get('telefon'),
                opis=request.form.get('opis'),
                koronawirus=request.form.get('koronawirus'),
                stan_napieciowy=request.form.get('napiecie'),
                agent=user_data['agent'],
                przelozony=user_data['przelozony'],
                telefon_przelozonego=user_data['telefon_przelozonego'],
                mail_przelozonego=user_data['mail_przelozonego']

            )
            send_mail(email, wstep, html)
            return email
        except:
            pass
            # return render_template('erz_zagrozenie_podsumowanie.html', dane=dane, header_text="Zagrożenie życia - podsumowanie")
    return render_template("erz_zagrozenie_form.html", form=form, header_text=header_text)


@main.route("/erz/<akcja>", methods=["POST", "GET"])
@login_required
def erz_wycofanie(akcja):
    form = ErzWycofanieLubWznowienie()
    if akcja == 'wycofanie':
        header_text = "Wycofanie wniosku o wstrzymanie energii elektrycznej"
        wznowienie = False
        mail_wstep = "W związku z ustaniem przyczyny wstrzymania dostaw energii prosimy o wycofanie z realizacji Wniosku na wstrzymanie dostawy energii, a w przypadku jego zrealizowania prosimy o dokonanie wznowienia dostarczania energii elektrycznej - zlecenie OT zostało wystawione w systemie bilingowym i przekazane do realizacji."
        temat = "Proszę o wycofanie zlecenia na wyłączenie"
    else:
        header_text = "Wznowienie dostarczania energii elektrycznej"
        temat = "Proszę o pilne wznowienie dostawy energii elektrycznej"
        mail_wstep = "W załączeniu przesyłamy wniosek o dokonanie wznowienia dostarczania energii elektrycznej w trybie pilnym."
        wznowienie = True
    if akcja == "smart":
        form.notatka.data = "Licznik SMART"
    if request.method == "POST":
        user_data = ogarnij_podpis()
        try:
            email = mail_991

            html = podlaczenie_wycofanie(
                wstep=mail_wstep,
                rejon_dystrybucji=form.rejon.data,
                lokalizacja=form.lokalizacja.data,
                nr_ot=form.nr_ot.data,
                rodzaj_umowy=form.rodzaj_klienta.data,
                imie=form.imie.data,
                nazwisko=form.nazwisko.data,
                adres=form.adres.data,
                miasto=form.miasto.data,
                kod_pocztowy=form.kod_pocztowy.data,
                nr_ewidencyjny=form.nr_ewidencyjny.data,
                nr_ppe=form.nr_ppe.data,
                telefon=form.telefon.data,
                koronawirus=form.koronawirus.data,
                notatka=form.notatka.data,
                agent=user_data['agent'],
                przelozony=user_data['przelozony'],
                telefon_przelozonego=user_data['telefon_przelozonego'],
                mail_przelozonego=user_data['mail_przelozonego']

            )
            # print("BOOOF-a!")
            send_mail(email, temat, html)
            return redirect(url_for('main.success', mail=email))
        except:
            pass
    return render_template("erz_podlaczenie_wycofanie.html", header_text=header_text, form=form, wznowienie=wznowienie)
