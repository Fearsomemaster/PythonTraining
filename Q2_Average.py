'''
   Program to find average number of marks scored by batch of students
'''

marks=[78,89,85,91,93,82,79]
sum=0
marks_no=0
for i in marks:
    sum=sum+i
    marks_no+=1
avg=sum/marks_no
print("Avg =",avg)
