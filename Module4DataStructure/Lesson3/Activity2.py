#To find the frequency of given "value"

frequency={
    "Bread":5,
    "Jam":5,
    "Chocolate":4,
    "cookies":4
}

k=int(input("Enter a frequency:"))

count=0
for key, value in frequency.items():
    if k ==value:
        count +=1

print(f"The value {k} appeared {count} no.of times")
