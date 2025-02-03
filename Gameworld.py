print("Welcome to the Game World.")
print("You have two games to choose from: running or long jump.")
Game = input("Enter the game you want to play (running or longjump):").strip().lower()
if Game == "running":
    distance = input("Choose your distance (200m or 100m):").strip().lower()
    if distance == "200m":
        print(" You won the 200m race.")
    elif distance == "100m":
        print("Game over.")
    else:
        print("Game over.")
elif Game == "longjump":
    jump_distance = input("Choose your jump distance (7m or 8m):").strip().lower()
    if jump_distance == "8m":
        print("You won the long jump with an 8m jump.")
    elif jump_distance == "7m":
        print("Game over.")
    else:
        print("Game over.")
else:
    print("Game over.")
