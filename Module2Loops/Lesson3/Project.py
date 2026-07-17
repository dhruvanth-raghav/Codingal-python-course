#FOR THE PET TASK MANAGER, GIVE AN OPTION TO THE USER TO ADD TASKS TO THE LIST
print("======🐶PET CARE TASK MANAGER🐈======")
print()
print("🐱WELCOME TO PET TASK CARE MANAGER🐶")
print()
PetTasks=["Here you go👉 " "Feed the pet","Refill the water bowl","Clean the pet's area","Take the pet for a walk"]
print()
choice=input("Do you want to enter your own pet tasks?(yes/no) :").lower()
while choice=="yes":
    NewTask=input("Enter the task:")
    print()
    PetTasks.append(NewTask)#"append"adds the given value to a specific list
    print()
    choice=input("Do you want to add another task?(yes/no):").lower()

oroginal_count=len(PetTasks)
completed_count=0
print()
print("✔️Your Pet Care Tasks✔️ :")
print(PetTasks)
print()
while len(PetTasks)>0:
    print()
    print("Current task:",PetTasks[0])
    ans=input("DId you complete this task?(yes/no):").lower()
    if ans=="yes":
         PetTasks.pop(0)
         completed_count +=1
         print("Task completed✔️,Good Job🥳")
    else:
        print("Complete it first before moving on")
        print("Tasks remaining:",len(PetTasks))
    count=0    
while True:
    #infinite loop
    print("Infinite loop example♾️🔽 ")
    
    count+=1
    if count==3:
        print("Loop stopped safely🛟")
        break#stops/ends the conditions
    print()
    print("====FINAL SUMMARY🔽====")
    print("Original task:",oroginal_count)
    print("Completed tasks:",completed_count)
    print("Remaining tasks:",len(PetTasks))


     
    