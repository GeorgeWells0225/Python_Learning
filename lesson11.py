cout = 5
def myfun():
    cout = 10 #非全局变量
    print(cout)

myfun()

print(cout)

def myfun1():
    global cout #定义为全局变量
    cout = 10
    print(cout)


myfun1()
print(cout)

