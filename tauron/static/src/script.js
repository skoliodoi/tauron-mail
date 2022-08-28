
$("#incydent-dropdown").dropdown()
$("#ezr-dropdown").dropdown()
$('.ui.radio.checkbox')
  .checkbox()
  ;

$("#zagrozenie_button").on('click', (e) => {
  e.preventDefault()

  $("#form-card").hide()
  $("#podsumowanie-card").show()

  const val = $("#zagrozenie_miejscowosc").val()
  const gmina = $("#zagrozenie_gmina").val()
  const ulica = $("#zagrozenie_ulica").val()
  const nrDomu = $("#zagrozenie_dom").val()
  const kodPocztowy = $("#zagrozenie_kod").val()
  const nazwiskoFirma = $("#zagrozenie_nazwisko_firma").val()
  const telefon = $("#zagrozenie_telefon").val()
  const opis = $("#zagrozenie_opis").val()
  const koronawirus = $("#zagrozenie_koronawirus").val()
  const stanNapiecia = $("input[name='napiecie']:checked", "#zagrozenie_form").val()


  $("#zag-pod-miej").empty()
  $("#zag-pod-gmina").empty()
  $("#zag-pod-ulica").empty()
  $("#zag-pod-dom").empty()
  $("#zag-pod-kp").empty()
  $("#zag-pod-nf").empty()
  $("#zag-pod-tel").empty()
  $("#zag-pod-opis").empty()
  $("#zag-pod-korona").empty()
  $("#zag-pod-stan").empty()

  $("#zag-pod-miej").append(val)
  $("#zag-pod-gmina").append(gmina)
  $("#zag-pod-ulica").append(ulica)
  $("#zag-pod-dom").append(nrDomu)
  $("#zag-pod-kp").append(kodPocztowy)
  $("#zag-pod-nf").append(nazwiskoFirma)
  $("#zag-pod-tel").append(telefon)
  $("#zag-pod-opis").append(opis)
  $("#zag-pod-korona").append(koronawirus)
  $("#zag-pod-stan").append(stanNapiecia)
});

$("#zagrozenie_submit").on('click', (e) => {
  e.preventDefault()
  const miejscowosc = $("#zagrozenie_miejscowosc").val()
  const gmina = $("#zagrozenie_gmina").val()
  const ulica = $("#zagrozenie_ulica").val()
  const nrDomu = $("#zagrozenie_dom").val()
  const kodPocztowy = $("#zagrozenie_kod").val()
  const nazwiskoFirma = $("#zagrozenie_nazwisko_firma").val()
  const telefon = $("#zagrozenie_telefon").val()
  const opis = $("#zagrozenie_opis").val()
  const koronawirus = $("#zagrozenie_koronawirus").val()
  const stanNapiecia = $("input[name='napiecie']:checked", "#zagrozenie_form").val()
  $.post("/erz-zagrozenie", {
    "miejscowosc": miejscowosc,
    'gmina': gmina,
    'ulica': ulica,
    'nr_budynku': nrDomu,
    'kod_pocztowy': kodPocztowy,
    'nazwisko_firma': nazwiskoFirma,
    'telefon': telefon,
    'opis': opis,
    'koronawirus': koronawirus,
    'napiecie': stanNapiecia
  }).done(data => {
    window.location.href = `/success/${data}`
  })
 
})

$("#zagrozenie_popraw").on('click', (e) => {
  e.preventDefault()
  $("#form-card").show()
  $("#podsumowanie-card").hide()
})

const lokalizacje = {
  "JR 10,11 Bielsko Biała": ["POK 61 Bielsko Biała", "POK 62 Cieszyn", "POK 63 Wadowice", "POK 64 Żywiec", "POK 65 Kęty"],
  "JR 14,15 Będzin": ["POK 72 Sosnowiec", "POK 73 Będzin", "POK 74 Dąbrowa Górnicza",
    "POK 75, 78 Jaworzno, Mysłowice", "POK 76 Trzebinia-Siersza", "POK 77 Zawiercie", "POK 79 Olkusz"],
  "JR 14, 15 Częstochowa": ["POK 81 Częstochowa miasto", "POK 84 Częstochowa teren",
    "POK 82 Myszków", "POK 83 Lubliniec", "POK 85 Kłobuck"],
  "JR 6,7 Kraków": ["POK 92 Nowa Huta", "POK 94 Krowodrza Wschód", "POK 91 Śródmieście", "POK 94 Krowodrza Zachód",
    "POK 93 Podgórze Wschód", "POK 93 Podgórze Zachód", "POK 98 Nowy Sącz", "POK 96 Nowy Targ",
    "POK 97 Limanowa", "POK 95 Zakopane"],
  "JR 14, 15 Tarnów": ["POK 45,49 Tarnów", "POK 47 Bochnia", "POK 46 Dębica", "POK 48 Dąbrowa Tarnowska"],
  "JR 8,9 Jelenia Góra": ["POK 25 Jelenia Góra", "POK 26 Bolesławiec", "POK 27 Lubań"],
  "JR 8,9 Legnica": ["POK 21 Legnica", "POK 22 Głogów", "POK 23 Chojnów", "POK 24 Lubin"],
  "JR 16,17 Opole": ["POK 32 Opole", "POK 33 Namysłów", "POK 34 Kluczbork", "POK 39 Brzeg",
    "POK 36 Kędzierzyn-Koźle", "POK 35 Strzelce Opolskie", "POK 37 Nysa", "POK 38 Paczków"],
  "JR 16,17 Wałbrzych": ["POK 41 Wałbrzych", "POK 42 Strzegom", "POK 43 Dzierżoniów", "POK 44 Kłodzko"],
  "JR 8,9 Wrocław": ["POK 51 Wrocław", "POK 52 Oborniki Śląskie", "POK 53 Oleśnica", "POK 54 Strzelin", "POK 55 Środa Śląska"],
  "JR 1,3 Gliwice": ["POK 1 Gliwice", "POK 2 Zabrze", "POK 3 Bytom", "POK 4 Pyskowice", "POK 9 Ruda Śląska",
    "POK 8 Tarnowskie Góry", "POK 5 Chorzów", "POK 6 Mikołów", "POK 7 Katowice", "POK 10 Racibórz", "POK 11 Rybnik",
    "POK 12 Wodzisław Śląski", "POK 13 Pszczyna"
  ]
}

$("#koronawirus").on('click', () => {
  console.log('Ping!')
})
$("#rejon").on('change', (e) => {
  if (e.target.value != '') {
    $("#lokalizacja").prop("disabled", false)
  } else {
    $("#lokalizacja").prop("disabled", true)
  }

  for (const each in lokalizacje) {
    if (e.target.value == each) {
      $("#lokalizacja").empty()
      for (const miasto of lokalizacje[each])
        $("#lokalizacja").append($('<option>', {
          value: miasto,
          text: miasto
        }))
    }
  }

})