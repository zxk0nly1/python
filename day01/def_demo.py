def     say_demo():
    print("hello world")
    print("你好世界")

# say_demo()

def my_add(a,b):# ab为函数的形参
    c=a+b
    print("a+b的值为:",c)
#my_add(10,20)# 函数的实参

def my_sum(a,b):
    if a>b:
        return  a
    else :
        return  b
# print(my_sum(10,20))

a=100#a为全局变量
def my_func(b,c): #bc为函数形参
    d=30
    a=200#相当于创建了一个和全局变量一样的局部变量，在函数内部没有权限更改全局变量
    print("b=",b)
    print("c=",c)
    print("a=",a)#函数内部可以访问全局变量

my_func(10,20)
#print(d) #函数外部不能访问局部变量
print("函数执行完毕后a:",a)