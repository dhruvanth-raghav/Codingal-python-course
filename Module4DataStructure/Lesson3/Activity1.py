#TO REMOVE THE DUPLICATED "VALUES" IN A DICTIONARY

d={"A":1,
"B":1,
"C":1,
"D":2
}

result={}
seen_values=[]

for key, value in d.items():
    #we will not add key, if value has already been stored in the "result"
    if value not in seen_values:
        seen_values.append(value)
        result[key]=value


print(result)