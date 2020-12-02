# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
rest_age = 90 - int(age)
rest_days = rest_age*365
rest_week = rest_age*52
rest_month = rest_age*12
output = f'You have {rest_days} days, {rest_week} weeks and {rest_month} months left'
print(output)
