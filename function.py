#FUNCTION:way of writing a code,group of statements performing a specific task
#PROGRAME TO MAKE A FUN TO CALCULATE AVG OF 3 NO INPUT B Y USER
def avg():#function defination
    a=int(input("Enter no 1:"))
    b=int(input("Enter no 2:"))
    c=int(input("Enter no 3 :"))
    avg=(a+b+c)/3
    print("The average of three no is:",avg)
avg()#function call
#Programe to greet user by "Good day" by function
def  fun():
    print("Good day")
fun()

'''TYPES OF FUNCTIONS
USER DEFINED:made by user,
builtin:already present in libraries,len(),print() etc'''

#FUNCTION WITH ARGUMENT---->name is parameter here
def hello(name,bye):
    print("hello"  +name)
    print(bye)
    return "ok"# return is used when we want to give value
a=hello("sid","bye")
hello("sagar","bye")
hello("vartika","bye")


#Default argument value:we can have value as default as default argument in the function
def hello(name,bye="see you"):
    print("hello"  +name)
    print(bye)
    return "ok"# return is used when we want to give value
a=hello("sid","bye")
hello("sagar","bye")
hello("vartika")

