import csv

#  you can either read in line-by-line or all at once

#  first open the file
with open ('data/students.csv', 'r', encoding = 'utf-8') as f:
    reader = csv.DictReader(f)
    list_of_student_dicts = list(reader)
    listof_studetns = []

for student_dict in list _of_student_dicts: 
    new_student = cls(**student_dict)
    list_of_students = append(new_student)
restu list_of_students

# convert the file into a list of dictionaries
    print(reader)