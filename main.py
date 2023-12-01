from random import *
from datetime import *
from tkinter import messagebox
import smtplib
import os
import pandas as p

def check_birthday():
    try:
        month_row = bday_data[bday_data.month == now.month]
        entry = month_row[month_row.day == now.day]
    except KeyError:
        messagebox.showwarning(title="Key Error", message="This data cannot be found.")
    else:
        return entry

def write_and_send():
        try:
            with open(file=f"{folder}\\{letter}", mode="r") as email_data:
                template = email_data.read()
                email = template.replace("[NAME]", f"{data_entry.name.iloc[0]}")

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_pw)
                connection.sendmail(
                    from_addr=my_email, to_addrs="address@example.com",
                    msg=f"Subject: Happy Birthday\n\n{email}")
        except FileNotFoundError:
            messagebox.showwarning(title="File Not Found", message="This file does not exist.")
        except IndexError:
            messagebox.showwarning(title="No Birthdays", message="No data of registered birthdays today.")
        else:
            messagebox.showinfo(title="Confirmation", message="Email sent successfully.")


bday_data = p.read_csv("birthdays.csv")
now = datetime.now()
folder = "letter_templates"
my_email = "jrydel92@gmail.com"
my_pw = "123"
letter_list = os.listdir(folder)
data_entry = check_birthday()
letter = choice(letter_list)
write_and_send()

