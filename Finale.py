import random


inventory = []
goldbag = 0
playerHP = 100

def melee(OppHP):
    global playerHP
    playerStrength = random.randint(10, 41)
    enemStrength = random.randint(5, 31)
    OppHP -= playerStrength
    print("You hit the enemy and did", playerStrength, "damage.")
    playerHP -= enemStrength
    print("The Serf hits you back and deals", enemStrength, "damage.")
    print("Enemy's HP:", OppHP)
    print("Your HP:", playerHP)
    if OppHP <= 0:
        print("You killed the Rizz Lizard Serf!")
    if playerHP <= 0:
        print("GAME OVER")
    return OppHP

def magic(OppHP):
    global playerHP
    playerMagic = random.randint(10, 41)
    enemStrength = random.randint(5, 31)
    OppHP -= playerMagic
    print("You magicked at the enemy and did", playerMagic, "damage.")
    playerHP -= enemStrength
    print("The Serf hits you back and deals", enemStrength, "damage.")
    print("Enemy's HP:", OppHP)
    print("Your HP:", playerHP)
    if OppHP <= 0:
        print("You killed the Rizz Lizard Serf... But with magic!")
    if playerHP <= 0:
        print("GAME OVER")#Make work.
    return OppHP


def fight():
    global playerHP
    ranenem = random.randint(0, 11)
    if ranenem > 5:
        OppHP = random.randint(10, 201)
        if OppHP > 100:
            enemlevel = "high level"
        elif OppHP > 50:
            enemlevel = "medium level"
        else:
            enemlevel = "low level"
       
        print(f"You have encountered a {enemlevel} Rizz Lizard Serf!")
       
        while OppHP > 0 and playerHP > 0:
            print("1. Melee Attack")
            print("2. Magic attack")
            print("3. Run Away (like a coward)")
            eneask = input("What would you like to do? (1-3): ")
           
            if eneask == "1":
                OppHP = melee(OppHP)
                if OppHP <= 0 or playerHP <= 0:
                    break
            elif eneask == "2":
                magic()
            elif eneask == "3":
                print("You ran away! (like a coward).")
                break
            else:
                print("That isn't a choice.")
    else:
        print("You didn't find any danger.")

def potion():
    print("The Serf dropped a", ,"potion.") #Add variable for potions.

print("You have been a slave to the Chef Boyardee Factory for years, and it's all thanks to the Rizz Lizards that showed up on that sorrowful day. \nThe eight Rizz Lizard Nobles that rule every piece of real estate in the land of M'ogus have been tormenting the people. Do you want to watch \neverything from the sidelines? Or do you want to step up and do something? Your choice. You can quit your job and head out for adventure, or you \ncan stay and let the land of M'ogus crumble.\n \n")


employment_status = input("stay or leave?: ") # Asks the user if they want to stay or leave
if employment_status == "stay":
    print("The guards notice you thinking deeply about your situation. They are jealous of your ability to think, so the mind-controlled guards grab and throw you outside the Boyardee walls.")
elif employment_status == "leave":
    print("Yippee, now the game can begin. \nAs you leave the building, several mind-controlled guards grab and throw you outside the Boyardee walls.")
else:
    print("I can't read it very well, but you probably decided to leave, so as you leave the building, several mind-controlled guards grab and throw you outside the Boyardee walls. :(")


def choice():
    global inventory, goldbag, playerHP
    while True:
        print("1. Check inventory")
        print("2. Look for treasure")
        print("3. Look for danger")
        print("4. Travel")
       
        ask = input("What would you like to do? (1-4): ")
       
        if ask == "1":
            print("Your inventory:", inventory)
        elif ask == "2":
            treasnum = random.randint(1, 9)
            rantreas = random.randint(0, 11)
            if rantreas > 5:
                print(f"You found {treasnum} gold on the ground!")
                goldbag += treasnum
                print(f"You now have {goldbag} gold in your goldbag.")
            else:
                print("You didn't find any treasure :(")
        elif ask == "3":
            fight()
            print("Hello")

        elif ask == "4":
            print("")
        else:
            print("Not vald choice")


choice()



