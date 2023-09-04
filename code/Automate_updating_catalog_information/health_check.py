#!/usr/bin/env python3

import os
import shutil
import psutil
import emails
import socket

#cpu_usage_percentage = 90
cpu_usage_percentage = psutil.cpu_percent(interval=1)
print("cpu_usage_percentage: ", cpu_usage_percentage)

#disk_space_free_percentage = 10
disk_usage = psutil.disk_usage('/')
disk_space_free_percentage = (disk_usage.free / disk_usage.total) * 100
print("disk_space_free_percentage: ", disk_space_free_percentage)

#memory_free_in_mb = 400
memory_info = psutil.virtual_memory()
memory_free_in_mb = memory_info.available / ( 1024 ** 2  )
print("memory_free_in_mb: ", memory_free_in_mb)

#host_name_issue = True
try:
    ip_address = socket.gethostbyname("localhost")

    if ip_address == "127.0.0.1":
        host_name_issue = "True"
    else:
        host_name_isue = "False"
except socket.gaierror:
    print("Hostname 'localhost' can not be resolved. There may be a resolution issue.")
print("host_name_issue: ", host_name_issue)

if cpu_usage_percentage > 80:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_email_with_no_attachment("automation@example.com", "student-04-ac64d0c750c3@example.com",subject, "Please check your system and resolve the issue as soon as possible.")
    emails.send_email(message)

if disk_space_free_percentage < 20:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_email_with_no_attachment("automation@example.com", "student-04-ac64d0c750c3@example.com",subject, "Please check your system and resolve the issue as soon as possible.")
    emails.send_email(message)

if memory_free_in_mb < 500:
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_email_with_no_attachment("automation@example.com", "student-04-ac64d0c750c3@example.com",subject, "Please check your system and resolve the issue as soon as possible.")
    emails.send_email(message)

if host_name_issue == True:
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_email_with_no_attachment("automation@example.com", "student-04-ac64d0c750c3@example.com",subject, "Please check your system and resolve the issue as soon as possible.")
    emails.send_email(message)


