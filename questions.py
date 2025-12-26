#Q1}write a prog to read a text from file "poem.txt" and find wheather it contain word "twinkle" or not.
with open(r"C:\Users\aishw\OneDrive\Desktop\python\file handling\poem.txt", "r") as f:
    c=f.read()
    if "twinkle" in c:
        print("yes, 'twinkle' is present in the file")
    else:
        print("no, 'twinkle' is not present in the file") 
        
#Q2}The game( ) function lets user play and returns the score in integer format .read a file "hiscore.txt" to check the previous hiscore .if the current score is more than hiscore then update the hiscore.txt file with current score.
import  random
def game():
    print("you are playing the game")
    score = random.randint(0, 100)
    with open(r"C:\Users\aishw\OneDrive\Desktop\python\file handling\hiscore.txt", "r") as f:
        hiscore = f.read()
        if(hiscore==""):
            hiscore=0
        else:
            hiscore=int(hiscore)
            
    print("Your score is:", score)
    if (score>hiscore ):
        #store the hiscore in file
        with open(r"C:\Users\aishw\OneDrive\Desktop\python\file handling\hiscore.txt", "w") as f:
            f.write(str(score))
            print("New high score!")
        
        
        return score  
game()



#Q3} write code to print table frpm 2 to 20 and store it in file "tables.txt"
def table(n):
    t=""
    for i in range(1,11):
        t+=f"{n} x {i} = {n*i}\n"
        with open(r"C:\Users\aishw\OneDrive\Desktop\python\file handling\tables.txt", "w") as f:
            f.write(t)
    
for i in range(2,21):
    table(i)
    
    
#Q4} a file contain word"donkey " multiple times .write a program to replace this word with "#######" and save it to same file.
word="donkey"
with open(r"C:\Users\aishw\OneDrive\Desktop\python\file handling\donkey.txt", "r") as f:
    content=f.read()
newcontent=content.replace(word, "#######")
with open(r"C:\Users\aishw\OneDrive\Desktop\python\file handling\donkey.txt", "w") as f:
    f.write(newcontent)
