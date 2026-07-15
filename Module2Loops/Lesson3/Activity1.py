# 1) Ask the user to enter a number and store it in `n`.
n=int(input("Enter a number:"))
# 2) Set `sum` to 0.
sum=0
# (This will store the running total.)
i=1
while i<=n:
    sum=sum+i
    i=i+1
    
print(sum)