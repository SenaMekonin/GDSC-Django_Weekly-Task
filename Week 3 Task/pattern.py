# Question number 2
in_ch = input("Please enter the pattern to be printed: ")
if in_ch.lower() in ('a', 'e', 'i', 'o', 'u'):
    print("Vowels are not allowed in the input ")
else:
    if len(in_ch) == 1:
        for i in range(1, 6):
            for j in range(1, i * 2):
                print(in_ch, end="")
            print()
    elif len(in_ch) != 1:
        print("The length of the character should be 1")