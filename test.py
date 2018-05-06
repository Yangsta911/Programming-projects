test_file = open('/home/yx/Documents/test.txt')
text = test_file.read()
print(text)
a = abs(10) + abs(-10)
print(a)
b = abs(-10) + -10
print(b)

import random
num = random.randint(1, 100)
while True:
 print('Guess a number between 1 and 100')
 guess = input()
 i = int(guess)
 if i == num:
  print('You guessed right')
  break
 elif i < num:
  print('Try higher')
 elif i > num:
  print('Try lower')