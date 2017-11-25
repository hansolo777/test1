import calendar
import re

myCal = calendar.HTMLCalendar(calendar.MONDAY)
myStr = myCal.formatmonth(2017, 12, True)

re.sub('28', '28<br/>[My Data]', myStr)


for x in range(0, 3):
    myStr = (myStr+myStr+'x')

print (myStr)

file = open('calendar.html', 'w')
file.write(myStr)
file.close()

exit
