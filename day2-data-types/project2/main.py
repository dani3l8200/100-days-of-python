# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: You might need to do some research in Google to figure out how to do this.
print('Welcome to the tip calculator')
bill = float(input('What was the total bill? $'))
porcentage = int(
    input('What porcentage tip would you like to give? 10, 12 or 15? '))
people = int(input("How many people to split the bill? "))
result_porcentage = (1 + porcentage / 100)
result = round((bill / people) * result_porcentage, 2)
message = f'Each person should pay: ${result}'
print(message)
