class Animal(object):
    def __init__(self,name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print (self.health)
        return self


class Dog(Animal):
    def __init__(self,name):
        super(dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self


class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(name)
        
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print ("I am a Dragon")
        return self

animal = Animal("animal")
animal.walk().walk().walk().run().run().displayHealth()

animal = Animal("animal")
animal.walk().walk().walk().run().run().displayHealth()

dra = Dragon("dragon")
dra.displayHealth()






class Animal(object):
    def __init__(self, name):
        self.health = 100
        self.name = name
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print "My name is: " + self.name
        print "I have: " + str(self.health) + ' Health'

animal = Animal("Ragnar")
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__ (self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

dog = Dog("Nilla")
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self
    
    def displayHealth(self):
        print "This is a dragon"
        super(Dragon, self).displayHealth()

dragon = Dragon('Fafnir')
dragon.fly().displayHealth()



class Animal(object):
    # Attributes
    def __init__(self,name):
        self.name = name
        self.health = 100
    # Methods
    def walk(self):
        self.health -= 1
        print("+1xp")
        return self
    def run(self):
        self.health -= 5
        print("-5xp")
        return self
    def displayHealth(self):
        print(str(self.name) +' now has '+ str(self.health) +' xp')

animal = Animal("Big Animal")
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    # Attributes
    def __init__(self,name):
        super(Dog,self).__init__(name)
        self.health = 150
    # Methods
    def pet(self):
        self.health += 5
        print("+5xp")
        return self
    
dog = Dog("Small Dog")
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    # Attributes
    def __init__(self,name):
        super(Dragon,self).__init__(name)
        self.health = 170
    # Methods
    def fly(self):
        self.health -= 10
        print("-10xp")
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print("I am a Dragon!!!")

dragon = Dragon("Huge Rarrr")
dragon.displayHealth()

class Cat(Animal):
    # Attributes
    def __init__(self,name):
        super(Cat,self).__init__(name)
        self.health = 999
    # Methods
    def catch(self):
        self.health -= 10
        print("-10xp")
        return self

cat = Cat("Meow")
cat.pet().fly().displayHealth()