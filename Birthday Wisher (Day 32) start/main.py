import smtplib
import datetime as dt
import random

my_email = 'pyhtonmailtesting@gmail.com'
my_password = 'mwbagxjkgrkqjwde'

current_day = dt.datetime.now()
current_day_of_week = current_day.weekday()
if current_day_of_week == 3:
    with open('quotes.txt', 'r') as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f'Subject:Monday Motivation\n\n{quote}')
        connection.close()





#
# smtp example from gmail to yahoo:
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, to_addrs='testpythonemail@yahoo.com',
#                             msg=f'Subject:Monday Motivation\n\n{quote}')
#     connection.close()

