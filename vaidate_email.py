#!/usr/bin/python

user_input = str(raw_input("email id: "))
from validate_email import validate_email
is_valid = validate_email(user_input)
if is_valid is True:
 import csv
 email_list = []
 filekhol = open('output.csv')
 csv_file = csv.reader(filekhol)

 for row in csv_file:
  email_list.append(row)

 for email in email_list:
  if user_input in str(email):
   print 'Exist..:)'
  else:
   print 'Not Exist...:('
else:
 print 'Invalid Email Address..:/'
