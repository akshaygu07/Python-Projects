bill = input("Enter the bill amount: ")
tip = input("Enter the tip percentage: ")
people = input("Enter the number of people: ")

total = float(bill) * (1+float(tip)/100)
per_person = total / int(people)
print(f"Total bill amount: {total:.2f}")
print(f"Each person should pay: {per_person:.2f}")