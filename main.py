import smtplib
import pandas
import random
import datetime

now = datetime.datetime.now()
month = now.month
day = now.day
today = (month, day)

MY_EMAIL = "mail"
MY_PASSWORD = "pass"

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}

if today in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        letter = file.read()
        final_letter = letter.replace("[NAME]", birthdays_dict[today]['name'])
        final_letter_1 = final_letter.replace("Sender", "[sender_name]")
        print(final_letter_1)
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, birthdays_dict[today]['email'], f"Subject:Happy Birthday!!!\n{final_letter_1}")
        connection.close()
