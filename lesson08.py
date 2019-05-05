member = ['梁非凡', '刘醒', '卢本伟', '牛逼', 'diao','我卢本伟没有开挂']

print(member[2])

member.remove('牛逼')

print(member)

del member[3]

print(member)

member.pop()   #默认取出最后一个元素，或者在括号里加入元素序号

print(member)

member = ['梁非凡', '刘醒', '卢本伟', '牛逼', 'diao','我卢本伟没有开挂']
member = member[1:5]

print(member)