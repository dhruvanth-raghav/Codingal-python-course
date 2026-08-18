student_data={
    "id1":{"name":"Dhruvanth","Class":"9th","subject":"Physics,Chemistrt,Biology"},
    "id2":{"name":"Billy","Class":"7th","subject":"Music,Math"},
    "id3":{"name":"Aarav","Class":"11th","subject":"Art,Buisness"},
    "id4":{"name":"Sanaathani","Class":"7th","subject":"History,Hindi,Drama"}
}
print("===ORIGINAL  RECORDS===")
print(student_data)
print()

print("DETAILS OF ID1:")
print(student_data.get("id1","not found"))
print()

print("DETAILS OF ID5:")
print(student_data.get("id5","not found"))
print()

student_data["id5"]={"name":"Bharat","Class":"5th","subject":"History,Hindi"}
print()
print("==AFTER ADDING ID5==")
print(student_data)

student_data["id2"]["subject"]="Music,math,coding"
print()
print("AFTER UPDATING ID2 SUBJECTS:")
print(student_data["id2"])

cleaned_data={}
seen_records=[]

for student_id, details in student_data.items():
    unique_key=(details["name"],details["class"],details["subject"])