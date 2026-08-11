numbers=[1,2,3,4,5]
print(numbers)
print(len(numbers))

names=["Alice","Bob","charlie"]
print(names)
print(len(names))

empty=[]
print(len(empty))

#NOTE:LISTS USUALLY CONTAIN HOMOGENEOUS DATA - (SAME DATA TYPE)
print(names[1])
print(numbers[3:5])

reverse=numbers[::-1]
print(reverse)

triples = names*3
print(triples)
print(len(triples))