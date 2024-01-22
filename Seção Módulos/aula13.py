import os
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv
import pathlib

load_dotenv()

path_html = pathlib.Path(__file__).parent / 'aula13.html'
remetente = os.getenv('FROM_EMAIL', '')
destinatario = 'may.ambrosiosilva@gmail.com'

# configurações
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# lendo template HTML
with open(path_html, 'r', encoding='utf-8') as file:
    text = file.read()
    template = Template(text)
    text_email = template.substitute(nome='Mayara')

# MIMEMultpart
mime_multpart = MIMEMultipart()
mime_multpart['From'] = remetente
mime_multpart['To'] = destinatario
mime_multpart['Subject'] = 'Olá Mayara'

corpo_email = MIMEText(text_email, 'html', 'utf-8')
mime_multpart.attach(corpo_email)

# enviando e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multpart)
    print('E-mail enviado com sucesso!')