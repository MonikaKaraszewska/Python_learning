'''https://www.youtube.com/watch?v=eirjjyP2qcQ&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=24'''

import datetime
print(dir(datetime))
print('')
print("............................Get Current Date and Time")
print(datetime.datetime.now())
print('')
print("...............Get Current Date")
print(datetime.date.today())
print('')



print("  .............................................................datetime.date")
print("................................video......creating date")
# don't put 0 eg.(2016,07,24)
d = datetime.date(2016,7,24)
print(d)
print("...............................wyswietlic tylko rok, albo miesiac, albo dzien")
tday = datetime.date.today()
print(tday.year)
print(tday.day)
print(tday.month)
print('')

print("...............................dzien tygodnia")
print(tday.weekday()) # because for .weekday() Monday is 0 and Sunday is 6
print(tday.isoweekday())# and here Monday is 1 and Sunday 7

print('........................ datetime.timedelta() function')
tdelta = datetime.timedelta(days=7)
# what the date will be one week from now
print(tday+tdelta)
# what the date was one week ago
print(tday-tdelta)

bday = datetime.date(2023,12,17)
till_day = bday -tday
print(till_day.days)
print(till_day.total_seconds())

print("  .............................................................datetime.time")
# datetime.date gives us date,year, day, month
# datetime.time gives us hours, minutes, seconds, microsecond
print("......................................creating time")

t = datetime.time(9, 30, 45, 100000)
print(t)

# to get access to everything(time and date at once we need datetime.()
td = datetime.datetime(2006,7,26,12,30,45,100000)
print(td)
print(datetime.datetime.now())
#form datetime.datetime() we can grab what we need, eg. only time, or only date, only year
print(td.time())
print(td.date())
print(td.year)
print(td.hour)
jetzt = datetime.datetime.now()
print(jetzt.year)
print(jetzt.hour)

print('...............timedelta .......with datetime.datetime()')
tdelta2 = datetime.timedelta(days=7)
print(td + tdelta2)
tdelta2 = datetime.timedelta(hours=7)
print(td + tdelta2)
tdelta2 = datetime.timedelta(days=7)
print(td - tdelta2)
print('....t1 / t2 / t3/ t4..')
t1 = datetime.timedelta(days=-50)
t2 = datetime.timedelta(hours=3)
t3 = datetime.timedelta(hours=5,days=7)
t4 = datetime.timedelta(weeks=-1, days=-4,
                         hours=-15, minutes=-25,
                         seconds=-54)

now = datetime.datetime.now()

print(now+t1)
print('')
print('........................datetime.datetime.today()')

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

print(".............................pytz biblioteka")
import pytz
dt = datetime.datetime(2016, 7 , 30,12, 45, tzinfo=pytz.UTC)
print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

# for tz in pytz.all_timezones:
#     print(tz)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('Singapore'))
print(dt_mtn)
dt_mtn = dt_utcnow.astimezone(pytz.timezone('Zulu'))
print(dt_mtn)
dt_mtn = dt_utcnow.astimezone(pytz.timezone('Poland'))
print(dt_mtn)


'''naive date time - the datetime representation does not have a time zone.
 aware DateTime object does include timezone information.'''

print(" ......................how to convert a string onto a date format")
# strptime - string to Datetime
dt_str = 'July 26, 2006'
dt = datetime.datetime.strptime(dt_str,'%B %d, %Y')

print(dt)

print("...........................strftime - datetime to string........")
# strftime - datetime to string
dt_mtr = datetime.datetime.now()
print(dt_mtr.strftime('%B %d, %Y'))

