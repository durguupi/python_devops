import datetime

tday = datetime.date.today()

tdelta = datetime.timedelta(days=7)
# Adding seven days todays date
print(f"After Seven days date will be: ", tday + tdelta)
# Subtracting todays date and getting the last week
print(f"Before Seven days date will be: ", tday - tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2
bday = datetime.date(2021, 6, 17)
till_bday = bday - tday

print(f"From today to birthday how many days remaning: {till_bday}")

print(f"From today to birthday how many days remaning: {till_bday.days}")


print(
    f"From today to birthday how many seconds remaning: {till_bday.total_seconds()}")
