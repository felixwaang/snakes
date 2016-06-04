#Given a doomsday for the year and a day/month/year
#return the weekday for the doomsday
#Felix 30/05/16

January = [3,4]
February = [28,29]
March = [7]
April = [4]
May = [9]
June = [6]
July = [11]
August = [8]
September = [5]
October = [10]
November = [7]
December = [12]
Months = [January,February,March,April,May,June,July,August,September,October,November,December]
WeekText = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

for _ in xrange(5):
  print ('month, "/", day, "/", year')
    
  while (doomsDay > 7):
    doomsDay = doomsDay - 7
        
  if (month > 2):
    part6 = (day+14) - Months[month-1][0]
    myDay = doomsDay + part6
    while (myDay > 7):
      myDay = myDay - 7
  else:
    if ((year % 400) != 0 and (year % 4) != 0):
      part6 = (day+35) - Months[month-1][0]
      myDay = doomsDay + part6
      while (myDay > 7):
        myDay = (myDay - 7)
    else:
      part6 = (day+35) - Months[month-1][1]
      myDay = doomsDay + part6
      while (myDay > 7):
        myDay = myDay - 7
        
    print ("The answer is: "), WeekText[int(myDay)-1]
    
