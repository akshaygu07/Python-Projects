users = {
    "alice": "password123",
    "bob": "qwerty",
    "kush": "securepass"
}
username = input("Enter your username: ")
if username in users:
    password = input("Enter your password: ")
    if users[username] == password:
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")