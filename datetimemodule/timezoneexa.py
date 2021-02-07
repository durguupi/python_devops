import datetime
import pytz

# To print all the available timezone
# for tz in pytz.all_timezones:
#   print(tz)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

dt_india = dt_utcnow.astimezone(pytz.timezone('Asia/Calcutta'))
print(dt_india)
