# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
high_score = 0
for n in student_scores:
    if high_score == 0:
        high_score = n
    elif high_score > n:
        print(f'actual high score: {high_score}, searching other high score if is possible...')
    elif high_score < n:
        high_score = n
print(f'\nThe highest score in the class is: {high_score}')