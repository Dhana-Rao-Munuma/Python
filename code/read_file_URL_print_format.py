

import csv
import datetime
import requests

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = 2019 #int(input('Enter a value for the year: '))
    month = 5 #int(input('Enter a value for the month: '))
    day = 1 #int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def read_and_load_data_in_dict():

    date_employees={}
    data = get_file_lines(FILE_URL)

    reader = csv.reader(data[1:])

    for row in reader:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')

        employee = "{} {}".format(row[0], row[1])
        if row_date in date_employees:
            date_employees[row_date].append(employee)
        else:
            date_employees[row_date]=[employee]
    return date_employees

def list_newer_new(start_date, my_dict):

    while start_date < datetime.datetime.today():
        if start_date in my_dict:
            employees = my_dict[start_date]
            print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))

        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)

def main():
    start_date = get_start_date()

    my_dict={}
    my_dict=read_and_load_data_in_dict()

    print(start_date)
    list_newer_new(start_date, my_dict)

if __name__ == "__main__":
    main()
