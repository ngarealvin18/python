height = float(input("Enter Your Height"))
weight = float(input("Enter Your Weight"))

BMI = weight/height*height

if BMI < 18.5:
    category = "Under weight"
elif 18.5 <= BMI < 25:
    category = "Normal Weight"
elif 25 <= BMI < 29.9:
    category = "overweight"
else:
    category = "obese"
print(category)