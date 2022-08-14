import random
for i in range(100):
    print("-" *50)
    print("\tSTONE/PAPER/SCISSER")
    print("-"*50)

    player=input("Enter Your Name:")
    option=input("Select Stone/Paper/Scissor:")
    print("-"*50)

    print(player, "Selected", option)

    opt=["Stone", "Paper", "Scissor"]
    coption= random.choice(opt)
    print("Computer Selected", coption)
    print("-"*50)

    if option== "Paper":
        if coption=="Paper":
            print("Draw")
        elif coption=="Scissor":
            print("Computer Wins")
        else:
            print(player, "Wins")

    elif option== "Stone":
        if coption=="Stone":
            print("Draw")
        elif coption=="Paper":
            print("Computer Wins")
        else:
            print(player, "Wins")

    elif option== "Scissor":
        if coption=="Scissor":
            print("Draw")
        elif coption=="Stone":
            print("Computer Wins")
        else:
            print(player, "Wins")
    else: 
        print("Invalid")

print("-"*50)