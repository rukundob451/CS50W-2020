import time

SUNSET = 18  # 6 PM
SUNRISE = 6  # 6 AM

# Get the current time by calling the localtime() method in the time module.
current_time = time.localtime()

# Check if it is between sunset and sunrise
if SUNSET <= current_time.tm_hour < SUNRISE:
    print("It is day time.")
else:
    print("It is night time.")
