# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()  # input turned into a list
for n in range(0, len(student_heights)):  # for index 0 to index len, which is n + 1 by default
  student_heights[n] = int(student_heights[n])  # every value converted to int
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
total_students = 0
for n in student_heights:  # for every n, add value n
    total_height += n

for n in student_heights: # for every n, add +1 to students
    total_students += 1

ave = total_height / total_students

print(total_height)
print(round(ave))