# M1 L6 A3

# 1) Ask the user to enter their height in centimeters and store it in `height`.
height=float(input("Enter your height in cm:"))
# 2) Ask the user to enter their weight in kilograms and store it in `weight`.
weight=float(input("Enter your weight in kg:"))
# 3) Calculate BMI using the formula:

# BMI = weight ÷ (height in meters)²
bmi= weight/(height/100)**2
# (Convert height from cm to meters by dividing by 100.)

# Store the result in `BMI`.

# 4) Print the BMI value.
print("your BMI=", bmi)
# 5) Use if–elif–else to decide the BMI category:

# - If BMI is 18.4 or less → print "underweight"
if bmi<=18.4:
    print("you are underweight")
# - Else if BMI is 24.9 or less → print "healthy"
elif bmi<=24.9:
    print("You are healthy")
# - Else if BMI is 29.9 or less → print "over weight"
elif bmi<=29.9:
    print("over weight")
# - Else if BMI is 34.9 or less → print "severely over weight"
elif bmi<=34.9:
    print("you are severly over weight")
# - Else if BMI is 39.9 or less → print "obese"
elif bmi<=39.9:
    print("Obese")
# - Else → print "severely obese"
else:
    print("Severly obese")