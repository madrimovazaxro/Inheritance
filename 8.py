# Vehicle classida brand va speed atributlari bo‘lsin.
#  Bike classi Vehicle’dan meros olsin va o‘ziga xos type (например: "mountain") 
# atributi bo‘lsin.
#  Bir nechta Bike obyektini ro‘yxatda saqlang va hammasining 3ta ma’lumotini chiqaring.

import os
os.system("cls")

class Vehicle:
    def __init__(self, b, s):
        self.brand = b
        self.speed = s

class Bike(Vehicle):
    def __init__(self, b, s, t):
        Vehicle.__init__(self, b, s)
        self.type = t
    def __str__(self):
        return f"Brendi: {self.brand}\nTezligi: {self.speed}\nTuri: {self.type}\n"
    
bike1 = Bike("Trek", 30, "road")
print(bike1)
bike2 = Bike("Specialized", 35, "road")
print(bike2)
bike3 = Bike("Giant", 20, "mountain")
print(bike3)


