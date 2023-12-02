# Question number 3
word = input("Please enter the word to check: ")
if word == word[::-1]:
    print(f"The word {word} is palindrome.")
else:
    print(f''' The word {word} is not a palindrome,
 because {word[::-1]} is not equal to {word}
    ''')