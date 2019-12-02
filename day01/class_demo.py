class Car(object):
    """"
        此类是一个汽车类
    """
    def get_speed(self,speed):
        """
        此实例方法是给对象添加速度的属性
        """
        self.car_speed=speed

    def get_brand(self,brand):
        """
        此实例方法是给汽车添加品牌的方法
        """
        self.car_brand=brand
        print(self.color,"的",self.car_brand, "正在以", self.car_speed, "的速度行驶！")
car=Car()   # 类的实例化
# print(id(car))
car.color="黑色"#给对象添加上颜色的属性
car1=Car()
car.get_speed(200)
car.get_brand("奔驰")
#print(id(car1))
car1.color="红色"
car1.get_speed(150)
car1.get_brand("大众")


