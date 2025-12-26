''' programe to build password guessing game

computer picks the secret password(words) the user keeps guessing the word after each guess computer gives hint how close the word is 
game count how many guess it takes can add different difficulty level'''


import random

easy=['tiger','lion','panther','hyena']
medium=['python','blanket','bottle','monkey']
difficult=['umbrella','diamond','computer','elephant']


print("Welcome to password guessing game")
print("Choose the difficulty level: easy,medium,difficult")

level=input("Enter the difficulty level:").lower()
if level=="easy":
    sec=random.choice(easy)
elif level=="medium":
    sec=random.choice(medium)
elif level=="difficult":
    sec=random.choice(difficult)
    
else:
    print("Invalid value,take easy level")
    sec=random.choice(easy)
    
attempts=0
print("\n Enter the password")

while True:
    guess=input("Enter your guess:").lower()
    attempts+=1
    
    if guess==sec:
        print(f"Congrats! you guessed the correct password in{attempts} attempt")
        
        break
    hint=""
    for i in range(len(sec)):
        if i<len(guess) and guess[i]==sec[i]:
            hint+=guess[i]
        else:
            hint+="_"
    print("Hint",hint)
print("Game over")
        
    