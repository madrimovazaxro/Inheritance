import os
os.system("cls")

#  Product classida title va price bo‘lsin.
#  Laptop classi Product’dan meros olsin va cpu_model atributi bo‘lsin.
#  Laptop obyektlarini ro‘yxatda saqlang va ularning narxidan 
# eng qimmatini topib chiqarib bering.

class Product:
    def __init__(self, t, p):
        self.title = t
        self.price = p
        self.laptops = []
class Laptop(Product):
    def __init__(self, t, p, m):
        Product.__init__(self, t, p)
        self.cpu_model = m


    def __str__(self):
        return f"{self.title} {self.price} {self.cpu_model}"

l1 = Laptop("Apple MacBook Air 13", 1150, "Apple M4")

l2 = Laptop("ASUS Zenbook S 14 OLED", 1420, "Intel Core Ultra 7")

l3 = Laptop("Dell Inspiron 14 Plus", 1100, "Intel Core i7")
