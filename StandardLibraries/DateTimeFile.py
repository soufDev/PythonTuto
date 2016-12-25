# -*-coding:Latin-1 -*
import time
import datetime

date = datetime.date(2010, 12, 25)
today = datetime.date.today()
print(date)
print(today)
print(today > date)

print(datetime.date.fromtimestamp(time.time()))     #same than date.today
