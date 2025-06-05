number = input("Enter a number to be reveresed: ")
if number.startswith("-"):
    reversed_number = "-" + number[:0:-1]  # skip the minus sign during slicing
else:
    reversed_number = number[::-1]
print("The reversed number is: " + reversed_number)