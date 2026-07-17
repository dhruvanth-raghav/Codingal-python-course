num=int(input("Enter a number: "))
power=int(input("Enter a : "))
ans=1
ans*=num
for i in range(power):
    ans*=num
print("Answer=",ans)