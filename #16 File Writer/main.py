content = input("What do you want to write to the file?")
with open("Output.txt", "w") as file:
    file.write(content)
print("Content written to Output.txt successfully.")