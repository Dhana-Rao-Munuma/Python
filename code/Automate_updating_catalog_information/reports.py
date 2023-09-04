#!/usr/bin/env python3

import os
import requests
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image,SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

from datetime import datetime

def generate_report(title, paragraph, attachment):
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()
    header = title + " " + str(datetime.now().strftime("%B %d, %Y"))
    print(header)

    story = []
    # write header to the PDF
    report_title = Paragraph(header, styles["h1"])
    story.append(report_title)
    #report.build([report_title])

    # Add an empty line (Spacer) between files outside the story list
    story.append(Spacer(1, 12))
    # write paragraph to the PDF
    #report_title = Paragraph(paragraph, styles["h2"])
    #report.build(report_title)


    for line_nu in range(len(paragraph)):
        #line_style = Paragraph(each_line, styles['Normal'])
        line_style = Paragraph(paragraph[line_nu], styles['Normal'])
        story.append(line_style)
        if line_nu % 2 == 1:
            # Add an empty line (Spacer) between files outside the story list
            story.append(Spacer(1, 12))

    report.build(story)


if __name__ == "__main__":

    paragraph = []

    #paragraph.append("Hello")
    #paragraph.append("Hi")
    #paragraph.append("How\n")
    #paragraph.append("Are\n")
    #paragraph.append("You\n")

    txt_file_full_path = "/home/student-04-ac64d0c750c3/supplier-data/descriptions/"
    files = os.listdir(txt_file_full_path)

    for each_file in files:
        if each_file.lower().endswith('.txt'):
            file_with_full_path = os.path.join(txt_file_full_path, each_file)
            with open(file_with_full_path,"r") as f_open:
                line_no = 0
                for each_line in f_open.readlines():
                    line_no += 1
                    if line_no == 1:
                        paragraph.append("{} {}".format("name:",each_line))
                    if line_no == 2:
                        paragraph.append("{} {}".format("weight:",each_line))
                    if line_no == 3:
                        # Add an empty line (Spacer) between each paragraph
                        None
                        #paragraph.append(Spacer(1, 12))  # Adjust the second argument to control the space between lines

    generate_report("Processed Update on",paragraph,"/tmp/processed.pdf")

