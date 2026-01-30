import os 
os.system("cls")

#  Transport classida model va year atributlarini yarating.
#  Car classi transportdan meros olsin. Car uchun color atributi qo‘shing.
#  Mashina obyektidan model, yil va rangni chiqarib bering.

class Transport:
    def __init__(self, m, y):
        self.model = m
        self.year = y

class Car(Transport):
    def __init__(self, m, y, c):
        Transport.__init__(self,m,y)
        self.color = c
    def __str__(self):
        return f"Model: {self.model}\nYili: {self.year}\nRangi: {self.color}\n"

c1 = Car("Malibu", 2020, "Qora")
c2 = Car("Sparl", 2016, "Oq")
c3 = Car("Gentra", 2021, "Qora")
print(c1)
print(c2)
print(c3)