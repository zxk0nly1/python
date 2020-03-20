### mysql与sqlite操作

![image-20200320155056875](upload%5Cimage-20200320155056875.png)

文件结构及内容

***do_sqlite.py***

```python
# -*- coding:utf-8 -*-
import os,sqlite3

db_file=os.path.join(os.path.dirname(__file__),'sqlite_test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

#初始化数据
    conn=sqlite3.connect(db_file)    
    cursor=conn.cursor()
    cursor.execute('create table user (id varchar(20) primary key , name varchar(20), score int)')
    cursor.execute(r"insert into user values ('A-001','Adam',95)")
    cursor.execute(r"insert into user values ('A-002','Bart',62)")
    cursor.execute(r"insert into user values ('A-003','Lisa',78)")
    cursor.close()
    conn.commit()
    conn.close()

def get_score_in(low,high):
    '''返回指定分数区间的名字，按分数从低到高排序''' 
    try:
        conn=sqlite3.connect(db_file)
        cursor=conn.cursor()
        cursor.execute('select name from user where score between ? and ? order by score',(low,high))
        values=cursor.fetchall()
        result=[]
        for i in values:
            result.append(i[0])
        return result
    except BaseException as e:
        print('Conn Error!',e)
    finally:
        cursor.close()
        conn.close()

# 测试
assert get_score_in(80,95)==['Adam'],get_score_in(80,95)
assert get_score_in(60,80)==['Bart','Lisa'],get_score_in(60,80)
assert get_score_in(60,100)==['Bart','Lisa','Adam'],get_score_in(60,100)

print('Pass')
```

***sqlite.py***

```python
# -*- coding: utf-8 -*-

import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# 通过rowcount获得插入的行数:
print('rowcount =', cursor.rowcount)
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()

# 查询记录：
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句:
cursor.execute('select * from user where id=?', '1')
# 获得查询结果集:
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
```

***do_mysql.py***

```python
# -*- coding: utf-8 -*-

import mysql.connector

# change root password to yours:
conn = mysql.connector.connect(user='root', password='password', database='test')

cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Russell'))
print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()
```

![image-20200320161228032](upload%5Cimage-20200320161228032.png)