# class Cat:
#     def sound(self):
#         print("Meow")

# class Dog:
#     def sound(self):
#         print("Woof")

# animals = [Cat(), Dog()]
# for animal in animals:
#     animal.sound()

# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print(self.name, "says Woof!")

# rex = Dog("Rex")
# rex.bark()
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())