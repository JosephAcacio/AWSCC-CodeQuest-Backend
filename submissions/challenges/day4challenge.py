firstPlayer= input("Choose among 'Rock', 'Paper', or 'Scissor': ");
secondPlayer = input("Choose among 'Rock', 'Paper', or 'Scissor': ");

Player1 = firstPlayer.capitalize();
Player2 = secondPlayer.capitalize();

print(f"\nPlayer 1: {Player1}");
print(f"Player 2: {Player2}\n");

if (Player1 == "Rock") and (Player2 == "Rock"):
    print("Tie");
elif(Player1 == "Rock") and (Player2 == "Paper"):
    print("Player 2 wins");
elif(Player1 == "Rock") and (Player2 == "Scissor"):
    print("Player 1 wins");
elif(Player1 == "Paper") and (Player2 == "Paper"):
    print("Tie");
elif(Player1 == "Paper") and (Player2 == "Rock"):
    print("Player 1 wins");
elif(Player1 == "Paper") and (Player2 == "Scissor"):
    print("Player 2 wins");
elif(Player1 == "Scissor") and (Player2 == "Scissor"):
    print("Tie");
elif(Player1 == "Scissor") and (Player2 == "Paper"):
    print("Player 1 wins");
elif(Player1 == "Scissor") and (Player2 == "Rock"):
    print("Player 2 wins");
else:
    print("You entered an invalid value, please use proper words as directed");
