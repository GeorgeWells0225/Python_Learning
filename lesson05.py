favourite = 'FUCK'
for i in favourite:
    print(i, end='\n')
favourite = ['梁非凡', '刘醒', '卢本伟', '牛逼', 'diao']
for i in favourite:
    print(i, end='')
member = ['梁非凡', '刘醒', '卢本伟', '牛逼', 'diao']
for each in member:
    print(each, len(member))
member = ['梁非凡', '刘醒', '卢本伟', '牛逼', 'diao']
member.append('李云龙')
member.extend(['马飞飞'])
member.insert(1, '你说你马呢')
for each in member:
    print(each, len(each))
list(range(25, 50))
for i in range(1, 50):
    print(i)
for i in range(1, 100, 5):
    print(i)