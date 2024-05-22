import smtplib
from email.message import EmailMessage
import json
import argparse


def extract_personnal_info(path):
    with open(path, 'r') as f:
        data = json.load(f)

    mail_info = data.get("mail", {})
    password = mail_info.get("password")
    user = mail_info.get("user")

    return user, password


def email_alert(subject, body, to, path):
    user, password = extract_personnal_info(path)
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = user

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


def send_message(msg, title, destination, path):

    email_alert(title, msg, destination, path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='AlertEmail',
        description='Send email to alert user of something')
    parser.add_argument('-d', '--destination', type=str, required=True, help='Sender')
    parser.add_argument('-m', '--message', type=str, required=True, help='Message content')
    parser.add_argument('-t', '--title', type=str, required=True, help='Title')
    parser.add_argument('-path', '--path', type=str, required=True, help='Path')

    args = parser.parse_args()

    send_message(args.message, args.title, args.destination, args.path)
