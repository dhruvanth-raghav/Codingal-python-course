import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
characters = lower + upper + num
password = ""

for i in range(10):
    password = password + random.choice(characters)
print("here is your password!:",password)