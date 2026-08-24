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
    unique_key=(details["name"],details["Class"],details["subject"])

    if unique_key not in seen_records:
        seen_records.append(unique_key)
        cleaned_data[student_id] = details
 
student_data = cleaned_data
 
print("")
print("After removing duplicate records:")
print(student_data)
 
# PART 6: Remove one student record using pop()
removed_student = student_data.pop("id4", "Student not found")
 
print("")
print("Removed student:")
print(removed_student)
 
# PART 7: Check the dictionary's length
print("")
print("Total student records left:", len(student_data))
 
# PART 8: Iterate through the dictionary
print("")
print("===== FINAL STUDENT SUBJECT RECORDS =====")
 
for student_id, details in student_data.items():
    print(student_id, ":", details)
 
print("==========================================")
