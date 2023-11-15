from datetime import datetime as dt
#now() function exisaise
print("Now time all",dt.now())
print("Now time year",dt.now().year)
print("Now time month",dt.now().month)
print("Now time day",dt.now().day)
print("Now time hour",dt.now().hour)
print("Now time minute",dt.now().minute)
print("Now time second",dt.now().second)
print("Now time microsecond",dt.now().microsecond,'\n')

# instilizaing
d1=dt(year=2003,month=12,day=14,hour=22,minute=22,second=22)
d2=dt(year=2017,month=9,day=7,hour=23,minute=20,second=12)
print("Instilizing date",d1)
dy=d2-d1
print("time delta date",dy,'\n')

# format srftime() function
print("format year",dt.now().strftime("%Y"))
print("format short year",dt.now().strftime("%y"))
print("format month",dt.now().strftime("%m"))
print("format full month name",dt.now().strftime("%B"))
print("format short month name",dt.now().strftime("%b"))
print("format D > month day short year name",dt.now().strftime("%D"))
print("format day of the month",dt.now().strftime("%d"))
print("format full weekday name",dt.now().strftime("%A"))
print("format short weekday name",dt.now().strftime("%a"))
print("format hour in 24",dt.now().strftime("%H"))
print("format hour in 12",dt.now().strftime("%I"))
print("format AM/PM",dt.now().strftime("%p"))
print("format minute",dt.now().strftime("%M"))
print("format second",dt.now().strftime("%S"))
print("format hour minute second in formatting",dt.now().strftime("%X"))
print("format W ",dt.now().strftime("%W"))
print("formatting ",dt.now().strftime("%y::%m::%d %Y::%B::%A"),'\n')

# format strptime()
date_string = "2021-09-30 14:30:00"
format = "%Y-%m-%d %H:%M:%S"
print("formatting strptime()",dt.strptime(date_string,format),'\n')

# replace() function 
d3=dt(year=2003,month=12,day=14,hour=22,minute=22,second=22)
replced=d3.replace(year=2004,day=15)
print("Replce formatting ",replced,'\n')

# today() time
print("todays time",dt.today(),'\n')

# utcnow() UTC time
print("UTC time",dt.utcnow(),'\n')

