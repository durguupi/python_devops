import datetime
# date in the format of hour, minutes, seconds, milliseconds.
ti = datetime.time(9, 30, 23, 100000)

print(f"Time: {ti}")
print(f"Hours: {ti.hour}")
print(f"Minutes: {ti.minute}")
print(f"Seconds: {ti.second}")
