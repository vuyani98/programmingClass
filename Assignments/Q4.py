word = input("Enter a word: ")
reversedWord = word[::-1]
if word == reversedWord:
    print("Palindrome")
else:
    print("Not a Palindrome")
