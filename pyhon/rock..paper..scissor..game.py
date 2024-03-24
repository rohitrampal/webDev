# user_name=input("Enter you name: ")
# print(f"""Hi {user_name}, Welcome to the Rock Paper Scissor game 
# You are playing with computer 
# Let's play the game, good luck\n """)

import random

var=["r","p","s"]
cmp_choice=random.choice(var)
i=0
ucount=0
ccount=0
while i<5:

    user_choice=input("""Enter any of the given option
    for Rock type r
    for Paper type p
    for Scissor type s:\n""")
    
    if cmp_choice==user_choice:
        print("You choose: ",user_choice)
        print("Comouter choose: ",cmp_choice)
        print("Match draw...")

    elif (user_choice=="r" and cmp_choice=="s") or (user_choice=="p" and cmp_choice=="r") or (user_choice=="s" and cmp_choice=="p"):
        print("You choose: ",user_choice)
        print("Comouter choose: ",cmp_choice)
        print("You win the game...")
        ucount+=1
    else:
        print("You choose: ",user_choice)
        print("Comouter choose: ",cmp_choice)
        print("Computer win the game...")
        ccount+=1
    i+=1

if ucount==ccount:
    print("user: ",ucount)
    print("computer: ",ccount)
    print("Match draw")
elif ucount>ccount:
    print("user: ",ucount)
    print("computer: ",ccount)
    print("You win the game")
else:
    print("user: ",ucount)
    print("computer: ",ccount)
    print("Computer win the game")
