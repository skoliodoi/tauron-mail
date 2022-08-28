

def zglos_incydent_mail(**kwargs):
    html = f"""<span>Witam,</span>
  <p>{kwargs['wstep']}
  </span>
  <span><b>Rodzaj incydentu:</b> {kwargs['rodzaj']}</span>
  <span><b>Data zgłoszenia:</b> {kwargs['data']}</span>
  <span><b>Imię i nazwisko:</b> {kwargs['dane_osobowe']}</span>
  <span><b>Email:</b> {kwargs['email']}</span>
  <span><b>Opis incydentu:</b> {kwargs['opis']}</span>
  <span><b>Login agenta:</b> {kwargs['login']}</span>
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
