import datetime

# Get today's date
today = datetime.date.today()

# Convert and parse a date from a string
date = "2013:12:25 11:45:07"
convertedDate = datetime.datetime.strptime(date, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d')

print("Today is: ")
print(today) 
print("Converted date of 2013:12:25 11:45:07 is: ")
print(convertedDate)

