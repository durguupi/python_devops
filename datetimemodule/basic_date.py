import datetime

d = datetime.date(2019, 10, 14)

print(d)

# For seeing todays date
dtoday = datetime.date.today()

print(f"Today's date is: {dtoday}")
print(f"Year: {dtoday.year}")
print(f"Month: {dtoday.month}")
print(f"Day: {dtoday.day}")

# Weekday
# Monday 0 sunday 6
print(dtoday.weekday())
# For ISO weekday Monday 1 sunday 7
print(dtoday.isoweekday())
