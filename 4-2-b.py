import re
line0  = "2018 Test log line 192.168.1.1 pinged your hostname test.com"
line1 = "2019 Test log line 192.168.1.7 aa:bb:cc:dd:43:56 pinged your hostname test.com"

lines = [line0, line1]

for line in lines:
    # Find MAC
    match = re.search("[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}", line, re.IGNORECASE)
    print("\nLine #" + str(lines.index(str(line))))
          
    if match:
        print(match.group(0))
    else:
        print("NO MAC FOUND!")
