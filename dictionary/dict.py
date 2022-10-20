# Write Python code which Accept the student name and in turn returns their respective Mark.
# Make sure to use dictionaries to store student name and their respective mark.
# The dictionary should include at least 7 elements.

marks = {"Peter": 52, "Jancy": 42, "Paul": 98, "Helna": 97, "John": 74, "Jibin": 84, "Jack": 99}

try:
    student_name = input("Enter the student name: ")
    print("Mark of", student_name, "is", marks[student_name])
except KeyError:
    print("Student does not exist")
