with open("output.txt", "w") as f:
    f.write("Hello, this is a test file with some text in it.")

file = input("Enter the file name (with .txt): ")
with open(file, 'r') as f:
    content = f.read()
    number_of_words = len(content.split())
    print(f"The file {file} has {number_of_words} words.")
