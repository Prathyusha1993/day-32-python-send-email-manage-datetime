import smtplib

my_email = 'pyhtonmailtesting@gmail.com'
password = 'mwbagxjkgrkqjwde'

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs='testpythonemail@yahoo.com', msg='Subject:Hello, Hii\n\nThis is the body of my email.')
    connection.close()