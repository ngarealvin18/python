class Fruits:
    def __init__(self, name, price, colour):
        self.name=name
        self.price=price
        self.colour=colour
    def onyesha(self):
        print(f"My favourite Fruit is {self.name}"
              f", it costs Ksh.{self.price}"
              f" and its {self.colour} in colour.")
myobj = Fruits ("Orange", 50, "orange")
myobj1 = Fruits("Apple", 30, "green")
myobj.onyesha()
myobj1.onyesha()
