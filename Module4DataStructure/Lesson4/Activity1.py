list1=[1,2,3,3,4,4,5,5,5,6,7,7,8,10,10,10]
print(list1)
print(type(list1))

set1={1,2,3,3,4,4,5,5,5,6,7,7,8,10,10,10}
print(set1)
print(type(set1))

fruits={"apples","apples","oranges","oranges","oranges","watermelon","watermelon"}
print(fruits) 

fruits.add("kiwi")
print(fruits)

fruits.add("apples")
print(fruits)

basket={"apples","bananas","grapes"}
common_fruits=fruits.intersection(basket)
print(common_fruits)


all_fruits=fruits.union(basket)
print(all_fruits)

fruits_list=list(fruits)
print(fruits_list)


num_set=set(list1)
print(num_set)

#ARRAYS-this only allows us to store data of a single data type

import array as arr  #this is aslo called as a alias
fruits_counts=arr.array("i",[1,5,9,77,5])
print(fruits_counts)
print(type(fruits_counts))

# array cannot be used to create a collections of strings
fruits_counts.append(56)
print(fruits_counts)
fruits_counts.insert(2,8)
print(fruits_counts)

print(f"5 appears {fruits_counts.count(5)} times.")

fruits_counts.reverse()
print(fruits_counts)

point1=(0,0)
point2=(1,10)
point3=(0,0)
point4=(-5,-6)

point_set={point1,point2,point3,point4}
print(point_set)

s={ [1,2],[1,2] }# you cannot use list as a set element
print(s)