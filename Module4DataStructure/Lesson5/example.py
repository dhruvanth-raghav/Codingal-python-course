items=["Pencil","Eraser","Protractor"]
#Find all the items that start with the character "P", and store it in a new list 'p-items'
# p_items=[]

# for element in items:
#     if element[0]=="P":
#         p_items.append(element)


#LIST COMPREHENSION
p_items=[element#This is what will be added to the list
         
for element in items #the loop
if element[0]=="P"]



p_items=[element for element in items if element[0]=="P"]
print(p_items)