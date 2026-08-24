GradeBook={
    "Dhruvanth": 97,
    "Abishek": 98,
    "Sanaathani":72,
    "Jack": 56,
    "Jill":67
}

total=0
for marks in  GradeBook.values():
    total+=marks

avg=total/len(GradeBook)
student_names=" , ".join(GradeBook.keys())
print(f"The average of {student_names} is equal to:",avg)

user_input=input("Enter the name of the student:")
searchResult=GradeBook.get(user_input,"...Name not found!")
print("Searching for the requested name:",searchResult)


#This is to find the maximum and minimum scores,(not the key)
# TopScorer= max(GradeBook.values())
# BottomScorer=min(GradeBook.values())
# print(TopScorer,BottomScorer)

TopScorer= max(GradeBook,key=GradeBook.get)
BottomScorer=min(GradeBook,key=GradeBook.get)
print("The top scorer is:",TopScorer)
print("The lowest scorer is:",BottomScorer)
#How do I use a for loop to find the top scorer and bottom scorer