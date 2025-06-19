i = int(input("Enter the number of expenses to track: "))
expenses = []
total_amount = 0

for x in range(i):
    name = input("Enter the expense name: ")
    amount = float(input("Enter the expense amount: "))
    expenses.append({"name": name, "amount": amount})
    total_amount += amount

print("\nThe number of expenses tracked:", i)
print("Total amount spent:", total_amount)
print("Expense breakdown:")
for expense in expenses:
    print(f" - {expense['name']}: ${expense['amount']:.2f}")
