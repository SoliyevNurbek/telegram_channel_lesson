# date() function
from datetime import date
d=date(2003,12,14)
dh=date.today()
print("Yashagan kunim",dh-d)
print("Iso format",d.isoformat())
