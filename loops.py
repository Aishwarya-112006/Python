# #for loop
# for i in range(1,6):
#     print(i)

# #while loop
# i=1
# while(i<51):
#     print(i)
#     i+=1

#PROG TO PRINT CONTENT OF LIST USING WHILE LOOP
l=["sid",1,34,"adi"]
i=0
while(i<len(l)):
    print(l[i])
    i+=1
#PROG TO PRINT CONTENT OF LIST,TUPLE AND STRING USING FOR LOOP
lst=[1,45,6,7,8,89]
for item in lst:
    print(item)
tup=(100,97,69)
for i in tup:
    print(i)
s="Aishwarya singh"
for i in s:
    print(i)


#USING RANGE FUN
for i in range(0,100,2):
    print(i)


#USING FOR LOOP WITH ELSE:else block is executed after loop is exhausted
l=[100,80,90]
for item in l:
    print(item)
else:
    print("Done")

#BREAK STTEMENT:terminate programe abruptly
for i in range(0,80):
    
    
    if(i==3):
        break
    print(i)



#Continue staement:skips the value of specific iteration
for i in range(100):
    if(i==50):
        continue
    print(i)
    
#while loop: the con is checked first if its true it gets executed else not ---> if the loop is entered the process of condition check and execution is executed till condition becomes false
i=1
while(i<10):
    print(i)
    i+= 1

#PASS STATEMENT---> null staement ,instruct to do nothing
l=[4,6,8]
for item in l:
    pass
print(item)