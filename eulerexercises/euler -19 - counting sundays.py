from datetime import date

sunday = 6

start = date(1901, 1 ,1)
end = date(2000, 12, 31)

count = 0
year = start.year
month = start.month
while year <= end.year and month <= end.month:
    print(str(year )+ '-' +str(month))
    test = date(year,month,1)
    if test.weekday() == sunday:
        print('found a sunday')
        count+=1
    if month == 12:
        month =1
        year +=1
    else:
        month +=1
print ("Count is: " + str(count))

