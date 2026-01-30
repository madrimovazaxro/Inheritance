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
class Laptop(Product):
    def __init__(self, t, p, m):
        Product.__init__(self, t, p)
        self.cpu_model = m

    def __str__(self):
        return f"'{self.title}', {self.price}, '{self.cpu_model}'"

laptops = [
    Laptop("MacBook Pro", 2200, "M2"),
    Laptop("HP Spectre", 1800, "Intel i7"),
    Laptop("Lenovo", 1700, "Intel i5")
]

eng_qimmat = max(laptops, key=lambda laptop: laptop.price)

print(f"{eng_qimmat.title}")
print(f"Narxi: {eng_qimmat.price}")
print(f"cpu_modeli: {eng_qimmat.cpu_model}")