f = open("output.txt", "w")
f.write("Hello, this is is a test file with some text in it.")
f.close()

filename = input("Enter the file name (e.g., output.txt): ")
search_word = input("Enter the word to search for: ").lower()

with open(filename, "r") as f:
    content = f.read().lower()
    words = content.split()
    count = words.count(search_word)

print(f"The word '{search_word}' appears {count} times in the file '{filename}'.")
