# 🚨 Don't change the code below 👇
weight_of_user = float(input("What's is your weight? "))
height_of_user = float(input("What's is your height? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi_of_user = round(weight_of_user/(height_of_user ** 2))
if bmi_of_user < 18.5:
    print(f'Your BMI is {bmi_of_user}, you are underweight')
elif bmi_of_user >= 18.5 and bmi_of_user < 25:
    print(f'Your BMI is {bmi_of_user}, you have a normal weight.')
elif bmi_of_user >= 25 and bmi_of_user < 30:
    print(f'Your BMI is {bmi_of_user}, you are slightly overweight.')
elif bmi_of_user >= 30 and bmi_of_user < 35:
    print(f'Your BMI is {bmi_of_user},  you are obese.')
elif bmi_of_user >= 35 and bmi_of_user < 50:
    print(f'Your BMI is {bmi_of_user}, you are clinically obese.')
else:
    print(f'Your BMI is {bmi_of_user} exaged, joker')
