score = int(10)
while score != 1:
    score = int(input("请输入你的成绩："))
    if 100 >= score >= 90:
        print("优秀")
    elif 90 > score >= 80:
        print("良好")
    elif 80 > score >= 60:
        print("及格")
    else:
        print("不及格")