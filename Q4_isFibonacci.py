'''
  Program to find a given number is fibonacci number or not
'''

a,b=1,1
user_input=int(input("Enter the Number"))
while b<user_input:
    a,b=b,a+b
if user_input==b:
   print(user_input,"is a fibonacci number")
else:
    print(user_input,"is not a fibonacci number")
