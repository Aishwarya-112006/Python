#WAP TO PRINT MULTIPLICATION TABLE FOR ANY NO USING FOR AND WHILE  LOOP in reverse order6

n=int(input("Enter the number"))
for i  in range (1,11):
    print(f"{n}*{11-i}={n*(11-i)}")
'''USING WHILE LOOP
m=int(input("Enter the no.:"))
i=1
while(i<11):
    print(f"{n}*{i}={n*i}")
    i+=1'''


#WAP TO GREET ALL PERSON NAMES STORED IN A LIST l AND WHICH STARTS WITH S
l=["Harry","Soha","Soham"]
for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")


#WAP to tell wheather a given no is prime or not
num=int (input("Enter the number:"))
for i in range(2,n):
    if(n%i==0):
        print("number is  prime")
else:
    print("Number is not prime")


#WAP TO PRINT SUM OF FIRST N NATURAL NO USING WHILE LOOP
a=int(input("Enter the num:"))
i=1
sum=0
while(i<=a):
    sum+=i
    i+=1
print(sum)


#WAP TO PRINT THE FACTORIAL OF A GIVEN NUM
b=int(input("Enter the number"))
product=1
for i in range(1,b+1):
    product=product*i
print(f"the factorial of{n} is {product}")

#WAP TO PRINT FOLLOWING PATTERN
'''*
  ***
 *****'''
c=int(input("Enter the number of line:"))
for i in range(1,c+1):
    print(" "*(c-i),end="")
    print("*"*(2*i-1),end="")
    print("")

#WAP TO PRINT FOLLOWING PATTERN
'''
*
**
***'''
d=int(input("Enter the number of line"))
for i in range(1,d+1):
    print("*"*i,end="")
    print("")

#Wap to print the following pattern
'''
***
* *
***'''
e=int(input("Enter the no of line:"))
for i in range(1,e+1):
    if(i==1 or i==3):
        print("*"*e,end="")
    else:
        print("*",end="")
        print(" "*(e-2),end="")
        print("*",end="")
    print("")
