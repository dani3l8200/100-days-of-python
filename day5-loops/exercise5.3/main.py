# Write your code below this row 👇
sum_total = 0
for even_number in range(0, 101):
    if even_number % 2 == 0:
        sum_total += even_number

print(f'The sum of even numbers is: {sum_total}')