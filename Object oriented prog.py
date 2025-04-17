# creating class superhero
class superhero: 
    def __init__(self, name, power, age):
        self.name = name 
        self.power = power
        self.age = age
   
        # creating a method of the class superhero
        # this method is used to introduce the superhero
    def introduce(self): 
        print(f"I am {self.name}, My age is {self.age}")
    
    def speed(self):
        print(f"I can reach speeds of {self.power}")
    
        # creating a subclass of superhero
        # this subclass is called batman
        # this subclass has an additional attribute called networth
class batman (superhero):
    def __init__(self, name, networth, age):
        super().__init__(name, "Super rich", age)
        self.networth = networth

    def introduce(self):
        print(f"I am {self.name}, My age is {self.age}")
    
    def rich(self):
        self.networth += 1000000000
        print(f"My networth is {self.networth}")


        # creating an object of the class superhero
        # this object is called hero
        # this object has the attributes name, power and age
hero = superhero("Lightening Mcqueen", 250, 15)
hero.introduce()
hero.speed()

bat= batman("Bruce Wayne", 5000, 35)
bat.introduce()
bat.rich()





