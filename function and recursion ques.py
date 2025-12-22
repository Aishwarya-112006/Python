#Q1}write a fun to find greatest of 3 no
''''def greatest(a,b,c):
    if(a>b and a>c):
        print("a is the greatest",a)
    elif(b>a and b>c):
        print("b is the greatest",b)
    else:
        print("c is the greatest",c)
greatest(10,20,30)'''
    
#Q2}write a function to convert celcius temperature to fahrenhite
'''def celtofah(t):
    fah=(t*9/5)+32
    print("The tem in fahrenhite scale is:",fah)
cel=int(input("Enter the temp in celcius scale:"))
celtofah(cel)'''

#Q3} write a recursive fun to print sum of n natural no
'''def sum(n):
    if(n==1):
        return 1
    else:
        return sum(n-1)+n
print(sum(4))'''

#Q4} write a fun to print n line as given below:
'''***
**
*'''# for n=3
'''def pattern(n):
    if(n==0):
        return ""
    else:
        print("*"*n)
        pattern(n-1)
pattern(50)'''

#Q5}write a fun to remove a given word from a list and add it strip 
def rem(li,word):
    l=[]
    for item in li:
        if not(item==word):
            l.append(item.strip(word))
    return l
li=["sid","sagar","vartika","aastha"]
rem(li,"ka")
    