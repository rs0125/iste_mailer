import smtplib
import os
from dotenv import load_dotenv
import json
import datetime
import schedule
import time

load_dotenv()

months = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]

def check_bday(obj):
    name = obj["name"]
    phone = int(obj["phone_number"])
    CurrentDate = datetime.datetime.now().strftime('%Y-%m-%d')
    obj_date = obj["birthday"]
    obj_date = obj_date.split("-")
    CurrentDate = CurrentDate.split("-")
    if(int(obj_date[1]) == int(CurrentDate[1])):
        if (int(CurrentDate[2]) == (int(obj_date[2]) - 1)):
            day = obj_date[2]
            month = months[int(obj_date[1])]
            wish = f"Subject: Birthday Wish \n\nIts {name}'s birthday on {day} of {month}, Phone Number: +91{phone}"
            return wish
    return None


if __name__ == "__main__":
    email = os.environ.get('MY_EMAIL')
    rev = os.environ.get('VED_EMAIL')
    token = os.environ.get('TOKEN')
    subject = "Wish Reminder"
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(email, token)
            print("Successfully Logged in")
            try:
                with open('iste2024.json', 'r') as f:
                    data = json.load(f)
                print("Loaded Data")
                for person in data:
                    wish = check_bday(person)
                    if (wish != None):
                        server.sendmail(email, rev, wish)
                        print(f"Sent Email : {wish}")
            except Exception as e:
                print(f"Error Importing JSON File: {e}")
    except Exception as e:
        print(f"Server Unavailable: {e}")
