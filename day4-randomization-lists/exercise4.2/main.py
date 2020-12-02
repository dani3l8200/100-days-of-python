import random
# Split string method
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
random_pay = random.randint(0, len(names) - 1)
print(f'{names[random_pay]} is going to buy the meal today!')
