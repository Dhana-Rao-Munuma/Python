#!/usr/bin/env python3

import csv
import os
import re
import operator

error_messages_file=os.path.join(os.path.expanduser("~"),"error_message.csv")
user_statistics_file=os.path.join(os.path.expanduser("~"),"user_statistics.csv")
input_log_file=os.path.join(os.path.expanduser("~"),"syslog.log")

pattern = r"ticky: (INFO|ERROR) ([\w' ]*)(\[#[0-9]*\])? \(([\w.]*)\)"  # \(([\w]*)\)"

error_message_stats = {}
user_stats = {}

with open(input_log_file,"r") as file:
    for each_line in file:
        #print("each_line " , each_line)
        match = re.search(pattern, each_line)
        string_1 = ""
        string_2 = ""
        string_3 = ""
        string_4 = ""
        if match:
            if match.group(1):
                string_1 = match.group(1)
            if match.group(2):
                string_2 = match.group(2)
            if match.group(3):
                string_3 = match.group(3)
            if match.group(4):
                string_4 = match.group(4)
        #print(string_1, "-", string_2, "-", string_4) #, "-", string_4)

        if string_2 not in error_message_stats:
            error_message_stats[string_2] = 1
        else:
            error_message_stats[string_2] += 1

        if string_4 not in user_stats:
            user_stats[string_4] = {"INFO":0, "ERROR":0}

        error_type = string_1
        user_stats[string_4][error_type] += 1

        """
        if string_1 == "INFO":
            user_stats[string_4]["INFO"] += 1
        elsif string_1 == "ERROR":
            user_stats[string_4
        """

#error_message_stats_sorted = sorted(error_message_stats(),key=operator.itemgetter(1))
error_message_stats_sorted = dict(sorted(error_message_stats.items(), key=lambda item: item[1], reverse=True))

with open(error_messages_file, "w", newline="") as error_message_f:
    writer = csv.writer(error_message_f)

    header = ["Error", "Count"]
    writer.writerow(header)

    for key, value in error_message_stats_sorted.items():
        #print("key ", key, "value ", value )
        row = [key, value]
        writer.writerow(row)

user_stats

user_statistics_file


user_stats_sorted = dict(sorted(user_stats.items(), key=lambda item: item[0]))

with open(user_statistics_file, "w", newline="") as user_stats_f:
    writer = csv.writer(user_stats_f)

    header = ["Username", "INFO", "ERROR"]
    writer.writerow(header)

    for key, value in user_stats_sorted.items():
        print("key ", key, "value ", value )
        row = [key]
        for info_count, error_count in value.items():
            print("info count ", info_count, "error_count ", error_count)
            row.append(error_count)
        writer.writerow(row)


