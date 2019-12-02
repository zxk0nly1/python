class Car(object):
    def __init__(self,color,brand):
        self.color=color
        self.brand=brand

    def get_speed(self,speed):
        self.speed=speed
        print(self.color,"的",self.brand,"汽车正在以",self.speed,"的速度行驶！")

car=Car("黑色","奔驰")
car.get_speed(120)
car1=Car("红色","奥迪")
car1.get_speed(200)