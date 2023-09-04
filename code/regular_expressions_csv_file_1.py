import csv
import re
input_file = "C:\\Dhana\\OneDrive - Conduent\\Reading Materials\\python\\my_code\\user_emails.csv"
output_file = "C:\\Dhana\\OneDrive - Conduent\\Reading Materials\\python\\my_code\\updated_user_emails.csv"

modified_lines = []

with open(input_file,'r') as f:
    user_data_list = csv.DictReader(f)
    for line in user_data_list:
        #for items in line:
        print(line)

        line[" Email Address"] = re.sub(r"@abc\.edu","@xyz.edu",line[" Email Address"])
        print("email address " ,str(line[" Email Address"]))
        print("line ", line)
        modified_lines.append(line)


print(modified_lines)
with open(output_file,'w+', newline = '') as f:
    fieldnames = modified_lines[0].keys()
    print("fieldnames", fieldnames)
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(modified_lines)

