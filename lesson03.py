import random
secret = random.randint(1,10)

print("---------------------无中生有！两开花-------------------------")
temp = input("不妨输入一个数字猜一下爸爸想的是哪一个数字:")
guess = int(temp)
while guess != secret:
    temp = input("沙雕，猜错了。请重新输入吧！")
    guess = int(temp)
    if guess < secret:
        print("你怎么回事！小老弟？")
    else:
        if guess == secret:
            print("牛逼啊！小老弟？")
        else:
            print("你的吊就跟你的数一般大，小老弟！")
print("Game Over!你果然是张口就莱！")