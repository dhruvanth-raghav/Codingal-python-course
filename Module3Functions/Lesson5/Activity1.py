import random 

# r=random.random()
# print(r)

# s=r*50
# print(s)

# n=int(s)
# print(n)

# n=random.randint(0, 50)
# print(n)

SecretNum=random.randint(1, 50)
attempts=1
print("===WELCOME TO THE NUMBER GUESSING GAME!===")
while attempts <= 5:
    guess=int(input("Enter your guess:"))
    if guess==SecretNum :
        print("YOU GUESSED THE SECRET NUMBER CORRECT!")
        break
    difference=abs(guess-SecretNum)
    if difference < 5:
        print("HOT🔥")
    elif difference < 10:
        print("WARM🌡️")
    elif difference < 15:
        print("COLD🥶")
    else:
        print("ICE COLD🧊")

    for i in range(5-attempts):
        print("💓")
    attempts+=1
if attempts==6:
    print("YOU LOST!..THE SECRET NUMBER IS:",SecretNum)