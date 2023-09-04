import csv
user_data_list=[['dhana', 'munuma.dhanarao@gmail.com'], ['dhana1', 'munuma.dhanarao1@gmail.com']] 
csv_file_location = "C:\\Dhana\\OneDrive - Conduent\\Reading Materials\\python\\my_code\\user_emails.csv"
with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))
user_data_list=[['dhana', 'munuma.dhanarao@gmail.com'], ['dhana1', 'munuma.dhanarao1@gmail.com']] 
old_domain_email_list=['munuma.dhanarao@gmail.com','munuma.dhanarao1@gmail.com']
new_domain_email_list=['munuma.dhanaraotest@gmail.com','munuma.dhanarao1test@gmail.com']
for user in user_data_list:
    #for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
    for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        print('old_domain-' , old_domain, 'new_domain-', new_domain)
        print('user[1]-',user[1])
        if user[1] == old_domain:
            user[1] = new_domain
          #if user[1] == ' ' + ' munuma.dhanarao@gmail.com':
        #user[1] = ' ' + ' munuma.dhanaraotest@gmail.com'

for user in user_data_list:
    print('user' , user)