student = {
    "Sumant": 'A',
    "Sonu" : 'C',
    "Ranjeet": 'B'
}
print("Before: ", student)

update = (input("Enter Yes or No based on the Update or new Add on, Yes for update and No for New Add on: "))

if update == "Yes":
    existingName = input("Enter the name that you want to update the grade: ")
    existingGrade = input("Enter the new grade: ")
    student[existingName] = existingGrade
else:
    newStudentName = input("Enter the student name: ")
    newStudentGrade = input("Enter the grade: ")
    student[newStudentName] = newStudentGrade
print("After: ", student)
