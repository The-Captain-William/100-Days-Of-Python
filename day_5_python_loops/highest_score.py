# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# print(sorted(student_scores)[-1]) no for loop used, still could be useful

max_score = 0
for n in student_scores:
    if max_score < n:
        max_score = 0
        max_score += n
print(max_score)
print(f"The highest score in the class is: {max_score}")


