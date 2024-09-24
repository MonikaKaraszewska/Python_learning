import datetime

print(dir(datetime))

today = datetime.date.today()
print("today is:",today)
print("day:",today.day)
print("month:",today.month)
print("year:",today.year)

#strftime - convert object(czyli w tym przypadku 'today') to a string according to a given format
print(today.strftime('%Y %B %d %A'))
print(today.strftime('%Y %B %dth %A'))
print(today.strftime('%y %b %dth %a'))

print("................................................replace")

next_year = today.replace(year=today.year +1)
print(next_year)
#Replace the current date’s year with the year 2000.
rok2000 = today.replace(year=2000)
print(rok2000)

#Replace the current date’s month with the month February
rok2000 = today.replace(month=2)
print(rok2000)

rok2000 = today.replace(day=22)
print(rok2000)

styczen = datetime.date(2024, 1, 1)
urodziny=datetime.date(1981,12,15)

odlicznie = abs(next_year - today)
print(odlicznie.days)

#Wyswietlam ktory to dzien tygodnia
print(urodziny.isoweekday())

# wyswietlam jaki byl dzien tygodnia
print(urodziny.strftime('%A %a %B %b'))

print("......................................data i czas")

now = datetime.datetime.now()
print("Right now is: ", now)
print("It's is the {}th minute of the {}nd hour, of the {}th day of the {}nd month of the year {}".format\
          (now.minute, now.hour, now.day, now.month, now.year))
print('')
print('...................................time')

my_time = datetime.time(23, 33,18)
print(my_time)
#wysietla godzine czy jest PM, jak wpiszemy duze P, towyswietli tak jak jest napisane czyli 23:33
print(my_time.strftime("%I:%M %p"))


my_date = datetime.datetime.combine(today,my_time)
print(my_date)
print('')
print('.....ile masz lat')
now = datetime.date.today()
urodziny =datetime.date(1981,12,15)
future = datetime.date(2050, 12,17)

sekundy = now - urodziny
print("dni z funkcji: ",sekundy.days)
minuty = sekundy.total_seconds() / 60
godziny = minuty / 60
dni = godziny / 24
lata = dni /364
print(lata)