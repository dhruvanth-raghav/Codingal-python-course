details=(12,"Dhruvanth R,",9,"Nile","Drums",54.5)
print(details)
print(len(details))
print(type(details))
print("First element:",details[0])
print("Last element:",details[-1])

print(details[:4])

t1=(2,3,4,10,11,10,5,5,5,5,8)
print("No.of occurrence of 5:",t1.count(5))

#You cannot change or modify the original tuple values
#Tuples are immutable(cannot change)....But lists are mutable
names_list=["Alice", "Bharat", "Charlie"]
names_list[0]="Dhruvanth"
print(names_list)

names_tuple=("Alice","Bharat","Charlie")
# names_tuple[0]="Dhruvanth"

another_tuple=names_tuple +("Dhruvanth",)
print(another_tuple)

