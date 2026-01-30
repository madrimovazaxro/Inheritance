import os
os.system("cls")

# Animal nomli class yarating. Unda name atributi bo‘lsin.
#  Dog nomli class Animaldan meros olsin va o‘ziga xos sound atributi bo‘lsin 
#  ("Woof" qiymati bilan).
#  Obyekt yaratib, itning nomi va tovushini ekranga chiqaring.

class Animal:
    name = "Reks"
class Dog(Animal):
    sound = "Woof"
    def __str__(self):
        return f"{self.name} - {self.sound}"
    
a = Dog()
print(a)

