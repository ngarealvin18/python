class People:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display(self):
        print(f"My name is {self.name}"
              f" and i am {self.age} years old")
obj=People("Alvin", 19)
obj.display()

obj1=People("Sharon", 18)
obj1.display()

obj2=People("Mike", 19)
obj2.display()

obj3=People("Anabel", 18)
obj3.display()

obj4=People("Ian", 19)
obj4.display()

obj5=People("Mitchell", 18)
obj5.display()
