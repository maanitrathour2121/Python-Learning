import random
computer = random.choice([-1, 0, 1])

youDict = {"s": -1, "w": 0, "g": 1}
reverseDict = {-1: "Snake", 0: "Water", 1: "Gun"}
you = youDict[input("Enter your choice (s/w/g): ")]
print(f"Computer chose: {reverseDict[computer]}\nYou chose: {reverseDict[you]}")

if computer == you:
    print("It's a tie!")
else:
    if (you == -1 and computer == 0) or (you == 0 and computer == 1) or (you == 1 and computer == -1):
        print("You win!")
    else:
        print("Computer wins!")