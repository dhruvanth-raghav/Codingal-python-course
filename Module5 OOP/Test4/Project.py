#Write a program to create a quiz related to multiple fruits using object-oriented programming in Python. Create a class that consists of -1. a constructor with a dictionary of fruits and respective colours2. a function to execute the quiz. Here, the fruit will be chosen at random from the dictionary. Then ask the user to enter the colour of that fruit. Evaluate the answer and display the result accordingly.

import random

class Fruit_Quiz:
    def __init__(self):
        self.fruits = {
            "apple": "red",
            "banana": "yellow",
            "mango": "yellow",
            "orange": "orange",
            "lychee": "pink",
            "fig":"purple"
        }

    def quiz(self):
        fruit=random.choice(list(self.fruits.keys()))

        colour= input(f"What is the colour of this {fruit}?")

        if colour.lower()==self.fruits[fruit]:
            print("Correct colour✅")
        else:
            print(f"Wrong ❌..the colour is {self.fruits[fruit]}")

quiz=Fruit_Quiz()
quiz.quiz()
