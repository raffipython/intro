# Start the program
bill = 0
tip = 0
print("How much is the bill?")
bill = int(input())
tip = bill * 0.15
print("The tip is $" + str(tip))
print("The total, with tax, is $" + str(tip + bill))
# End the program