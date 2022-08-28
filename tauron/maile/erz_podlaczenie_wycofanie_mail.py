def podlaczenie_wycofanie(**kwargs):
    html = f"""<span>Witam,</span>
  <p>{kwargs['wstep']}
  </p>
  <span><b>Rejon dystrybucji:</b> {kwargs['rejon_dystrybucji']}</span>
  <span><b>Lokalizacja:</b> {kwargs['lokalizacja']}</span>
  <span><b>Numer wystawionego zlecenia OT:</b> {kwargs['nr_ot']}</span>
  <span><b>Rodzaj umowy:</b> {kwargs['rodzaj_umowy']}</span>
  <span><b>Imię:</b> {kwargs['imie']}</span>
  <span><b>Nazwisko:</b> {kwargs['nazwisko']}</span>
  <span><b>Ulica i numer domu:</b> {kwargs['adres']}</span>
  <span><b>Miejscowość:</b> {kwargs['miasto']}</span>
  <span><b>Kod pocztowy:</b> {kwargs['kod_pocztowy']}</span>
  <span><b>Numer ewidencyjny:</b> {kwargs['nr_ewidencyjny']}</span>
  <span><b>Numer PPE:</b> {kwargs['nr_ppe']}</span>
  <span><b>Numer licznika:</b> {kwargs['nr_licznika']}</span>
  <span><b>Telefon:</b> {kwargs['telefon']}</span>
  <span><b>Koronawirus:</b> {kwargs['koronawirus']}</span>
  <span><b>Powód:</b> {kwargs['powod']}</span>
  <span><b>Dodatkowe informacje:</b> {kwargs['notatka']}</span>
  <table style="border-collapse: collapse">
  <tbody>
    <tr style="color: #404040; font-family: Arial, sans-serif; font-size: 14tdx; line-height: 18px;">Serdecznie pozdrawiam, </tr>
    <tr style="display: inline">
      <td style="padding-right: 24px;"><img src="https://res.cloudinary.com/davhlcjqq/image/upload/v1661514202/welcomemail/voice-v3_um0cnv.png" alt="VCC_logo">
      <!--[if mso]>
        <span></span>
        <span></span>
        <span></span>
      <![endif]-->

      </td>
      <td cellpadding="0">
        <span style="color: #2589db; font-family: Arial, sans-serif; font-size: 17px; line-height: 21px;">{kwargs['agent']}</span>
        <span style="color: #404040; font-family: Arial, sans-serif; font-size: 13px; line-height: 17px;">Konsultant</span>
        <span style="color: #404040; font-family: Arial, sans-serif; font-size: 13px; font-weight: 600; line-height: 17px;"><b>Przełożony:</b> </span> <span>{kwargs['przelozony']}</span>
        <span style="color: #404040; font-family: Arial, sans-serif; font-size: 13px; font-weight: 600; line-height: 17px;"><b>Numer przełożonego:</b></span> <span>{kwargs['telefon_przelozonego']}</span>
        <span style="color: #404040; font-family: Arial, sans-serif; font-size: 13px; font-weight: 600; line-height: 17px;"><b>Email przełożonego:</b> </span><span>{kwargs['mail_przelozonego']}</span>
        <span></span>
        <span></span>
      </td>
    </tr>
  </tbody>
  </table>
"""

    return html
