#RECURSION: a function which calls itself,used to directly use mathematical formula in a function

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the number:"))
print(f"the factorial  of {n}is:",(fact(n)))