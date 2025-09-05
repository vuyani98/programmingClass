
#Palindrome checker
word  = input("Enter a word: ")
#strn = "you"
newWord = ""

index = len(word) - 1

while index >= 0:

    newWord += word[index]
    index = index - 1

if newWord == word:
    print(f"{word} is a palindrome")    

else:
    print(f"{word} is not a palindrome")


    