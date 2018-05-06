x = range(2, 50)
number = input("What is the number: ")
for elem in x:
    b = elem
    if number%b == 0:
        print elem