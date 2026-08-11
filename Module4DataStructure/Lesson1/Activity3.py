runs=[100,89,0,67,90,33,10]
# finding batting avg
sum=0
for i in runs:
    sum +=i
print("Total no.of runs:",sum)
avg=sum/len(runs)
print("Batting avg=",avg)

#find the Minimum & Maximum Score
runs.sort()
print(runs)

print("Min Score:",runs[0])
print("Max Score:", runs[-1])

print(len(runs))
print(runs[len(runs)-1])