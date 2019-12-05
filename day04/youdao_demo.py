import time
import random
from hashlib import  md5

ts=int(time.time()*10000)#获取时间戳
salt=ts+random.randint(0,9)#生成0-9随机整数
data="fanyideskweb"+"橙子"+str(salt)+"n%A-rKaT5fb[Gy?;N5@Tj"
s=md5()
s.update(data.encode())
sign=s.hexdigest()
print(sign)