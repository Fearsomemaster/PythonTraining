'''
Program to find Grades of students
'''

english_mark=int(input("Enter the marks scored in subject English"))
science_mark=int(input("Enter the marks scored in subject Science"))
maths_mark=int(input("Enter the marks scored in subject Maths"))
total_marks=(english_mark+science_mark+maths_mark)/3
print("Total Marks:",total_marks)
if(total_marks>=90):
    print("Grade A")
elif(total_marks>=80):
    print("Grade B")
elif(total_marks>=35):
    print("Average")
else:
    print("Fail")
