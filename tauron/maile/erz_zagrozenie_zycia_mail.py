def zagrozenie_zycia(**kwargs):
    html = f"""<span><b>{kwargs['wstep']}</b>
  </span>
  <span><b>Miejscowość:</b> {kwargs['miejscowosc']}</span>
  <span><b>Gmina:</b> {kwargs['gmina']}</span>
  <span><b>Kod pocztowy:</b> {kwargs['kod_pocztowy']}</span>
  <span><b>Ulica:</b> {kwargs['ulica']}</span>
  <span><b>Nr budynku/lokalu:</b> {kwargs['nr_budynku']}</span>
  <span><b>Nazwsko/Firma:</b> {kwargs['nazwisko_firma']}</span>
  <span><b>Telefon:</b> {kwargs['telefon']}</span>
  <span><b>Opis zdarzenia:</b> {kwargs['opis']}</span>
  <span><b>Koronawirus:</b> {kwargs['koronawirus']}</span>
  <span><b>Stan napięciowy:</b> {kwargs['stan_napieciowy']}</span>
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
