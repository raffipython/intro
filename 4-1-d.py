import re
line = "2018 Test log line 192.168.1.1 aa:bb:cc:dd:ef:14 pinged your hostname test.com "

# Find year
match = re.search("^[0-9]{4}", line)
print(match.group(0))

# Find IP
match = re.search("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", line)
print(match.group(0))

# Find MAC
match = re.search("[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}", line, re.IGNORECASE)
print(match.group(0))

