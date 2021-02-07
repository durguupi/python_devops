import datetime
# To work with timezone we use pytz moudle
# We can install it with pip3 install pytz
import pytz
# Prints in UTC timezone period
dt = datetime.datetime(2021, 8, 8, 1, 40, 23, tzinfo=pytz.UTC)
print(dt)
# # This prints time local timezone value
# dt_now = datetime.datetime.now()
# print(dt_now)
# This prints the time and date in UTC format. This is prefeered way of working
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

# This also prints the time and date in UTC format but its called in differnt way.
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)
