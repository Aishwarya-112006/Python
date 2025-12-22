# WAYS OF STRING DECLARATION

#a='aishwary' #single quoted string
#b="aishwary" #double quoted string
#c='''aishwary''' #triple quoted string

# STRING SLICING
name="anushka singh"
namelen=len(name)
nameshort=name[0:6] #start from index 0 to all the way till index 6 (exluding index 6)
print(namelen)
print(nameshort)
char=name[1]
print(char)

# NEGATIVE SLICING
a="sunita"
z=a[-4:-1]
print(z)
print(a[1:4])
word="amazing"
print(word[1:6:2])

# STRING FUNCTIONS
print(len("sid"))#length function
mystr="sid"
print(mystr.endswith("id")) #endwith fuction and startswith function
print(mystr.startswith("a"))
print(mystr.capitalize()) #capitalize function
print(str(12345))#str function
print(type(str(12345)))
print("SID".lower())#upper and lower function
print("sid".upper())
s="hello world"
index=s.find("world")#find function
print(index)
replacedstring=s.replace("hello","python")#replace fuction
print(replacedstring)


#ESCAPE SEQUENCE CHARACTER
ma="jghfjfiikfikgi\nsidffhjfjfjjfij"
print(ma)