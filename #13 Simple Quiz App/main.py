score = 0
one = input("Question 1: What’s the capital of France? ").lower()
if one == "paris":
    score += 1
two = input("Question 2: What’s the capital of Germany? ").lower()
if two == "berlin":
    score += 1
print("Your score is: "+str(score)+"/2")

