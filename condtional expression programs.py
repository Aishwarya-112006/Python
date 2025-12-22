#PROG TO PRINT GREATEST OF 4 NO ENTERED BY USER
a=int(input("Enter no 1:"))
b=int(input("Enter no 2:"))
c=int(input("Enter no 3:"))
d=int(input("Enter no 4:"))
if(a>b and a>c and a>d):
    print("Greatest no is a:",a)
elif(b>a and b>c and b>d):
    print("Greatest no is b:",b)
elif(c>a and c>b and c>d):
    print("Greatest no is c:",c)
else:
    print("Greatest no is d:",d)



#PROG TO FIND WHEATHER AS STUDENT IS PASSED OR FAILED IF IT REQUIRE TOTAL OF 40% OR 33% TO PASS TAKE MARKS OF THREE SUBJECTS
m1=int(input("Enter mark 1:"))
m2=int(input("Enter mark 2:"))
m3=int(input("Enter mark 3:"))
avg=(m1+m2+m3)/3
if(avg>40 or avg>33):
    print("Passed")
else:
    print("Failed")



#SPAM COMMENT CONTAINS"MAKE A LOT OF MONEY","BUY NOW" ,SUB THIS, CLICK THIS,WRITE A PROG TO DETECT THESE SPAM
p1="MAKE A LOT OF MONEY"
p2="BUY NOW"
p3="SUB THIS"
p4="CLICK THIS"
text=input("Enter the text")
if((p1 in text)or(p2 in text)or(p3 in text)or(p4 in text)):
    print("spam")
else:
    print("Safe")



#PROG TO FIND WHEATER A GIVEN USERNAME CONTAIN LESS THAN 10 CHAR OR NOT
username=input("Enter username:")
if(len(username)<10):
    print("Username is less than 10 char")
else:
    print("Username is greater ias greater than 10 character")


#PROG TO FIND OUT WHEATHER A GIVEN NAME IS PRESENT IN LIST OR NOT
l=["sid","adi","satyam"]
name=input("Enter the name:")
if(name in l):
    print("Name is present in list")
else :
    print("Name is not in list")



#PROG TO TELL IF GIVEN POST IS TALKING HARRY OR NOT
post=input("Enter the post")
if("Harry" in post.lower()):
    print("Post is about harry")
else:
    print("Post is not about harry")