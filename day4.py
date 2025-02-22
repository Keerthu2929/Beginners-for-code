import random

print("Welcome to Rock , Paper , Scissors Game.")

print("You have to choices: rock , paper, scissors.")

player_choice = int(input("Rock , Paper , Scissors\n"))

select_choices = ["stone","paper","scissors"]

computer_choices = random.choice(select_choices)

print(f"Computer chose: {computer_choices}")

if player_choice == computer_choices:

  print("It is a tie!")

elif player_choice == "stone":

  if computer_choices == "scissors":

    print("You win!.")

  else:

    print("You lose!.")

elif player_choice == "paper":

  if computer_choices == "stone":

    print("You win!.")

  else:

    print("You lose!.")

elif player_choice == "scissors":
   
   if computer_choices == "paper":
        
        print("You win!.")

else:

  print("You lose!.")

