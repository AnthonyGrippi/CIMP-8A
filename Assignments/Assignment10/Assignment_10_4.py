
message = "Stranger things!"

print(message)
print()
print("Is 'things' found in message = ", "things" in message)
print("Is 'Things' found in message = ", "Things" in message)
print("Is 'hings' found in message = ", "hings" in message)
print("Is ' things' found in message = ", " things" in message)
print()

word = input("Enter a search word: ")
if word in message:
    print(word, "was found in ", message)
else:
    print(word, "was NOT found in", message)