import random

options = ["rock","paper","scissor"]
userscore = int(0)
aiscore = int(0)
aichoice = random.choice(options)

def RPSchoice():
    global userscore, aiscore
    while True: 
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            if choice == "1" and aichoice == "rock":
                print("You chose: Rock. The ai chose: Rock. It's a tie.")

        if choice == "1":
            if choice == "1" and aichoice == "paper":
                aiscore += 1
                print("You chose: Rock. The ai chose: Paper. The ai won.")

        if choice == "1":
            if choice == "1" and aichoice == "scissor":
                userscore += 1
                print("You chose: Rock. The ai chose: Scissors. You won.")

        if choice == "2":
            if choice == "2" and aichoice == "rock":
                userscore += 1
                print("You chose: Paper. The ai chose: Rock. You won.")

        if choice == "2":
            if choice == "2" and aichoice == "paper":
                print("You chose: Paper. The ai chose: Paper. It's a tie.")

        if choice == "2":
            if choice == "2" and aichoice == "scissor":
                aiscore += 1
            print("You chose: Paper. The ai chose: Scissors. The ai won.")

        if choice == "3":
            if choice == "3" and aichoice == "rock":
                aiscore += 1
                print("You chose: Scissors. The ai chose: Rock. The ai won.")

        if choice == "3":
            if choice == "3" and aichoice == "paper":
                userscore += 1
                print("You chose: Scissors. The ai chose: Paper. You won.")

        if choice == "3":
            if choice == "3" and aichoice == "scissor":
                print("You chose: Scissors. The ai chose: Scissors. It's a tie.")
        
        if choice == "4":
            print("Your score was:", userscore, "Ai score was:", aiscore)
            break    
        
        else:
            print("Invalid choice")        
RPSchoice()

