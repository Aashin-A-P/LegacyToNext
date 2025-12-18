import calendar
month,date,year=map(int,input().split(' '))
ans=calendar.weekday(year,month,date)
day=calendar.day_name[ans]
print(day.upper())