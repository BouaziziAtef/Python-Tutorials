print('\t\t *******************************')
print('\t\t **    Python-Tutorial0001    **')
print('\t\t **===========================**')
print('\t\t ** Developer : BOUAZIZI ATEF **')
print('\t\t ** BOUAZIZI-ATEF@OUTLOOK.COM **')
print('\t\t *******************************\n')
#------------------------------------------------
input('Press enter to continue...')
#------------------------------------------------
print('\n')
import datetime

print("import datetime\n")
print("print(datetime.date) ==> ", datetime.date)
print('---------------')
print("print(datetime.datetime) ==> ", datetime.datetime)
print('---------------')
print("print(datetime.time) ==> ", datetime.time)
print('---------------')
print("print(datetime.timedelta) ==> ", datetime.timedelta)
print('---------------')
print("print(datetime.timezone) ==> ", datetime.timezone)
print('---------------')
print("print(datetime.tzinfo) ==> ", datetime.tzinfo)
print('---------------')
print("print(datetime.MINYEAR) ==> ", datetime.MINYEAR)
print('---------------')
print("print(datetime.MAXYEAR) ==> ", datetime.MAXYEAR)
print('---------------')
print("print(datetime.UTC) ==> ", datetime.UTC)

print('\n------------------------------')
print("print(datetime.datetime.now()) ==> ", datetime.datetime.now())
print('---------------')
print("print(datetime.datetime.now().date()) ==> ", datetime.datetime.now().date())
print('---------------')
print("print(datetime.datetime.now().time()) ==> ", datetime.datetime.now().time())

print('\n------------------------------')
print("print(datetime.datetime.today()) ==> ", datetime.datetime.today())
print('---------------')
print("print(datetime.datetime.today().date()) ==> ", datetime.datetime.today().date())
print('---------------')
print("print(datetime.datetime.today().time()) ==> ", datetime.datetime.today().time())

print('\n------------------------------')
print("print('Today's date:', datetime.datetime.today().date())) ==> Today's date:", datetime.datetime.today().date())

print('\n------------------------------')
print("print('Current date and time: ', datetime.datetime.now()) ==> Current date and time: ", datetime.datetime.now())
print('---------------')
print("print('Current date and time: ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) ==> Current date and time: ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print('\n------------------------------')
now = datetime.datetime.now()
print('now = datetime.datetime.now()')
print("print('Current date and time:', now) ==> Current date and time:", now)
print('---------------')
print("print(now.strftime('%Y-%m-%d %H:%M:%S')) ==> ", now.strftime('%Y-%m-%d %H:%M:%S'))

print('\n------------------------------')
from time import gmtime, strftime

print("from time import gmtime, strftime")
print("print(strftime('%z', gmtime())) ==> ", strftime("%z", gmtime()))

print('\n------------------------------')
from datetime import date
ToDay = date.today()
print("from datetime import date\n")
print("ToDay = date.today()")
print("print('Today's date:', ToDay) ==> Today's date:", ToDay)
print('---------------')
print("print('We are the {:%d, %b %Y}'.format(ToDay)) ==> We are the ","{:%d, %b %Y}".format(ToDay))


#------------------------------------------------
print('\n')
input('Press enter to exit!..')