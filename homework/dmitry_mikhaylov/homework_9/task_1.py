from datetime import datetime


given_datetime = "Jan 15, 2023 - 12:05:33"
python_datetime = datetime.strptime(
    given_datetime, "%b %d, %Y - %H:%M:%S")

print(datetime.strftime(python_datetime, "%B"))
print(datetime.strftime(python_datetime, "%d.%m.%Y, %H:%M"))
