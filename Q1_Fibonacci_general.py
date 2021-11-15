a,b=1,1
user_input=int(input("Number of Fibonacci numbers required"))
user_input-=1
counter=0
print(a)
while counter<user_input:
    print(b)
    a,b=b,a+b
    counter+=1
