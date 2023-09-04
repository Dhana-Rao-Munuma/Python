import re, sys

#email = input("enter the email id:")
email = sys.argv[1]

if re.search(".+@.+\.com$",email):
    print("Valid Email")
else:
    print("Invalid Email")

if re.search("^\w+@\w+\.com$",email):
    print("Valid Email")
else:
    print("Invalid Email")