student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.


# TODO-2: Write your code below to add the grades to student_grades.👇
student_grades = {}  # empty dict
for key in student_scores:  # name
    key_value = student_scores[key]  # mapping name to grade
    if key_value < 70:  # if grade
        student_grades[key] = "Fail"  # map that key to new key value
    elif 71 <= key_value <= 80:
        student_grades[key] = "Acceptable"
    elif 81 <= key_value <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 91 <= key_value <= 100:
        student_grades[key] = "Outstanding"
print(student_scores)






# 🚨 Don't change the code below 👇
print(student_grades)


