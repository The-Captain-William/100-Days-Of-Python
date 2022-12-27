import pandas

student_dict = {  # formatted for pandas - > (key, list)
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data = pandas.DataFrame(student_dict)
print(student_data, "\n")

for (index, row) in student_data.iterrows():  # .iterrows() taps into row
    print(row)  # (r)
    if row.student == "Angela":  # searches for student name string
        print("\n", row.score, "\n")  # prints score int (a)

#  p(r): student   Angela
#       score          56
# Name: 0, dtype: object

# p(a): 56
