a,b=1,1
previous_number=0
next_number=0
user_input=int(input("Enter the Number:"))
while b<user_input:
    previous_number=b
    a,b=b,a+b
    next_number=b
low_value=user_input-previous_number
high_value=next_number-user_input
if user_input==previous_number:
   print(user_input,"is a fibonacci number")
elif low_value<high_value:
    print(user_input,"is not fibonacci number nearest number is ",previous_number)
elif low_value>high_value:
    print(user_input,"is not fibonacci number nearest number is ",next_number)
else:
    print(user_input,"is not fibonacci number nearest number are",previous_number,"and",next_number)
