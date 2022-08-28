from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
from .data import oddzialy

rejony = [""]
for key, value in oddzialy.items():
    rejony.append(key)

umowy = ["Umowa kompleksowa"]
koronawirus_opcje = ["", "Nie odpytano o kwarantannę/nadzór", "Brak kwarantanny/nadzoru", "Uwaga - osoba objęta izolacją",
                     "Uwaga - osoba objęta kwarantanną", "Uwaga - osoba objęta nadzorem epidemiologicznym"]

powody = ["", "Kradzież licznika", "TD - brak podłączenia", "TD - uszkodzony licznik",
          "TD (błąd) - brak zasilania po realizacji innego, wcześniejszego zlecenia",
          "TD (błąd) - pomyłka w wyłączeniu", "TOK - błąd procedury", "TOK - brak możliwosci wykupu energii dla IPP",
          "TOK - reklamacja przez sekretariat", "Zagrożenie życia"]
incydenty = ["", "BOMBA, AKT TERRORYZMU, ZAGROŻENIE KRYTYCZNE",
             "INCYDENT INFORMATYCZNY", "INCYDENT RODO"]


class Incydent(FlaskForm):
    rodzaj = SelectField("Rodzaj incydentu", choices=incydenty)
    data_zgloszenia = DateField("Data zgłoszenia")
    dane_osobowe = StringField("Imię i nazwisko")
    telefon = StringField("Telefon kontaktowy")
    email = StringField("Email")
    opis = TextAreaField("Opis incydentu", render_kw={"rows": 15})
    send = SubmitField("Wyślij wiadomość")


class ErzAwaryjnePodlaczenie(FlaskForm):
    imie = StringField("Imię", render_kw={"placeholder": "Imię"})
    nazwisko = StringField("Nazwisko", render_kw={"placeholder": "Nazwisko"})
    rejon = SelectField("Rejon", choices=rejony)
    lokalizacja = SelectField("Lokalizacja (najpierw wybierz rejon)", choices=[
    ], render_kw={"disabled": True})
    # lokalizacja = SelectField("Wybierz opcje z pola REJON DYSTRYBUCJI")
    nr_ot = StringField("Numer wystawionego zlecenia OT",
                        render_kw={"placeholder": "Numer OT"})
    rodzaj_klienta = SelectField("Rodzaj klienta", choices=umowy)
    # oddzial = SelectField("Oddział", choices=rejony)
    kod_pocztowy = StringField("Kod pocztowy", render_kw={
                               "placeholder": "Kod pocztowy"})
    miasto = StringField("Miasto", render_kw={"placeholder": "Miasto"})
    adres = StringField("Adres", render_kw={"placeholder": "Adres"})
    nr_ewidencyjny = StringField("Nr ewidencyjny", render_kw={
                                 "placeholder": "Numer ewidencyjny"})
    telefon = StringField("Telefon", render_kw={
                          "placeholder": "Telefon kontaktowy"})
    nr_licznika = StringField("Nr licznika", render_kw={
                              "placeholder": "Numer licznika"})
    nr_ppe = StringField("Nr PPE", render_kw={"placeholder": "Numer PPE"})
    powod = SelectField("Powód", choices=powody)
    koronawirus = SelectField("Koronawirus", choices=koronawirus_opcje)
    przyczyna = TextAreaField("Przyczyna", render_kw={"rows": 3})
    send = SubmitField("Wyślij wiadomość")


class ErzWycofanieLubWznowienie(FlaskForm):
    imie = StringField("Imię", render_kw={"placeholder": "Imię"})
    nazwisko = StringField("Nazwisko", render_kw={"placeholder": "Nazwisko"})
    rejon = SelectField("Rejon", choices=rejony)
    lokalizacja = SelectField("Lokalizacja (najpierw wybierz rejon)", choices=[
    ], render_kw={"disabled": True})
    nr_ot = StringField("Numer wystawionego zlecenia OT",
                        render_kw={"placeholder": "Numer OT"})
    rodzaj_klienta = SelectField("Rodzaj klienta", choices=umowy)
    kod_pocztowy = StringField("Kod pocztowy", render_kw={
                               "placeholder": "Kod pocztowy"})
    miasto = StringField("Miasto", render_kw={"placeholder": "Miasto"})
    adres = StringField("Ulica i numer domu", render_kw={
                        "placeholder": "Adres"})
    nr_ewidencyjny = StringField("Nr ewidencyjny", render_kw={
                                 "placeholder": "Numer ewidencyjny"})
    telefon = StringField("Telefon", render_kw={
                          "placeholder": "Telefon kontaktowy"})
    nr_ppe = StringField("Nr PPE", render_kw={"placeholder": "Numer PPE"})
    koronawirus = SelectField("Koronawirus", choices=koronawirus_opcje)
    notatka = TextAreaField("Notatka", render_kw={"rows": 3})
    send = SubmitField("Wyślij wiadomość")


class ErzZagrozenieZycia(FlaskForm):
    miejscowosc = StringField("Miejscowość", render_kw={
                              "placeholder": "Miejscowość"})
    gmina = StringField("Gmina", render_kw={"placeholder": "Gmina"})
    kod_pocztowy = StringField("Kod pocztowy", render_kw={
                               "placeholder": "Kod pocztowy"})
    ulica = StringField("Ulica", render_kw={"placeholder": "Ulica"})
    nr_budynku = StringField("Numer budynku/lokalu",
                             render_kw={"placeholder": "Numer budynku/lokalu"})
    telefon = StringField("Telefon", render_kw={
                          "placeholder": "Telefon kontaktowy"})
    opis = TextAreaField("Opis zdarzenia", render_kw={"rows": 5})
    koronawirus = SelectField("Koronawirus", choices=koronawirus_opcje)
    nazwisko = StringField(
        "Nazwisko/Firma", render_kw={"placeholder": "Nazwisko/Firma"})

    send = SubmitField("Zapisz")
