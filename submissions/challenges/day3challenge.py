#mini challenge

num = int(input("Please enter a number: "));

if num < 0:
    print(f"{num} is a Negative number!");
elif num > 0:
    print(f"{num} is a positive");
else:
    print("The number you entered is Zero!");

#main challenge
print("\nType 'Y' if yes, 'N' if no");
first_answer = input("Is man asking for shelter? (Y/N): ");

if first_answer == "Y":
    second_answer = input("Police arrived and asked whether the thief is inside. (Y/N) ")
    if second_answer == "Y":
        print("You Win!")
    elif second_answer == "N":
        print("Game Over!")
    else:
        print("Invalid answer, please try again");
elif first_answer == "N":
    second_answer = input("He attacked on you, will you knock him down? (Y/N) ")
    if second_answer == "Y":
        print("You Win!");
    elif second_answer == "N":
        print("Game Over!");
    else:
        print("Invalid answer, please try again");
else:
    print("Invalid answer, please try again");
    