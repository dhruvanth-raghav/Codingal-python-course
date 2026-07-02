# M1 L6 A1&2

# 1) Store values in `a`, `b`, and `c`.
a=12
b=56
c=10
# 2) Check an AND condition using `a and b and c`:
if a and b and c:
    print("All values evalute to TRUE")
else:
    print("Atleast one is 0")
# - This becomes True only if all three values are treated as True.

# - If the condition is True, print the “all true” message.

# - Otherwise, print the “at least one false” message.

# 3) Re-assign (change) new values to `a`, `b`, and `c` for the next checks.
a=-34
b=8
c=0
# 4) Check an OR condition: `a > 0 or b > 0`
if a>0 or b>0:
    print("Either is greater than 0")
else:
    print("no number is greater than 0")

# - If at least one of them is greater than 0, print the “either is greater than 0” message.

# - Otherwise, print the “no number is greater than 0” message.

# 5) Check another OR condition: `b > 0 or c > 0`

# - If at least one of them is greater than 0, print the “either is greater than 0” message.

# - Otherwise, print the “no number is greater than 0” message.
a=5
b=6
if not (a==b):
    print(" a and b are diff")

is_adult=False
if not is_adult:
    print("Cannot drive")
else:
    print("Can drive")