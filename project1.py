#I:idea of the project
#B:what to build
#H:how the project will work
#W:concept used
#S:steps of pseudocode
#S:streatching 3 features

#FAKE NEWS HEADLINE GENERATOR

#subjects ,action and places are main foucus

#use of topics:

#list:store grp of word like name,place and action
#random.choice():to pick one item randomly from the list
#print(): to show headline on screen
#input(): to ask user if they want another headlinre or not
#while loop:to reapet the process till user says no
#string concatenation:to make sentence from given word 
#string format: use to format the sentence as user wish

import random

names=["Yash",
      "Purnima",
      "Himansh"]
actions=[
    "is dating",
    "slaps",
    "Was playing badmintion"
    
]
while True:
    name=random.choice(names)
    action=random.choice(actions)
    headline=f"BREAKING NEWS  {name} {action}"
    print("\n"+headline)
    
    user=input("Do you want more headlines(yes/no)").strip().lower()
    if user=="no":
        break
    print("Thank you for using fake headline generator")
