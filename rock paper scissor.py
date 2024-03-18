import random
print("Instructions are: ")
print("1.Rock beats paper.")
print("2.Paper beats Scissor.")
print("3.Scissor beats Rock.")
rock='''
        _____________
_______          ____)
               (_____)
               (_____)
               (______)
               (_____)
_______        (___)
        _____ '''

paper='''
          
        __________
____________    ______)_____
                  ___________)
                   ______________)
__________          _________)
            _____   ______)'''

scissor='''
              _______
____________         ______)
                     (______)
                      ________________)
                      ________________)
                      (_______)
                      (_______)
__________                      
              ________    
             '''



images=[rock,paper,scissor]        
user=int(input("enter your choice:type 0 for Rock,1 for paper,2 for Scissors:"))
if(user>2 or user<0):
    print("You entered invalid number,You lose.")
else:
  print(images[user])
  computer_choice=random.randint(0,2)
  print("computer choice: ")
  print(images[computer_choice])
  if user==computer_choice:
    print("It is a tie")
  elif computer_choice== 0 and user==2:
    print("You lose")
  elif user==0 and computer_choice==2:
    print("You win")
  elif computer_choice > user:
    print("You lose")
  elif user > computer_choice:
    print("You win")
print("Do you want to play again !!!")
print("Feedback about the game please?")
