import os
os.system("cls")

class Employee:
    def __init__(self, n, p):
        self.name = n
        self.position = p

class Manager(Employee):
    def __init__(self, n, p, s):
        Employee.__init__(self, n, p)
        self.team_size = s
    
    def __str__(self):
        return f"Ismi: {self.name}\nPozitsiyasi: {self.position}\nJamoa hajmi: {self.team_size}\n"
    
job1 = Manager("Valiyev Ali", "Manager", 6)
print(job1)
job2 = Manager("Aliyev Vali", "Accountant", 5)
print(job2)
