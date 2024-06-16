import datetime

#basic function for checking if tommorow's date is in our birthday list
def finder(birthday_list):
    tommorow = datetime.datetime.today() + datetime.timedelta(days=1)
    for i in birthday_list:
        if i.day == tommorow.day and i.month == tommorow.month:
            print("birthday tommorow")




# testing here
x = datetime.datetime(2020, 5, 17)
y = datetime.datetime(1920, 6, 17)
z = datetime.datetime(2024, 6, 17)

finder([x,y,z])