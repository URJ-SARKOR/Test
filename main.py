# class Animal:
#     def make_sound(self,s):
#         print(s)
#
# class Horse(Animal):
#     def dibi(self):
#         print('Встала на дыбы')
#
#
# mustang = Horse()
# mustang.make_sound('Igogo')
# mustang.dibi()



# class parents:
#     def give_mooney(self, p):
#         print(p)
#
# class child(parents):
#     def learn(self):
#         print('Начал учиться')
#
# child1 =child()
# child1.give_mooney('aaa')
# child1.learn()


# class Car:
#     def __init__(self,model,color,year):
#         self.model = model
#         self.color = color
#         self.year = year
# class SuperCar(Car):
#     def __init__(self,model,color,year,sponsor):
#         super.__init__(model,color,year)
#         self.sponsor = sponsor
#
# gentra = Car(model='Chevrolet',color='black',year=2022)
# amgone = SuperCar(model='Mercedez-Benz' , color='Silver',year=2022,sponsor='Petronas')
# print(amgone.sponsor)



# class Animal:
#     @classmethod
#     def make_sound(cls,s):
#         print(s)
#
# Animal.make_sound('frrrrrrr')









# class MyClass:
#     def __init__(self, value):
#         self.value=value
#
#     @classmethod
#     def from_string(cls,string):
#         return cls(int(string))
#
# my_obj = MyClass.from_string("10")
# print(my_obj.value)



# class Rectangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     @property
#     def area(self):
#         return self.width*self.height
# rectangle=Rectangle(4,5)
# print(rectangle.area)
#
# rectangle.width=6
# print(rectangle.area)
# rectangle.height= 50
# print(rectangle.area)



# class worker:
#     def __init__(self,name,position):
#         self.name = name
#         self.position = position
#
#     def work(self):
#         print('Работает')
#
# class HR(worker):
#     def __init__(self,name,position):
#        super().__init__(name,position)
#
#     def show_info(self,name):
#         return worker.pos
# jordan = worker('Jordan', 'Junior')
# pavel = HR('Pavel', 'HR')
#
# jordan.work()
# pavel.show_info()





# class Player:
#     def __init__(self, speed,power,accuracy,stamina):
#         self.speed = speed
#         self.power = power
#         self.accuracy = accuracy
#         self.stamina = stamina
# class Napadayushiy(Player):
#     def __init__(self,speed,power,accuracy,stamina):
#         super().__init__(speed,power,accuracy,stamina)
#     def goal(self):
#         print('Забил гол')
# class Goalkeeper(Player):
#     def __init__(self:

