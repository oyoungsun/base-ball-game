import random

number1 = random.randint(1, 9)
number2 = number1
number3 = number1
while number1 == number2 :
    number2 = random.randint(1, 9)
while number1 == number3 or number2 == number3 :
    number3 = random.randint(1, 9)
number = [number1, number2, number3]

print(number)
