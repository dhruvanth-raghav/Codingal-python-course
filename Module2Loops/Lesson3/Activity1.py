chores=["Make your bed", "clean room","buy groceries"]
original_count=len(chores)
print(f"You have {original_count}  number of chores to do today")
completed_count=0
while len(chores)>0:
    next_chore=chores[0]
    reply=input(f"Have you finished {next_chore}?(Yes/No): ").lower()
    if reply== "yes" :
        chores.pop(0)
        completed_count +=1
        print("Great job, Chores completed till now:",completed_count)
    else:
        print("TRY AGAIN")

    print("Remaining chores:",len(chores))
    print()


print("*****CHORE CHECKLIST SUMMARY*****")
print("Chores assigned today:",original_count)
print("Chores completed:", completed_count)
print("Chores remaining:",(original_count-completed_count))