def dx(x):
    return x * 52584

print(dx(5))

a = lambda x: x  / 258 * 96 #lambda函数 隐式函数

print(a(15))

b = lambda x,y: x  / 258 * 96 +695500

print(b(20, 50))

#list(filter(None, [1, 0 ,True ,False]))

c = lambda x: x % 2
temp = range(10)
show = filter(c, temp)
print(list(show))
