# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bill = 0.0
if size == "S":
    bill += 15.0

    if add_pepperoni == "Y":
        bill += 2

        if extra_cheese == "Y":
            bill += 1
        elif extra_cheese == "N":
            pass

    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill += 1
        elif extra_cheese == "N":
            pass

elif size == "M":
    bill += 20.0

    if add_pepperoni == "Y":
        bill += 3
        if extra_cheese == "Y":
            bill += 1
        elif extra_cheese == "N":
            pass

    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill += 1
        elif extra_cheese == "N":
            pass

elif size == "L":
    bill += 25.0

    if add_pepperoni == "Y":
        bill += 3.0
        if extra_cheese == "Y":
            bill += 1
        elif extra_cheese == "N":
            pass

    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill += 1
        elif extra_cheese == "N":
            pass

print(f'Your final bill is: ${bill}')
# Siempre me gusta complicarme :v 