from random import *
from datetime import *
from tkinter import messagebox
import smtplib
import os
import pandas as p


def write_and_send():
        try:
            with open(file=f"{folder}\\{letter}", mode="r") as email_data:
                template = email_data.read()
                email = template.replace("[NAME]", f'{bday_dict[day]["name"]}')

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_pw)
                connection.sendmail(
                    from_addr=my_email, to_addrs="address@example.com",
                    msg=f"Subject: Happy Birthday\n\n{email}")
        except FileNotFoundError:
            messagebox.showwarning(title="File Not Found", message="This file does not exist.")
        except IndexError:
            messagebox.showwarning(title="Index Error", message="There was an index error.")


def get_dict(data_file):
    bday_data = p.read_csv(data_file)
    dict = bday_data.to_dict(orient="index")
    my_dict = {(dict[i]["month"], dict[i]["day"]): dict[i] for i in dict}
    return  my_dict

now = datetime.now()
day = (now.month, now.day)

bday_dict = get_dict("birthdays.csv")
if day in bday_dict:
    folder = "letter_templates"
    my_email = "jrydel92@gmail.com"
    my_pw = "123"
    letter_list = os.listdir(folder)
    letter = choice(letter_list)
    write_and_send()


