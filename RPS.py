import random
computer_guess=random.randint(1,3)
user_choice=int(input("enter your coice: 1 for rock, 2 for paper, 3 for scissor >>  "))
if user_choice==1 and computer_guess==3 :
    print("computer guess is ",computer_guess," that is scissor, you win")
elif user_choice==1 and computer_guess==2 :
    print("computer guess is ",computer_guess," that is paper, computer win")
elif user_choice==2 and computer_guess==3 :
    print("computer guess is ",computer_guess," that is scissor, computer win")
elif  user_choice==2 and computer_guess==1:
    print("computer guess is ",computer_guess," that is rock, you win")
elif user_choice==3 and computer_guess==1:
    print("computer guess is ",computer_guess," that is rock, computer win")
elif user_choice==3 and computer_guess==2:
    print("computer guess is ",computer_guess," that is paper, you win")
elif user_choice==computer_guess:
    print("COMPUTER GUESS IS ALSO SAME,IT'S A TIE")
else:
    print("invalid input")


    
    
    