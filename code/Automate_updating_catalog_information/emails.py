#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

def generate_email(email_from, email_to, subject_line, email_body, attachment_path):
    """Creates an email with an attachement."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = email_from
    message["To"] = email_to
    message["Subject"] = subject_line
    message.set_content(email_body)

    # Process the attachment and add it to the email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=attachment_filename)

    return message

def generate_email_with_no_attachment(email_from, email_to, subject_line, email_body):
    """Creates an email without an attachement."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = email_from
    message["To"] = email_to
    message["Subject"] = subject_line
    message.set_content(email_body)

    return message


def send_email(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

