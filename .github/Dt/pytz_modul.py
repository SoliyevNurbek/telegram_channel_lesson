# pytz modul in timezone() function
from datetime import datetime as dt,timezone as tz
import pytz as pz
d=dt.now(pz.tz("US/Central"))
print("US central datetime",d)
print("US central datetime isoformat()",d.isoformat())
