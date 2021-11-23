'''
   Program to find the roll no of a student who scored highest marks
'''
marks=[78,89,85,91,93,82,79]
Marks_index=1
Max_marks=marks[0]
S_rollno=1
count=0
for Marks_index in marks:
    if Marks_index > Max_marks:
        Max_marks=Marks_index
        S_rollno=count+1
    count+=1
print("Roll no of Student who scored highest marks is:-",S_rollno)  
