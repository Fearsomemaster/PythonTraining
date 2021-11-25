'''
    Program to find Maximum value, Minimum value and number of single double and three
     digits numbers entered
'''
max_number=0
min_number=0
one_time=0
single_digit=0
double_digit=0
triple_digit=0
while True:
    User_input=int(input("Enter a Number"))
    count=0
    if User_input==0:
        break
    if one_time==0:
        max_number=User_input
        min_number=User_input
        one_time+=1
    if User_input>max_number:
        max_number=User_input
    if User_input<min_number:
        min_number=User_input
    while User_input>0:
        count+=1
        User_input=User_input//10
    if count==3:
        triple_digit+=1
    elif count==2:
        double_digit+=1
    else:
        single_digit+=1
    print("Maximum number :",max_number)
    print("Minimum number :",min_number)
    print("Single digit numbers :",single_digit)
    print("Double digit numbers :",double_digit)
    print("Triple digit numbers :",triple_digit)
    
    
       
        
    
