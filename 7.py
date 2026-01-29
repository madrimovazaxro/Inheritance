import os
os.system("cls")



#  Worker classida full_name va salary atributlari bo‘lsin.
#  Programmer classi Worker’dan meros olsin va language atributi qo‘shilsin.
#  Bir nechta programmer obyektlari yarating va ularning ma’lumotlarini ketma-ket 
# chiqarib bering.

class Worker:
    def __init__(self, n, s):
        self.full_name = n
        self.salary = s

    
class Programmer(Worker):
    def __init__(self, n, s, l):
        Worker.__init__(self, n, s)
        self.language = l

    def __str__(self):
        return f"Ism: {self.full_name}\nOylik: {self.salary}\nTil: {self.language}"


programmer1 = Programmer("Madrimova Zaxro", 100, 'Python')
print(programmer1)
print()
programmer2 = Programmer("Valiyev Ali", 200, 'Java')
print(programmer2)
print()
programmer3 = Programmer("Aliyev Vali", 300, 'C++')
print(programmer3)