class Person:
    """Simple class."""

    name = "Shodmon"
    surname = "Ravsh"
    age = 18


person = Person()
print(person.name)
print(person.age)

person.age = 27
print(person.age)

person.surname = "Ravshanov"
print(person.age)


class Person:
    """Simple example of the method."""

    name = "Shodmon"
    surname = "Ravshanov"
    age = 27

    def hello(self):
        return f"Hi, I'm {name}"


person = Person()
print(person.hello())


class Car:
    """Class with init."""

    def __init__(self, model, color, wheels):
        self.model = model
        self.color = color
        self.wheels = wheels


tesla = Car(model="Tesla", color="Black", wheels=4)
print(tesla.model)

mercedes = Car(model="Mercedes-benz", color="White", wheels=4)
print(tesla.model, tesla.color)


# make Person class with init
# create several persons with person class (yourself, your frirend)
# add them to the list
# print the list


print(tesla)
print([tesla, mercedes])


class Car:
    """Using of the str and repr."""

    def __init__(self, model, color, wheels):
        self.model = model
        self.color = color
        self.wheels = wheels

    def __str__(self):
        return f"Car{self.model, self.color, self.wheels} - str"

    def __repr__(self):
        return f"Car{self.model, self.color, self.wheels} - repr" # self.__str__()


tesla = Car(model="Tesla", color="Black", wheels=4)
mercedes = Car(model="Mercedes-benz", color="White", wheels=4)
print(tesla)
print(str(tesla))
print([tesla, mercedes])


# extend Person class with repr and str
# print them


class Cat:
    """Example of the custom method"""

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name} {self.__class__}"

    def say(self):
        return "Meow"


cat = Cat("Liza")
print(cat)
print(cat.say())


# extend Person class add method which returns legal age status


class Animal:
    """Example of the inheritance and polumorphism."""

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def voice(self):
        raise NotImplementedError   # new stuff explain


class Cat(Animal):

    def voice(self):
        return "Meow"


class Dog(Animal):

    def voice(self):
        return "Bark"


cat = Cat("Liza")
cat_another = Cat("Mura")
dog = Dog("Sharik")

print(f"{cat} голос! {cat.voice()}")
print(f"{cat_another} голос! {cat_another.voice()}")
print(f"{dog} голос! {dog.voice()}")


# Example of what to add to the class
def formated_text(name, voice):
    return f"{name} голос! {voice}"

print(formated_text(cat, cat.voice()))
print(formated_text(cat_another, cat_another.voice()))
print(formated_text(dog, dog.voice()))


# add another animal
# extend Person with base class Human


class Animal:
    """Example of the inheritance and polumorphism."""

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def voice(self):
        raise NotImplementedError

    def give_a_voice(self):
        return f"{self.name} голос! {self.voice()}"


class Cat(Animal):

    def voice(self):
        return "Meow"


class Dog(Animal):

    def voice(self):
        return "Bark"


cat = Cat("Liza")
cat_another = Cat("Mura")
dog = Dog("Sharik")

animals = [cat, cat_another, dog]

for animal in animals:
    print(animal.formated_text())



# add to the human class method say_hello
# implement that method in subclasses
