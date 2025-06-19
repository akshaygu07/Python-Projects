numbers = list(map(int, input("Enter numbers separated by space: ").split()))
frequency = {}

for i in numbers:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print("\nFrequency of each number:")
for num, count in frequency.items():
    print(f"{num} appears {count} time{'s' if count > 1 else ''}")