# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is leep year.')
        else:
            print(f'{year} is not leap year.')
    else:
        print(f'{year} is leap year.')
else:
    print(f'{year} is not leap year.')
