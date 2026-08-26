snack_box1 = {"chips", "drinks", "chocolate", "chips", "gummys"}
snack_box2 = {"chocolate", "sandwich", "jelly", "sandwich"}
print("Items available in snack box1:", snack_box1)
print("Items available in snack box2:", snack_box2)

snack_box1.add("fries")
print("Snack Box 1 after adding fries:", snack_box1)

common_snacks = snack_box1.intersection(snack_box2)
print("Snacks common in both boxes:", common_snacks)

import array as arr
snack_counts = arr.array('i', [4, 6, 3, 5])
print("Array:", snack_counts)

snack_counts.insert(0, 2)
snack_counts.append(7)
print("Snack counts after adding items:", snack_counts)

count_of_5 = snack_counts.count(5)
print("Number of times 5 appears:", count_of_5)

snack_counts.reverse()
print("Array Reversed:", snack_counts)

print()
print("===== SCHOOL SNACK COUNTER =====")
print("Snack Box 1:", snack_box1)
print("Snack Box 2:", snack_box2)
print("Shared snacks:", common_snacks)
print("Snack counts:", snack_counts)

