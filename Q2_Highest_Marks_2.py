'''
   Program to find the roll no of a student who scored highest marks
'''
marks=[78,89,85,91,93,82,79]
roll_nos=[1,2,3,4,5,6,7]
Marks_index=1
Max_marks=marks[0]
for Marks_index in marks:
    if Marks_index > Max_marks:
        Max_marks=Marks_index
count=0
value=0
for value in marks:
    if(value==Max_marks):
        S_rollno=count
    count+=1
S_rollno=roll_nos[S_rollno]
print("Roll no of Student who scored highest marks is:-",S_rollno)  
