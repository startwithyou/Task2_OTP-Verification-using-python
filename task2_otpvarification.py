import random
import smtplib

# generate a 6-digit OTP code
otp = random.randint(100000, 999999)

# send the OTP code to the user's email address using SMTP
from p1 import Password
sender_email = 'pawar.shwari25@gmail.com'
receiver_email = 'patilharshal069@gmail.com'
password = Password
message = f'Subject: OTP Verification\n\nYour OTP code is {otp}'

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

# prompt the user to enter the OTP code
user_input = input('Enter the OTP code sent to your email: ')

# compare the user's input with the generated OTP code
if int(user_input) == otp:
    print('OTP verification successful!')
else:
    print('OTP verification failed!')