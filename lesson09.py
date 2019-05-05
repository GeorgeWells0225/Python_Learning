list = [112, 223, 554, 666, 552, 112, 113, 123, 141, 112, 123, 123, 114, 552, 112, 552, 669]

a = list.count(123)

print(a)

b = list.index(123, 3, 15)#从第三个到第15个数组123出现的第一个位置

print(b)

list.reverse()

print(list)

list.sort()

print(list)

list.sort(reverse = True)

print(list)

list1 = list[:] #将数组拷贝而不是引用

print(list1)

c = list[:5]

print(c)
