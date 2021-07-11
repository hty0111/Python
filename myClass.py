class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tall = 165     #设置默认值
    def sit(self):
        print(self.name.title() + ' is sitting.')
    
my_dog = Dog('zxa', 20)
print('My dog ' + my_dog.name + ' is ' + str(my_dog.age) + ' years old.')
my_dog.sit()

class Car():
    def __init__(self, name, wheel, color) -> None:
        self.name = name
        self.wheel = wheel
        self.color = color
        self.meter = 0
    
    def update_meter(self, meter):
        if self.meter > meter:
            print("Cannot go back.")
        else:
            self.meter = meter
    
    def get_info(self):
        print(self.name, self.wheel, self.color, self.meter)

my_car = Car('horse', 4, 'yellow')
my_car.get_info()
my_car.meter = 40       #直接赋值
my_car.get_info()
my_car.update_meter(20) #调用函数赋值
my_car.get_info()

class Battery():
    def __init__(self, battery_size=70) -> None:
        self.battery_size = battery_size
    def print_info(self):
        print('The car has ' + str(self.battery_size) + ' battery size.')

class ElectricCar(Car):
    """电动车的独特之处"""
    def __init__(self, name, wheel, color) -> None:
        super().__init__(name, wheel, color)
        self.battery = Battery()       #实例化
        
    def update_meter(self):     #覆盖
        print('Updated successfully.')

your_car = ElectricCar('bike', 2, 'black')
your_car.battery.print_info()