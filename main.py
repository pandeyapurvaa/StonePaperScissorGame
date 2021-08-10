import random
# scissor=1
# stone=2
# paper=3
player=print("your turn")
player1=int(input("choose 1,2 or 3\n"))
if player1== 1:
       print("You choose Seissor")
elif player1== 2:
       print("You choose Stone")
elif player1== 3:
       print("You choose Paper")
computer=print("computer's turn")
comp=random.randint(1,3)
print(comp)
if comp== 1:
       print("Computer choose Seissor")
elif comp== 2:
       print("Computer choose Stone")
elif comp== 3:
       print("Computer choose Paper")
if(player1==1 and comp==1):
    print("The game is Tie")
elif(player1==2 and comp==2):
    print("The game is Tie")
elif(player1==3 and comp==3):
    print("The game is Tie")
elif(player1==1 and comp==2):
    print("Computer win!")
elif(player1==1 and comp==3):
    print("You Win!")
elif(player1==3 and comp==1):
    print("Computer Win!")
elif(player1==3 and comp==2):
    print("You Win!")
elif(player1==2 and comp==1):
    print("You Win!")
elif(player1==2 and comp==3):
    print("Computer Win!")

else:
    print("invalid enter")


























































