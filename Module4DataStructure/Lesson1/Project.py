#["apples......"]
#create a list of fruits
#take input from the user for a specific fruit
#and print how many times does the fruit appear in the list
#if it does not appear, print "could not find the specific fruit"
#BONUS:Can you create a function out of this process?
#eg, search(list,target)
#l=["apples","bananas"]
#"apples"
#search(l,t)

fruits=["apples","bananas","apples","grapes","apples"]
fruit=input("Enter a fruit:")
def search (list,target):
    count=0

    for fruit in list:
        if fruit == target:
            count +=1

    if count>0:
        print(f"the fruit -{target}, appeared {count} times")
    else:
        print("Could not find the specific fruit")

search(fruits,fruit)    
