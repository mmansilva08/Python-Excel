import smtplib
import ssl
import mimetypes
from email.message import EmailMessage

# Dados do email
password = open("senha", "r").read()
# print(password)
from_email = "mmansilva1981@gmail.com"
subject = "Automação Planilha"
to_email = "mmansilva1981@gmail.com"
body = """
Olá, segue em anexo a automação da planilha para empresa xyxy.
qualquer dúvida estou à disposição
"""

message = EmailMessage()
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subject

message.set_content(body)
safe = ssl.create_default_context()

# Adicionar anexo
anexo = "test.xlsx"
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split("/")
with open(anexo, "rb") as a:
    message.add_attachment(
        a.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=anexo
    )

# Envio do email
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )
