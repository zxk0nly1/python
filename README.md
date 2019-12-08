# python
python
# day01
day01
## 1、python基础

### 1、python中的变量

### 2、python中的数据类型

#### 整型 浮点型 复数 布尔类型

#### 复数分为实部和虚部

### 3、python中的算术运算符

#### +

#### -

#### *

#### /

#### // 地板除(取整运算)

#### % 取余运算

#### ** 幂运算

### 4、if条件判断语句

#### 让程序根据条件选择性的执行某条或者某些语句

```python
if 条件表达式1:
  语句块1
elif 条件表达式2:
  语句块2
else:
  语句块3
```



#### if与elif语句的区别

#### 当程序中需要使用多条语句进行判断的时候，如果判断语句全部为if语句，那当第一条if语句满足条件后，程序不会结束，而会继续向下判断所有的if语句中的真值表达式，执行所有满足表达式的语句。如果使用if语句和elif语句,当第一条if语句或者任意一个elif语句满足条件后，程序不会再向下继续判断，直接结束程序的执行

### 5、if语句的嵌套

```python
n=int(input("请输入一个月份："))
if 1<=n<=12:
  if n<=3:
    print("春季！")
  elif n<=6:
    print("夏季！")
  elif n<=9:
    print("秋季！")
  else:
    print("冬季！")
else:
  print("您输入的月份有误！")
```

### 6、字符串 str

#### 在python中用引号引起来的部分都称为字符串

##### ''

##### ""

##### ''''''

##### """"""

##### 引号的区别:

#### 1、单引号内的双引号不算做结束符

#### 2、双引号内的单引号不算做结束符

#### 3、三引号一般用于表示函数或者类的文档字符串

#### 4、三引号内可以包含单引号和双引号，三引号内的换行符会自动转换为\n

### 7、字符串的运算(不可变序列)

##### += 用于原字符串与运算符右侧的字符串进行拼接

* ##### 生成重复的字符串(只能和正整型数进行运算)

  ##### *= 生成重复的字符串

  ### 8、字符串的索引与切片

  ##### 索引 index

  ##### 从字符串中获取任意一个字符

  ##### 索引分为正向索引和反向索引

  ##### 正向索引从0开始，第一个元素的索引为0，第二个元素索引为1，以此类推，最后一个元素的

  ##### 索引为字符串的长度-1

  ##### 反向索引从-1开始，最后一个元素的索引为-1，倒数第二个元素的索引为-2，以此类推，第一

  ##### 个元素的索引为字符串长度的相反数

  #### s="A B C D E F"

  #### 正向索引 0 1 2 3 4 5

  #### 反向索引 -6 -5 -4 -3 -2 -1

  #### 语法规则:

  #### 字符串[整数表达式]

  #### 切片 slice

  #### 从字符串中获取连续或者带有一定间隔的字符

  #### 语法规则:

  #### 字符串[起始索引:终止索引:步长]

  #### 起始索引:切片切下的位置

  #### 终止索引:切片的终止点，但是不包含终止点

  #### 步长：切片每次获取完元素后，移动的方向和偏移量(没有步长相当于步长为1)

  #### 当步长为正数时，取正向切片

  #### 当步长为负数时，取反向切片

  #### 当切片带有步长时，切片获取完第一个元素后，用第一个元素的索引加上步长得到一个新的

  #### 索引，然后获取这个新索引所对应的元素，以此类推

  #### 当步长为负数时，起始索引所对应的元素必须在终止索引所对应元素的右边

  ### 9、while循环

  #### 让程序根据条件重复的执行某条或某些语句

  ```python
  i=循环变量初始值
  while 真值表达式:
    语句块1
  else:
    语句块2
  ```

  #### 从终端输入一个数字打印出如下的图形

  ##### 如输入：5

  ##### 1 2 3 4 5

  ##### 1 2 3 4 5

  ##### 1 2 3 4 5

  ##### 1 2 3 4 5

  ##### 1 2 3 4 5

  ```python
  n=int(input("请输入一个整数:"))
  i=1
  while i<=n:
    j = 1
    while j <= n:
      print(j, end=" ")
      j += 1
    print()
    i+=1
  ```

  ### 10、for循环

  ##### 遍历可迭代对象中的数据元素

  ##### 可迭代对象是指能够依次获取数据元素的对象

  ```python
  for 变量 in 可迭代对象:
    语句块1
  else:
    语句块2
  
  s="ABCDEF"
  for i in s:
    print(i)
  else:
    print("for循环因迭代结束而终止！")
  ```

  ### 11、for循环嵌套

  ```python
  for i in "ABC":
    for j in "123":
      print(i+j)
  ```

  ### 12、列表 list

  #### 列表可以存储任意类型的数据

  #### 列表是可变序列

  #### 1、表示方式

  ```python
  >>> L=[]
  >>> L
  []
  >>> type(L)
  <class 'list'>
  >>> L=["abc",100,200,3.14,[1,2]]
  >>> L
  ['abc', 100, 200, 3.14, [1, 2]]
  >>>
  ```

  ##### 2、列表的运算

  ##### +

  ##### +=

  ##### *

  ##### *=

  ```python
  >>> s="abc"
  >>> id(s)
  2537354902976
  >>> s=s+"123"
  >>> s
  'abc123'
  >>> id(s)
  2537384186128
  >>>
  >>>
  >>> s="abc"
  >>> id(s)
  2537354902976
  >>> s+="123"
  >>> s
  'abc123'
  >>> id(s)
  2537384186184
  >>>
  >>>
  >>>
  >>> L=[1,2,3]
  >>> id(L)
  2537384176264
  >>> L=L+[4,5,6]
  >>> L
  [1, 2, 3, 4, 5, 6]
  >>> id(L)
  2537384175432
  >>>
  >>>
  >>> L=[1,2,3]
  >>> id(L)
  2537384176264
  >>> L+=[4,5,6]
  >>> L
  [1, 2, 3, 4, 5, 6]
  >>> id(L)
  2537384176264
  >>
  ```

  #### 3、索引与切片

  ##### 列表的索引与切片规则和字符串的索引切片规则完全相同

  #### 4、索引与切片赋值

  ```python
  >>> L=[1,2,3,4,5,6,7]
  >>>
  >>> L[2]
  3
  >>> L[2]="B"
  >>> L
  [1, 2, 'B', 4, 5, 6, 7]
  ```

  #### 切片赋值

  #### 1、当切片赋值取出的数据为连续的时候，可以赋值给他任意个数据

  #### 2、当切片赋值的步长不为1时，切片取出的数据个数和赋值的数据个数必须相同

  #### 3、当切片赋值的起始索引和终止索引相同时，代表在这个索引所对应的元素前面插入数据

  ### 13、字典 dict

  #### 字典是可变序列，字典的存储是无序的

  #### 字典的存储方式是由键值对映射存储

  #### 每个键值对之间用逗号分隔，键和值之间用冒号进行连接

  #### 字典的键必须为不可变元素，字典的值可以为任意元素

  #### 字典的键不可重复，是唯一的

  #### 1、表示方式

  ```python
  >>> d={}
  >>> d
  {}
  >>> type(d)
  <class 'dict'>
  >>> d={"name":"小明","age":20}
  >>> d
  {'name': '小明', 'age': 20}
  >>>
  ```

  ### 2、字典的基本操作

  #### 1、增加键值对

  #### 增加的键值对的键值不存在原字典中

  ```python
  >>> d
  {'name': '小明', 'age': 20}
  >>> d["sex"]="男"
  >>> d
  {'name': '小明', 'age': 20, 'sex': '男'}
  >>
  ```

  ##### 2、修改键值对

  ##### 增加的键值对的键存在于原字典中

  ```python
  >>> d
  {'name': '小明', 'age': 20, 'sex': '男'}
  >>> d["age"]=30
  >>> d
  {'name': '小明', 'age': 30, 'sex': '男'}
  >>>
  ```

  ##### 3、删除键值对

  ```python
  >>> d
  {'name': '小明', 'age': 30, 'sex': '男'}
  >>> del d["sex"]
  >>> d
  {'name': '小明', 'age': 30}
  >>>
  ```

  #### 3、字典的遍历

  #### 字典的任何操作都是有键来进行操作

  ```python
  d={"name":"小明","age":20,"sex":"男"}
  for key in d:
    print(d[key])
  ```

  #### 14、元组 tuple

  #### 元组是不可变序列

  #### 元组可以存储任意类型的元素

  #### 元组的索引与切片规则和字符串中的规则完全相同

  ### 1、表示方式

  #### 当元组中只存放一个元素时，需要在这个元素后面加一个逗号，用来区分是单个的数据对象

  #### 还是一个元组

  ```python
  >>> t=(100)
  >>> t
  100
  >>> type(t)
  <class 'int'>
  >>>
  >>> t=(100,)
  >>> t
  (100,)
  >>>
  >>> type(t)
  <class 'tuple'>
  >>>
  ```

  ### 15、函数

  ```python
  def 函数名(参数列表):
    pass
  ```

  #### 有参数有返回值函数

  #### 有参数无返回值函数

  #### 无参数有返回值函数

  #### 无参数无返回值函数

  ```python
  def say_demo():
    print("hello world!")
    print("你好世界！")
  say_demo()
  def my_add(a,b): # a,b为函数的形参
    c=a+b
    print("a+b的值为:",c)
  my_add(10,20) # 10,20为函数的实参
  ```

  #### 1、return语句

  ##### 如果函数想返回一个指定的对象，就需要用到return语句

  ##### 语法:

  ##### return 对象1，对象2,....

  #### 1、如果一个函数中没有return语句相当于在函数末尾加了一行return None	

  #### 2、如果return语句后面没有返回的指定对象，相当于return None

  #### 3、return的作用是结束当前函数的执行，并且返回到调用该函数的地方

  ```python
  def my_sum(a,b):
    if a > b:
      return  a
    else:
      return  b
  print(my_sum(10,20))
  a=100 # a 为全局变量
  def my_func(b,c): # b,c为函数的形参 是局部变量
    d=30
    a=200 # 相当于创建了一个和全局变量相同名称的局部变量，在函数内部没有权限更改全局变量
    print("b=",b)
    print("c=",c)
    print("a=",a) #函数内部可以访问全局变量
  my_func(10,20)
  # print(d) #函数外部不可以访问局部变量
  print("函数执行完毕后a=",a)
  ```

  ### 16、面向对象编程

  #### 类 class

  ##### 具有相同属性或者行为的对象归为一个集合即为一个类

  ##### 类是产生对象(实例)的工厂

  #### 1、类的创建

  ```python
  class 类名(继承列表):
    实例方法
    类方法
    类变量
    静态方法
  ```

  #### 2、类的实例化(类的调用)

  ##### 对象=类名(参数列表)

  ```python
  class Car(object):
    """
   此类是一个汽车类
   """
    pass
  car=Car()  # 类的实例化
  print(id(car))
  car1=Car()
  print(id(car1))
  ```

  #### 3、实例属性

  ##### 给类产生的对象或者实例添加一个属性

  ##### 对象.实例属性名=属性值

  ###### **car** . color="红色"

  ```python
  class Car(object):
    """
   此类是一个汽车类
   """
    pass
  car=Car()  # 类的实例化
  car.color="黑色" #给对象添加上颜色的属性
  car1=Car()
  car1.color="红色"
  ```

  #### 4、实例方法

  ##### 让类产生的对象可以具备某些行为或者属性

  ```python
  class 类名():
    def 实例方法名(参数列表):
      pass
  ```

  **实例方法的本质就是定义在类内的函数，每个对象或者实例都可以调用**

  ```python
  class Car(object):
    """
   此类是一个汽车类
   """
    def get_speed(self,speed):
      """
     此实例方法是给对象添加速度的一个方法
     """
      self.car_speed=speed #给对象添加上速度的属性
      print(self.color,"正在以",self.car_speed,"的速度行驶！")
  car=Car()  # 类的实例化
  car.color="黑色" #给对象添加上颜色的属性
  car1=Car()
  car1.color="红色"
  ```

  #### 5、实例方法的调用

  ##### 实例.实例方法名(参数列表)

  ##### self代表类的实例，他是实例方法中的第一个参数，一般默认为self

  ```python
  class Car(object):
    """
   此类是一个汽车类
   """
    def get_speed(self,speed):
      """
     此实例方法是给对象添加速度的一个方法
     """
      self.car_speed=speed #给对象添加上速度的属性
      print(self.color,"的汽车正在以",self.car_speed,"的速度行驶！")
  car=Car()  # 类的实例化
  car.color="黑色" #给对象添加上颜色的属性
  car.get_speed(200) #调用实例方法
  car1=Car()
  car1.color="红色"
  car1.get_speed(150)
  ```

  ##### 6、类的构造函数(初始化函数)

  ```python
  class 类名(继承列表):
    def __init___(self,参数列表):
      pass
  ```

  ##### 类的构造函数会在类的实例化过程中自动调用，构造函数中一般会存放一些类产生的对象所

  ##### 具备的公有属性

  ##### 构造函数的名称必须为init不可改变

  ```python
  class Car(object):
    def __init__(self,color,brand):
      self.color=color
      self.brand=brand
    def get_speed(self,speed):
      self.speed=speed
      print(self.color, "的", self.brand, "汽车正在以", self.speed, "的速度行驶！")
      
  car=Car("黑色","奔驰")
  car.get_speed(120)
  car1=Car("红色","奥迪")
  car1.get_speed(200)
  ```

  #### 7、类的继承与派生

  ##### 类的继承代表子类可以具备父类所具有的属性和行为

  ##### 类的派生是指在子类中添加新的功能

  ```python
  class Father(object):
    def say(self,what):
      print("正在说:",what)
    def walk(self,distance):
      print("行走了",distance,"米")
  class Son(Father):
    def study(self,subject):
      print("正在学",subject)
  son=Son() # 子类实例化产生对象
  son.say("你好")
  son.walk(1000)
  father=Father()
  son.study("python")
  ```

  ### 17、python中的文本文件操作

  #### 操作模式

  #### r 只读模式

  #### w 只写模式

  #### a 追加写入

  #### rb 二进制读取模式

  #### wb 二进制写入模式

  ```python
  with open(文件名,操作模式,encoding="utf-8") as f:
    操作语句
  ```

  #### 1、文件的写入

  ##### f.write()

  ```python
  with open("data.txt","w",encoding="utf-8") as f:
    f.write("hello 100 200 你好")
  ```

  #### 2、文件的读取

  ##### f.read()

  ```python
  with open("data.txt","r",encoding="utf-8") as f:
    info=f.read()
    print(info)
  ```

  ### python -m pip install requests

  ### python -m pip install lxml

  ### python -m pip install bs4

  ### python -m pip install jieba

  ### python -m pip install wordcloud

  ### python -m pip install imageio

  ### python -m pip install matplotlib

# day02
day02

### <https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E7%AF%AE%E7%90%83&rsv_pq=92d663eb00032c69&rsv_t=c951RWw%2BlMsZRDpulGDfnDjBmyp%2BOD30PHre9B%2Buh87vNghl3iXlFbrmDj4&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=9&rsv_sug1=2&rsv_sug7=001&rsv_sug2=0&prefixsug=%25E7%25AF%25AE%25E7%2590%2583&rsp=8&rsv_sug9=es_0_1&inputT=936&rsv_sug4=78696&rsv_sug=9>

# 1、python爬虫下载器

## 1、requests模块

### 1、先确定要抓取的网站的地址url

### 2、对url发起请求并获取响应(网页的源代码)

### 3、requests.get()方法

#### 对网页发起请求并获取响应信息

#### requests.get(url,headers={},params={})

#### url:请求的网页的地址

```python
import requests


url="https://www.baidu.com/"  #确定抓取网页的url
res=requests.get(url)  # 对网页发起请求并获取响应信息
res.encoding="utf-8"
html=res.text #解析得到的相应内容
print(html)
```

#### headers:请求携带的浏览器以及操作系统信息

```python
import requests


url="https://www.baidu.com/"  #确定抓取网页的url
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
res=requests.get(url,headers=headers)  # 对网页发起请求并获取响应信息
res.encoding="utf-8"
html=res.text #解析得到的相应内容
print(html)
```

#### params:请求携带参数的字典

#### 模拟登陆：登陆账号之后寻找登陆的请求，找到用户的cookie信息，然后让请求携带这个信息去请求网页

```python
import requests

url="https://www.baidu.com/s?"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
         "Cookie":"BIDUPSID=20BA20A6474681053EA56436BC4B3D97; PSTM=1574518658; BAIDUID=9276E50B9B762C87B246AFFF86AFE4CB:FG=1; BD_UPN=12314753; ispeed_lsm=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=25_0_9_6_9_8_0_0_9_5_3_0_0_0_0_0_1575166622_0_1575337152%7C9%230_0_1575337152%7C1; H_PS_645EC=326b1bFfVwAZMn%2BEr2lUzz5jDYz09GAGHFBdUD0mYZboAS5tNtdv1A7yck4; delPer=0; BDUSS=FpvfnhINXpMeldCMU5NRDQ0STdRNi1QS2RLaDFKSTZHcnR2aEJLZmVxZWpUUTFlRUFBQUFBJCQAAAAAAAAAAAEAAAA2JBrPZmx50sHA-9ChuOe45wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKPA5V2jwOVdb; BD_HOME=1; H_PS_PSSID=1438_21105_30210_20698_22159"}
params={
    "wd":"篮球"
}
res=requests.get(url,headers=headers,params=params)
res.encoding="utf-8"
html=res.text
print(res.url) #返回请求的真实url地址
print(html)
```

# 2、range()函数

### 整数迭代生成器

```python
import requests

url="https://www.baidu.com/s?"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
         "Cookie":"BIDUPSID=20BA20A6474681053EA56436BC4B3D97; PSTM=1574518658; BAIDUID=9276E50B9B762C87B246AFFF86AFE4CB:FG=1; BD_UPN=12314753; ispeed_lsm=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=25_0_9_6_9_8_0_0_9_5_3_0_0_0_0_0_1575166622_0_1575337152%7C9%230_0_1575337152%7C1; H_PS_645EC=326b1bFfVwAZMn%2BEr2lUzz5jDYz09GAGHFBdUD0mYZboAS5tNtdv1A7yck4; delPer=0; BDUSS=FpvfnhINXpMeldCMU5NRDQ0STdRNi1QS2RLaDFKSTZHcnR2aEJLZmVxZWpUUTFlRUFBQUFBJCQAAAAAAAAAAAEAAAA2JBrPZmx50sHA-9ChuOe45wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKPA5V2jwOVdb; BD_HOME=1; H_PS_PSSID=1438_21105_30210_20698_22159"}
for page in range(1,5):
    pn=(page-1)*10  #构造翻页参数的值
    params={
        "wd":"篮球",
        "pn":str(pn)
    }
    res=requests.get(url,headers=headers,params=params)
    res.encoding="utf-8"
    html=res.text
    print(res.url) #返回请求的真实url地址
    print(html)
```

# 3、起点小说

```python
import requests
from user_headers import L
import random

url="https://www.qidian.com/all?"
headers={"User-Agent":random.choice(L)}
for page in range(1,5):
    params={
        "page":str(page)
    }
    res=requests.get(url,headers=headers,params=params)
    res.encoding="utf-8"
    html=res.text
    filenmae="第"+str(page)+"页.html"
    with open(filenmae,"w",encoding="utf-8") as f:
        f.write(html)
        print(filenmae,"下载成功！")
```

# 4、解析模块

### 正则表达式

### bs4

### xpath表达式

# 5、正则表达式

## import re  导入正则表达式模块

## 1、re.match()方法

### 从字符串的开头进行匹配，返回符合正则表达式的数据

#### 如果字符串的开头和正则表达式不匹配的话，直接返回None对象

| 元字符 | 作用                                 |
| ------ | ------------------------------------ |
| \s     | 匹配一个空白字符                     |
| \w     | 匹配字母数字下划线普通字符           |
| \W     | 匹配特殊字符                         |
| \d     | 匹配一个数字                         |
| .      | 代表匹配任意字符(\n除外)             |
| +      | 匹配前面的表达式多次                 |
| {m}    | 精确匹配前面的表达式m次              |
| ?      | 非贪婪匹配                           |
| ()     | 分组(想要什么数据就给什么数据加括号) |
| *      | 匹配出现1次或任意次的字符            |
| ^      | 从头开始匹配                         |
| $      | 匹配到末尾结束                       |

```python
import re

s="hello world 1234 5678 你好"
# result=re.match('^h\w\w\w\w\s\w{5}',s)
# result=re.match('^h(\w{4}\s\w{5})\s(\d{4}\s\d{4})',s)
result=re.search('^h.*',s)
print(result.group())
```

## 2、贪婪匹配与非贪婪匹配

### 贪婪匹配:在正则表达式匹配成功的前提下，尽可能多的匹配数据(.*)

### 非贪婪匹配:在正则表达式匹配成功的前提下，尽可能少的匹配数据(.*?)

```python
import re

s="hello world 12345678 你好"
# result=re.match('^h\w\w\w\w\s\w{5}',s)
# result=re.match('^h(\w{4}\s\w{5})\s(\d{4}\s\d{4})',s)
# result=re.search('^h.*',s)
result=re.match('^h(.*?)(\d+)',s)
print(result.group(1))
print(result.group(2))
```

## 3、search()方法

### 扫描整个字符串，返回第一个符合正则表达式的数据

```python
result=re.search('\w\s',s)
print(result.group())
```

#### 如果字符串中有多个区间满足正则表达式，也只能返回第一个满足的数据

## 4、findall()方法

### 扫描整个字符串，返回所有满足正则表达式的数据列表

### findall里没有group()方法

```python
result=re.findall('\w\s',s)
print(result)
```

## 5、标志位

### 正则表达式可以通过一些标志位来满足一些特殊的需求

#### re.S 代表可以进行多行匹配

```python
result=re.findall('.*',s,re.S)
print(result)
```

## 6、re.compile()

### 将字符串编译为一个正则表达式对象

```python
p=re.compile('.*',re.S)
result=re.findall(p,s)
print(result)
```

# 6、起点小说解析

```python
import re

html="""
<div class="book-mid-info">
                    <h4><a href="//book.qidian.com/info/1004608738" target="_blank" data-eid="qd_B58" data-bid="1004608738">圣墟</a></h4>
                    <p class="author">
                        <img src="//qidian.gtimg.com/qd/images/ico/user.f22d3.png"><a class="name" href="//my.qidian.com/author/4362453" data-eid="qd_B59" target="_blank">辰东</a><em>|</em><a href="//www.qidian.com/xuanhuan" target="_blank" data-eid="qd_B60">玄幻</a><i>·</i><a class="go-sub-type" data-typeid="21" data-subtypeid="8" href="javascript:" data-eid="qd_B61">东方玄幻</a><em>|</em><span>连载</span>
                        
                    </p>
                    <p class="intro">
                        在破败中崛起，在寂灭中复苏。沧海成尘，雷电枯竭，那一缕幽雾又一次临近大地，世间的枷锁被打开了，一个全新的世界就此揭开神秘的一角……
                    </p>
                    <p class="update"><span><style>@font-face { font-family: CjUTgyWy; src: url('https://qidian.gtimg.com/qd_anti_spider/CjUTgyWy.eot?') format('eot'); src: url('https://qidian.gtimg.com/qd_anti_spider/CjUTgyWy.woff') format('woff'), url('https://qidian.gtimg.com/qd_anti_spider/CjUTgyWy.ttf') format('truetype'); } .CjUTgyWy { font-family: 'CjUTgyWy' !important;     display: initial !important; color: inherit !important; vertical-align: initial !important; }</style><span class="CjUTgyWy"></span>万字</span>
                        
                    </p>
                </div>
"""
p=re.compile('<div class="book-mid-info">.*?data-bid.*?>(.*?)</a>.*?class="intro">(.*?)</p>',re.S)
data=re.findall(p,html)
print(data)
```

#### 面向对象

```python
import requests
import re
from user_headers import L
import random

class Qidian:
    def __init__(self):
        self.url = "https://www.qidian.com/all?"
        self.headers = {"User-Agent": random.choice(L)}

    def change_page(self):  # 进行翻页的函数
        for page in range(1,5):
            params={
                "page":str(page)
            }
            self.get_html(params)  # 调用获取网页源代码的函数

    def get_html(self,params):  # 获取网页源代码的函数
        res=requests.get(self.url,headers=self.headers,params=params)
        res.encoding="utf-8"
        html=res.text
        self.get_data(html)  # 调用解析数据的函数

    def get_data(self,html):  # 解析网页数据的函数
        p = re.compile('<div class="book-mid-info">.*?data-bid.*?>(.*?)</a>.*?class="intro">(.*?)</p>', re.S)
        data = re.findall(p, html)
        print(data)


    def save_data(self):  # 保存数据的函数
        pass

qidian=Qidian()
qidian.change_page()
```

# 7、csv文件的操作

```python
import csv

L=["小明","20","男"]
L1=["小红","25","女"]
with open("data.csv","w",encoding="utf-8",newline="") as f: #newline参数是为了防止出现空行
    writer=csv.writer(f)  #创建写入对象
    writer.writerow(L)
    writer.writerow(L1)
```

```python
import requests
import re
from user_headers import L
import random
import csv

class Qidian:
    def __init__(self):
        self.url = "https://www.qidian.com/all?"
        self.headers = {"User-Agent": random.choice(L)}

    def change_page(self):  # 进行翻页的函数
        with open("xiaoshuo.csv", "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["小说名称","小说简介"])
        for page in range(1,5):
            params={
                "page":str(page)
            }
            self.get_html(params)  # 调用获取网页源代码的函数

    def get_html(self,params):  # 获取网页源代码的函数
        res=requests.get(self.url,headers=self.headers,params=params)
        res.encoding="utf-8"
        html=res.text
        self.get_data(html)  # 调用解析数据的函数

    def get_data(self,html):  # 解析网页数据的函数
        p = re.compile('<div class="book-mid-info">.*?data-bid.*?>(.*?)</a>.*?class="intro">(.*?)</p>', re.S)
        data = re.findall(p, html)
        self.save_data(data) #调用保存数据的函数

    def save_data(self,data):  # 保存数据的函数
        for i in data:
            title=i[0]  #获取小说的名称
            text=i[1].strip()  #获取小说的简介 strip()代表去掉字符串两边的空白字符以及换行符
            content=[title,text] #创建写入csv文件的数据列表
            with open("xiaoshuo.csv","a",encoding="utf-8",newline="") as f:
                writer=csv.writer(f)
                writer.writerow(content)
                print("数据写入成功！")


qidian=Qidian()
qidian.change_page()
```

# 8、猫眼电影

```python
html="""
<div class="movie-item-info">
        <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
        <p class="star">
                主演：张国荣,张丰毅,巩俐
        </p>
<p class="releasetime">上映时间：1993-07-26</p>    </div>
"""

import re

p=re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>',re.S)
data=re.findall(p,html)
print(data)
```

# 9、xpath解析器

## from lxml import etree

## from lxml import html

### xpath解析器是在xml文档中寻找数据的一种工具

| 元字符 | 作用                   |
| ------ | ---------------------- |
| /      | 获取当前节点           |
| //     | 获取当前节点的子孙节点 |
| @      | 获取节点的属性         |
| text() | 获取节点的文本信息     |
| ../    | 获取当前节点的父节点   |

```python
from lxml import etree

html="""
<div class="movie-item-info">
        <p class="name"><a href="/films/13824" title="射雕英雄传之东成西就" data-act="boarditem-click" data-val="{movieId:13824}">射雕英雄传之东成西就</a></p>
        <p class="star">
                主演：张国荣,梁朝伟,张学友</p>
        <p class="releasetime">上映时间：1993-02-05(中国香港)</p>    
</div>
<div class="d1">
        <li id="link1">百度</li>
        <li id="link2">新浪</li>
        <li id="link3">网易</li>
        <p>hello world</p>
        <p>你好世界！</p>
</div>
"""
parse_html=etree.HTML(html) #将网页源代码转换成xpath对象
#获取class=movie-item-info的div节点下的class=name的p节点下的a节点的title属性
data=parse_html.xpath('//div[@class="movie-item-info"]/p[@class="name"]/a/@title')
# data=parse_html.xpath('//div') #获取所有的div节点
# data=parse_html.xpath('//p')
# data=parse_html.xpath('//div/p') #获取div节点下的p节点的信息
# data=parse_html.xpath('//div[@class="d1"]/p') #获取class=d1的div节点下p节点的信息
# data=parse_html.xpath('//div[@class="d1"]/p/text()') #获取class=d1的div节点下的p节点中的文本信息
# data=parse_html.xpath('//div[@class="d1"]/p[1]/text()') #获取class=d1的div节点下的第一个p节点中的文本信息
print(data)
```

# 10、学院官网

```python
import requests
from lxml import etree
from user_headers import L
import random


class Cunjin:
    def __init__(self):
        self.url="http://www.gdcjxy.com/index.html"
        self.headers={"User-Agent":random.choice(L)}

    def get_html(self,url):  #获取网页源代码并将源代码转换成xpath的函数
        res=requests.get(url,headers=self.headers)
        res.encoding="utf-8"
        html=res.text
        parse_html=etree.HTML(html) #将源代码转换为xpath对象
        return parse_html

    def get_t_link(self): #获取帖子中的站内链接的函数并拼接成完整链接
        parse_html=self.get_html(self.url) #对官网主页发起请求
        t_url=parse_html.xpath('//a[@class="p"]/@href')
        for link in t_url:
            url="http://www.gdcjxy.com"+link
            self.get_pic_url(url) #调用获取图片链接的函数


    def get_pic_url(self,url): #获取所有图片链接的函数
        parse_html=self.get_html(url)
        pic_url=parse_html.xpath('//span[@style="font-size:18px;"]/img/@src')
        for link in pic_url:
            pic_link="http://www.gdcjxy.com"+link
            print(pic_link)

    def save_pic(self): #将图片下载到本地的函数
        pass

cunjin=Cunjin()
cunjin.get_t_link()
```





# day03
day03

# 1、非结构化数据的下载

```python
import requests


url="图片链接.jpg"
res=requests.get(url,headers)
res.enconding="utf-8"
html=res.content  #将图片转换为二进制字节流
with open("data.jpg","wb") as f:
    f.write(html)
```

```python
import requests
from lxml import etree
from user_headers import L
import random
import os


class Cunjin:
    def __init__(self):
        self.url="http://www.gdcjxy.com/index.html"
        self.headers={"User-Agent":random.choice(L)}

    def get_html(self,url):  #获取网页源代码并将源代码转换成xpath的函数
        res=requests.get(url,headers=self.headers)
        res.encoding="utf-8"
        html=res.text
        parse_html=etree.HTML(html) #将源代码转换为xpath对象
        return parse_html

    def get_t_link(self): #获取帖子中的站内链接的函数并拼接成完整链接
        self.files="./寸金学院"
        if not os.path.exists(self.files): #检测当前路径是否存在同名文件夹
            os.mkdir(self.files)
        parse_html=self.get_html(self.url) #对官网主页发起请求
        t_url=parse_html.xpath('//a[@class="p"]/@href')
        for link in t_url:
            url="http://www.gdcjxy.com"+link
            self.get_pic_url(url) #调用获取图片链接的函数


    def get_pic_url(self,url): #获取所有图片链接的函数
        parse_html=self.get_html(url)
        pic_url=parse_html.xpath('//span[@style="font-size:18px;"]/img/@src')
        for link in pic_url:
            pic_link="http://www.gdcjxy.com"+link
            filename=self.files+"//"+pic_link[-15:] #以图片链接的后15位作为图片的名称
            self.save_pic(pic_link,filename) #调用保存图片的函数

    def save_pic(self,pic_link,filename): #将图片下载到本地的函数
        res=requests.get(pic_link,headers=self.headers)
        res.encoding="utf-8"
        html=res.content
        with open(filename,"wb") as f:
            f.write(html)
            print(filename,"下载成功！")


cunjin=Cunjin()
cunjin.get_t_link()
```

# 2、bs4选择器

## python -m pip install bs4

### from bs4 import BeautifulSoup

```python
from bs4 import BeautifulSoup

html=""""""
soup=BeautifulSoup(html,"lxml") #将源代码转换为soup对象

```

## 1、节点选择器

```python
soup=BeautifulSoup(html,"lxml") #将源代码转换为soup对象
# data=soup.div
data=soup.a
print(data)
```

## 2、获取节点属性

```python
# data=soup.a.attrs["class"]
data=soup.a["class"]
print(data)
data=soup.div.a["class"] #嵌套选择
print(data)
```

## 3、方法选择器

### 查询所有符合条件的元素，给他传入一些属性或文本，就可以得到所有符合条件的元素

```python
# data=soup.find_all(name="div")  #查找所有节点名称为div的节点信息
# data=soup.find_all(attrs={"id":"link"})
data=soup.find_all(id="link")
print(data)
# data=soup.find_all(class_="d1")
data=soup.find_all("div",class_="d1") # 查找class=d1的div节点信息
print(data)
```

## 4、css选择器

### 使用css选择器，调用select方法，可以查找定位符合条件的元素

```python
#thread_list > li:nth-child(9) > div > div.col2_right.j_threadlist_li_right > div.threadlist_lz.clearfix > div.threadlist_title.pull_left.j_th_tit
```

```python
soup=BeautifulSoup(html,"lxml") #将源代码转换为soup对象
# data=soup.select('div > ul > li') #层级选择
data=soup.select("div.threadlist_title") #通过选择器属性定位节点信息
print(data)
data=soup.select('div > ul > li') #层级选择
print(data)
for i in data:
    print(i.text) #获取节点中的文本信息
    print(i.string)
```

# 3、古诗词项目

## www.gushiwen.org

## 1、获取所有页面的古诗的标题与内容

## 2、存储格式如下：

### 每首古诗单独为一个文件，所有古诗存放在一个文件夹内

### 每首古诗文件内的古诗为，标题独自占一行，内容每遇到句号换行一次

### 如果古诗标题内存在/，需要去除这个/

```python
import requests
from bs4 import BeautifulSoup
import os
from user_headers import L
import random

class Gushi:
    def __init__(self):
        self.url="https://www.gushiwen.org/default_4.aspx"
        self.headers={"User-Agent":random.choice(L)}


    def get_soup(self):
        self.files="./古诗词"
        if not os.path.exists(self.files):
            os.mkdir(self.files)
        res=requests.get(self.url,headers=self.headers)
        res.encoding="utf-8"
        html=res.text
        soup=BeautifulSoup(html,"lxml")
        self.get_data(soup)

    def get_data(self,soup):
        title=soup.select('div > p > a > b') #通过css选择器查找标题内容
        comment=soup.find_all("div",class_="contson") #通过方法选择器查找内容信息
        self.save_data(title,comment) #调用保存信息的函数

    def save_data(self,title,comment):
        for i in range(len(title)): #获取标题和内容列表的索引
            name=title[i].text
            for j in name:
                if j=="/":
                    name=name.replace(j,"")
            filename=self.files+"//"+name
            data=comment[i].text
            with open(filename,"w",encoding="utf-8") as f:
                f.write(name)
                for i in data:
                    f.write(i)
                    if i =="。": #如果写入的字符为。,则添加一个换行符进去，进行换行的操作
                        f.write("\n")
                print("数据存储成功！")



gushi=Gushi()
gushi.get_soup()
```

# 4、json模块

## 用于python数据类型和json数据类型之间的相互转换

## json                                python

### 对象                                       字典

### 数组                                       列表

## 1、json.loads()

#### 用于将json--->python数据类型

```python
import json

json_data="""[{"name":"小明"},{"age":"20"},{"sex":"男"}]"""
print(json_data)
print(type(json_data))
# for i in json_data:
#     print(i)

data=json.loads(json_data) #将json-->python
print(data)
print(type(data))
for i in data:
    print(i)
```

## 2、json.dumps()

#### 用于将python--->json数据类型

```python
#json.dumps使用的默认编码是ASCII编码，ensure_ascii=False参数的作用就是不适用和这个编码格式
json_text=json.dumps(data,indent=2,ensure_ascii=False)
with open("data.json","w",encoding="utf-8") as f:
    f.write(json_text)
```

# 5、bilibili小视频

## 1、抓包 找到存放视频信息的真实请求

## 2、分析请求参数，找到可变的参数信息

## 3、构造参数字典，然后对url发起请求

## 4、发起请求后得到json数据，然后将json数据转换为python数据

## 5、解析数据，获取视频的下载地址

## 6、将视频下载到本地文件夹

```python
import requests
import json
import os
from user_headers import L
import random
import string

class Bilibili:
    def __init__(self):
        self.url="https://api.vc.bilibili.com/board/v1/ranking/top?"
        self.headers={"User-Agent":random.choice(L)}
        self.all_chars=string.whitespace+string.punctuation #设置一个变量绑定所有的空白字符以及特殊字符
        self.files="./B站视频"

    def get_json(self):  # 对网页发起请求并获取json信息的函数
        if not os.path.exists(self.files):
            os.mkdir(self.files)
        for i in range(1,82,10):
            params={
                "page_size":"10",
                "next_offset": str(i),
                "tag": "小视频",
                "type":"tag_general_week",
                "platform":"pc"
            }
            res=requests.get(self.url,headers=self.headers,params=params)
            res.encoding="utf-8"
            html=res.text
            json_data=json.loads(html)# 将获取的json数据转换为python数据类型
            self.get_video_url(json_data) #调用获取视频链接的函数

    def get_video_url(self,json_data): # 解析json数据获取视频下载链接的函数
        for i in json_data["data"]["items"]:
            video_url=i["item"]["video_playurl"] #获取视频的地址
            name=i["item"]["description"] #获取视频的名称
            if len(name) > 15:
                name=name[-15:]
            for j in name:
                if j in self.all_chars: #如果标题中存在特殊字符，就替换为空字符
                    name=name.replace(j,"")
            filename=self.files+"//"+name+".mp4"
            self.save_video(video_url,filename) #调用保存视频的函数


    def save_video(self,video_url,filename): # 保存视频到本地的函数
        res=requests.get(video_url,headers=self.headers)
        res.encoding="utf-8"
        html=res.content
        with open(filename,"wb") as f:
            f.write(html)
            print(filename,"下载成功！")


bili=Bilibili()
bili.get_json()
```

# 6、豆瓣电影排行

## 1、通过分析查找任意一个类型的电影榜单

## 2、找到存放电影信息的请求

## 3、获取所有的电影数据

#### 电影名称  演员信息 国家 上映时间 评分 排名 电影类型

## 4、将所有的数据存储到excel表格或者数据库

```python
import requests
from user_headers import L
import json
import csv
import random

class Douban:
    def __init__(self):
        self.url="https://movie.douban.com/j/chart/top_list?"
        self.headers={"User-Agent":random.choice(L)}

    def get_json_data(self):
        with open("movie.csv","w",encoding="utf-8",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(["电影名称","演员信息","国家","上映时间","评分","排名","电影类型"])
        for i in range(0,81,20):
            params={
                "type":"13",
                "interval_id":"100:90",
                "action":"",
                "start":str(i),
                "limit":"20"
            }
            res=requests.get(self.url,headers=self.headers,params=params)
            res.encoding="utf-8"
            html=res.text
            json_data=json.loads(html) #将源代码转换为json数据
            self.get_data(json_data) #调用获取信息的函数


    def get_data(self,json_data):
        for i in json_data:
            title=i["title"]  #获取电影名称
            actors=i["actors"] #获取演员信息   list
            actors=",".join(actors)
            regions=i["regions"] #获取国家信息  list
            regions=",".join(regions)
            release_date=i["release_date"] #获取上映时间
            score=i["score"] #获取评分信息
            rank=i["rank"] #获取排名信息
            types=i["types"] #获取类型信息   list
            types=",".join(types)
            content=[title,actors,regions,release_date,score,rank,types]
            self.save_data(content) #调用保存数据的函数

    def save_data(self,content):
        with open("movie.csv","a",encoding="utf-8",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(content)
            print("数据存储成功！")

douban=Douban()
douban.get_json_data()
```



# day04
day04

# 1、python链接mysql数据库

## 1、建立链接

```python
        conn=pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="123456",
            database="douban"
        )

```

## 2、创建游标对象

```python
cursor=conn.cursor() #创建游标对象
```

## 3、执行插入数据库操作

```python
sql_insert="""INSERT INTO movie_info(title,actors,regions,release_time,score,rank,types) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        cursor.executemany(sql_insert,t_list) #插入数据
        conn.commit() #关闭连接
```

```python
import requests
from user_headers import L
import json
import csv
import random
import pymysql

class Douban:
    def __init__(self):
        self.url="https://movie.douban.com/j/chart/top_list?"
        self.headers={"User-Agent":random.choice(L)}

    def get_json_data(self):
        with open("movie.csv","w",encoding="utf-8",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(["电影名称","演员信息","国家","上映时间","评分","排名","电影类型"])
        for i in range(0,81,20):
            params={
                "type":"13",
                "interval_id":"100:90",
                "action":"",
                "start":str(i),
                "limit":"20"
            }
            res=requests.get(self.url,headers=self.headers,params=params)
            res.encoding="utf-8"
            html=res.text
            json_data=json.loads(html) #将源代码转换为json数据
            self.get_data(json_data) #调用获取信息的函数


    def get_data(self,json_data):
        for i in json_data:
            title=i["title"]  #获取电影名称
            actors=i["actors"] #获取演员信息   list
            actors=",".join(actors)
            regions=i["regions"] #获取国家信息  list
            regions=",".join(regions)
            release_date=i["release_date"] #获取上映时间
            score=i["score"] #获取评分信息
            rank=i["rank"] #获取排名信息
            types=i["types"] #获取类型信息   list
            types=",".join(types)
            content=[title,actors,regions,release_date,score,rank,types]
            # self.save_data(content) #调用保存数据的函数
            self.save_mysql(content) #调用保存数据库的函数

    def save_data(self,content):
        with open("movie.csv","a",encoding="utf-8",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(content)
            print("数据存储成功！")

    def save_mysql(self,content): #将数据存储到数据库的函数
        t_content = tuple(content)
        t_list=[t_content]
        conn=pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="123456",
            database="douban"
        )
        cursor=conn.cursor() #创建游标对象
        sql_insert="""INSERT INTO movie_info(title,actors,regions,release_time,score,rank,types) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        cursor.executemany(sql_insert,t_list) #插入数据
        conn.commit() #关闭连接
        print("数据存储成功！")

douban=Douban()
douban.get_json_data()
```

## 2、有道翻译

```pyth
i: 橙子
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15755328116991  #不同
sign: 8426ffae4746b0c256debb05c2fe6360 #不同
ts: 1575532811699 #不同
bv: 6cf12640614e68ba598ee58ceccb0605
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_CLICKBUTTION
 
i: 苹果
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15755326946679
sign: b8bd75822a971700fe6d340ddff3d580
ts: 1575532694667
bv: 6cf12640614e68ba598ee58ceccb0605
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_CLICKBUTTION
```

#### r变量为获取当前时间节点的时间戳 ---> ts

#### i变量为 r+一个0~9之间的随机数 ----> salt

#### e变量为 输入需要翻译的单词

#### sign--> md5加密("fanyideskweb" +e+i+"n%A-rKaT5fb[Gy?;N5@Tj"")

```python
import requests
import json
from user_headers import L
import random
import time
from hashlib import md5
class Youdao:
  def __init__(self):
    self.url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    self.headers={"User-Agent":random.choice(L),
984118829@qq.com 姓名 学号
           "Cookie":"OUTFOX_SEARCH_USER_ID=-1431696184@10.169.0.83;
OUTFOX_SEARCH_USER_ID_NCOO=1943625779.162675; JSESSIONID=aaaUBWn5SCFytfQLoev7w;
___rl__test__cookies=1575535864354",
           "Referer":"http://fanyi.youdao.com/"}
  def get_json(self):
    word=input("请输入需要翻译的单词:")
    ts =str(int(time.time() * 10000))  # 获取时间戳
    salt = ts + str(random.randint(0, 9))  # 生成0~9之间的随机整数
    data = "fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
    s = md5()
    s.update(data.encode())
    sign = s.hexdigest()
    data={
      "i":word,
      "from":"AUTO",
      "to": "ko",
      "smartresult":"dict",
      "client":"fanyideskweb",
      "salt":salt,
      "sign":sign,
      "ts": ts,
      "bv":"6cf12640614e68ba598ee58ceccb0605",
      "doctype":"json",
      "version":"2.1",
      "keyfrom":"fanyi.web",
      "action":"FY_BY_CLICKBUTTION"
   }
    res=requests.post(self.url,headers=self.headers,data=data)
    res.encoding="utf-8"
    html=res.text
    json_data=json.loads(html)
    self.get_data(json_data)
  def get_data(self,json_data):
    data=json_data["translateResult"][0][0]["tgt"]
    print("翻译的结果为:",data)
youdao=Youdao()
youdao.get_json()
```

# day05
day05
# 1、词云项目

### 1、对获取的评论数据进行分词

```python
import jieba
def cut_info():
  with open("comment.txt","r",encoding="utf-8") as f:
    text=f.read()
    cut_text=" ".join(jieba.cut(text))
    with open("cut_text.txt","w",encoding="utf-8") as f:
      f.write(cut_text)
cut_info()
```

### 2、绘制词云

```python
#通过wordcloud模块传入词云相对应的参数
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
#将图片变为多维数组的模块，实现图片和文字的交互
from imageio import imread
#使用codecs打开文件，不需要考虑编码格式问题，默认都是用Unicode编码
import codecs
#绘制数学统计制图陌路爱，用它来显示和绘制词云
import matplotlib.pylab as plt
from os import path
class Darw_pic:
  def __init__(self):
    self.font_path="./font/simhei.ttf"  #设置字体路径
    self.image_path="timg.jpg" #设置图片路径
    self.cut_text="cut_text.txt" #设置文本路径
  def get_info(self):
    d=path.dirname(__file__) #获取当前文件的操作路径
    image=imread(self.image_path) #将图片处理为多维数组
    text=codecs.open(path.join(d,self.cut_text),"rb",encoding="utf-8").read() #读取文本
数据
    self.draw_wordcloud(image,text) #调用绘制词云的方法
  def draw_wordcloud(self,image,text):
    stopwords=set(STOPWORDS) #使用默认的屏蔽词
    # 字体路径 图片数组 屏蔽字 背景颜色 最大词数限制 字体最大限制 文本数据
    wordcloud=WordCloud(font_path=self.font_path,mask=image,
              stopwords=stopwords,background_color="white",
              max_words=2000,max_font_size=200).generate(text)
    image_color=ImageColorGenerator(image) #让字体颜色随着图片变色改变
    wordcloud.to_file("wordcloud.jpg") #给生成的词云命名
    plt.imshow(wordcloud.recolor(color_func=image_color)) #生成词云的颜色
    plt.axis("off") #不显示坐标轴
    plt.show() #显示词云
   
draw=Darw_pic()
draw.get_info()
```



![wordcloud](./day05/wordcloud.jpg)
