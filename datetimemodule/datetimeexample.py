import datetime

time_date = datetime.datetime.today()

print(f"Print Todays date and Time: {time_date}")

time_date_ran = datetime.datetime(2021, 4, 22, 20, 33, 22, 10000)

tdelta_days = datetime.timedelta(days=8)
tdelta_hours = datetime.timedelta(hours=8)

print(f"Timedate custom : {time_date_ran}")
print(f"Timedate custom + 10 days :", time_date_ran + tdelta_days)
print(f"Timedate custom + Hours :", time_date_ran + tdelta_hours)
