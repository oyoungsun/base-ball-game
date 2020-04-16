import random


number1 = random.randint(1, 9)
number2 = random.randint(1, 9)
number3 = random.randint(1, 9)
number = [number1, number2, number3]

playbaseball(mynum) :
    mynum = input(">>")
    mynum = list(mynum)
    mynum = [int(i) for i in mynum]

    ball = 0
    strike = 0
    t = 0
    for i in range(0, 3):
        if mynum[i] == number[i]:
            strike += 1
            ball = ball -1
        for j in range(0, 3):
            if mynum[i] == number[j]:
              ball += 1
    print("ball", ball)
    print("strike", strike)
    print(number)
    if number == mynum:
        t = 1
        print("삼진아웃")
    else:
        t = 0
    return t

