# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
prom = 0
size = 0
for n in student_heights:
    prom += n
    size += 1
prom = round(prom / size)
print(prom)