print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
input1 = input("You have to select the left or right:").strip().lower()
if (input1 == "left"):
  print("You have to go next step.")
  input2 = input("You have to select the swim or wait:").strip().lower()
  if (input2 == "wait"):
    print("You have to go next step.")
    input3 = input("You have to select the red or yellow or blue:").strip().lower()
    if (input3 == "red"):
      print("Burned by fire.")
    elif(input3 == "yellow"):
      print("you win!")
    elif(input3 == "blue"):
      print("Eaten by beasts")
  elif (input2 == "swim"):
    print("Game the over.")
elif (input1 == "right"):
  print("Game the over.")
else:
  print("Game tha over.")
