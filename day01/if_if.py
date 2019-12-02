n=int(input("请输入一个月份："))
if 1<=n<=12:
    if n<=3:
        print("spring")
    elif n<=6:
        print("summer")
    elif n<=9:
        print("autumn")
    else:
        print("winter")
else:
    print("你输入的月份有误")