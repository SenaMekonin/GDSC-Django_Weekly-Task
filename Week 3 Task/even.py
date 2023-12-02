# Question number 4
sum = 0
count = 0
for i in range(0, 50, 2):
    sum += i

    if i % 3 == 0:
        print("Three")
        count += 1
    if i % 5 == 0:
        print("Five")
        count += 1
print("Sum of even number is: ", sum)
print("Count of 3 or 5 is:", count)
