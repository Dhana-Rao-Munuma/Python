#!/usr/bin/env python3

import emails

if __name__ == "__main__":
    email_from = "automation@example.com"
    email_to = "student-04-ac64d0c750c3@example.com"
    subject_line = "Upload Completed - Online Fruit Store"
    email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = "/tmp/processed.pdf"
    message = emails.generate_email(email_from, email_to, subject_line, email_body, attachment)
    emails.send_email(message)
