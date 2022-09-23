
class Animal:
    """Example of the inheritance and polumorphism."""

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def voice(self):
        raise NotImplementedError   # new stuff explain

animal = Animal(
    'name'
)
print(animal.voice())
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

