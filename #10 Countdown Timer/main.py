import time
countdown = input("Enter the countdown time in seconds: ")
int_countdown = int(countdown)
for i in range(int_countdown, 0, -1):
    print(i)
    time.sleep(1)
print("Time's up!")