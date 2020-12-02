# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()
name_concat = name1_lower + " " + name2_lower
name_T = name_concat.count('t')
name_R = name_concat.count('r')
name_U = name_concat.count('u')
name_E = name_concat.count('e')
name_L = name_concat.count('l')
name_O = name_concat.count('o')
name_V = name_concat.count('v')
name_LE = name_concat.count('e')
true = name_T + name_R + name_U + name_E
love = name_L + name_O + name_V + name_LE
true_love = int(str(true) + str(love))

if true_love < 10 or true_love > 90:
    print(f'Your score is {true_love}, you go together like coke and mentos.')
elif true_love > 40 and true_love < 50:
    print(f'Your score is {true_love}, you are alright together.')
else:
    print(f'Your score is {true_love}')
