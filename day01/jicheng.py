"""
类的继承和派生
"""
class Father(object):
    def say(self,what):
        print("正在说:",what)

    def walk(self,distance):
        print("行走了",distance,"米")


class Son(Father):
    def study(self,subject):
        print("正在学",subject)

son=Son()# 子类实例化对象
son.say("你好")
son.walk(1000)
father=Father()
son.study("python")