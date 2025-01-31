import datetime as dt
import smtplib
import pandas
import random

MY_EMAIL = 'pyhtonmailtesting@gmail.com'
MY_PASSWORD = 'mwbagxjkgrkqjwde'

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

birth_data = pandas.read_csv('birthdays.csv')

birthdays_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in birth_data.iterrows()}

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person['email'],
                            msg=f'Subject:Happy Birthday\n\n{contents}')
        connection.close()
