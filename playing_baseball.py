import random

def comnumber() :
    number1 = random.randint(1, 9)
    number2 = number1
    number3 = number1
    while number1 == number2 :
     number2 = random.randint(1, 9)
    while number1 == number3 or number2 == number3 :
     number3 = random.randint(1, 9)
    number.append(number1)
    number.append(number2)
    number.append(number3)

    return number

def playbaseball(mynum) :

    mynum = list(mynum)
    mynum = [int(i) for i in mynum]

    ball = 0
    strike = 0
    t = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if  number[i] == mynum[j]:
                if  i == j :
                    strike +=1
                else :
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

def playgame() :
    print("--- 게임시작 ---")
    print("-1 입력하면 게임을 포기합니다.")
    count = 1
    t = 0
    number = comnumber()
    while t < 1:
        print("%d회차" % count)

        mynum = input("숫자>>")
        if mynum == -1:
            break
        print("%d회차 결과" % count)
        playbaseball(mynum) # t =playbaseball
        count += 1
        print()
        if count == 11:
            print("게임오버")
            break
    count1 = count - 1
    print("걸린 회차 : %d회차 " % count1)
    print("답", number)
    print("--- 게임종료 ---")


print("야구게임")

while 1 :
    number = []
    print('-' * 5, "메뉴", '-' * 5)
    print("1. 시작 2. 규칙 3. 종료")
    a = int(input(">>"))
    if a == 1 :
       playgame()
       break



    elif a==2 :
        print("""----- 규칙 -----
        게임이 시작되면 랜덤으로 세 자리 숫자가 생성됩니다.  
        매 회 세 자리 숫자를 입력해주세요.
        자리와 값이 같으면 Strike
        값만 같으면 Ball
        10회까지 못 맞추면 게임 오버 됩니다.
        -----------------
        """)
        continue
    elif a == 3:
        break