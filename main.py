import datetime
from static import data

#basic function for checking if tommorow's date is in our birthday list
def finder(birthday_list):
    tommorow = datetime.datetime.today() + datetime.timedelta(days=1)
    for i in birthday_list:
        if int(i['birthday'][8:10]) == int(tommorow.day) and int(i['birthday'][5:7]) == int(tommorow.month):
            print(i['name'] , "has a birthday tommorow")


# testing here
finder(data)