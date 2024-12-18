import random

import sys

inventory = [""]
goldbag = 0
playerHP = 200
playerStrength = 30
playerMagic = 30
reward = ["Dwarven Double Barrel Shotgon","Dwarven Bazooka","Dwarven .357 Magnum","Dwarven Barrett .50 Caliber Sniper","Dwarven Armor","Dwarven Helmet","Dwarven Boots"]
mogusmeet = 0

def melee(OppHP):
    global playerHP, playerStrength
    enemStrength = random.randint(5, 31)
    OppHP -= playerStrength
    print("You hit the enemy and did", playerStrength, "damage.")
    playerHP -= enemStrength
    print("The Serf hits you back and deals", enemStrength, "damage.")
    print("Enemy's HP:", OppHP)
    print("Your HP:", playerHP)
    if OppHP <= 0 and playerHP > 0:
        print("You killed the Rizz Lizard Serf!")
        potion()
    if playerHP <= 0:
        while True:
            print("GAME OVER")
    return OppHP

def magic(OppHP):
    global playerHP, playerMagic
    
    enemStrength = random.randint(5, 31)
    OppHP -= playerMagic
    print("You magicked at the enemy and did", playerMagic, "damage.")
    playerHP -= enemStrength
    print("The Serf hits you back and deals", enemStrength, "damage.")
    print("Enemy's HP:", OppHP)
    print("Your HP:", playerHP)
    if OppHP <= 0 and playerHP > 0:
        print("You killed the Rizz Lizard Serf... But with magic!")
        potion()
    if playerHP <= 0:
        while True:
            print("GAME OVER")
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
                OppHP = magic(OppHP)
                if OppHP <= 0 or playerHP <= 0:
                    break
            elif eneask == "3":
                print("You ran away! (like a coward).")
                break
            else:
                print("That isn't a choice.")
    else:
        print("You didn't find any danger.")

def potion():
    global playerHP, playerStrength, playerMagic
    potion = ["strength", "health", "magic"]
    ranpot = random.choice(potion)
    print("The Serf dropped an illegal, and highly expiremental", ranpot,"potion.") 
    drink = input(f"Would you like to drink the highly illegal, possibly cancerous {str(ranpot)} potion? Your actions may have consequences... (y/n): ")#Maybe add consequences.
    if drink == "y":
        if ranpot == "strength":
            playerStrength += 10
            print("You drink the potion. The liquid coats your throat with a viscous, acidic sludge. It burns. \nStrength: ", str(playerStrength), "\nMagic: ", str(playerMagic), "\nHealth Points: ", str(playerHP))
            if ranpot == "health":
                playerHP += 10
                print("You drink the potion. The liquid coats your throat with a viscous, acidic sludge. It burns. \nStrength: ", str(playerStrength), "\nMagic: ", str(playerMagic), "\nHealth Points: ", str(playerHP))
                if ranpot == "magic":
                    playerMagic += 10
                    print("You drink the potion. The liquid coats your throat with a viscous, acidic sludge. It burns. \nStrength: ", str(playerStrength), "\nMagic: ", str(playerMagic), "\nHealth Points: ", str(playerHP))
                    if drink == "n":
                        print("Very well... The potion's glass shatters in your hands. Its contents immediatley evaporate and the glass becomes a fine dust on the ground. \nStrength: ", str(playerStrength), "\nMagic: ", str(playerMagic), "\nHealth Points: ", str(playerHP))

def bossreward():
    global inventory, reward
    ranReward = random.choice(reward)
    inventory += ranReward
    reward -= ranReward
    print("The Rizz Lizard Noble dropped:", ranReward)
    print(ranReward, "has been added to your inventory.")

def bossmelee(BossHP):
    global playerHP, playerStrength
    bossStrength = random.randint(5, 31)
    BossHP -= playerStrength
    print("You hit the Noble and did", playerStrength, "damage.")
    playerHP -= bossStrength
    print("The Noble hits you back and deals", bossStrength, "damage.")
    print("Noble's HP:", BossHP)
    print("Your HP:", playerHP)
    if BossHP <= 0 and playerHP > 0:
        print("You killed the Rizz Lizard Noble...")
    if playerHP <= 0:
        while True:
            print("GAME OVER")
    return BossHP

def bossmagic(BossHP):
    global playerHP, playerMagic
    
    bossStrength = random.randint(5, 31)
    BossHP -= playerMagic
    print("You magicked at the Noble and did", playerMagic, "damage.")
    playerHP -= bossStrength
    print("The Noble hits you back and deals", bossStrength, "damage.")
    print("Noble's HP:", BossHP)
    print("Your HP:", playerHP)
    if BossHP <= 0 and playerHP > 0:
        print("You killed the Rizz Lizard Noble...")
    if playerHP <= 0:
        while True:
            print("GAME OVER")
    return BossHP

def bossfight():
    global playerHP, mogusmeet
    BossHP = random.randint(100, 201)
    while BossHP > 0 and playerHP > 0:
        print("1. Melee Attack")
        print("2. Magic attack")
        print("3. Run Away (like a coward)")
        bossask = input("What would you like to do? (1-3): ")
        
        if bossask == "1":
            BossHP = bossmelee(BossHP)
            if BossHP <= 0 or playerHP <= 0:
                mogusmeet += 1
                break
        elif bossask == "2":
            BossHP = bossmagic(BossHP)
            if BossHP <= 0 or playerHP <= 0:
                mogusmeet += 1
                break
        elif bossask == "3":
            print("You ran away! (like a coward).")
            break
        else:
            print("That isn't a choice.")




def travel():
    global mogusmeet
    print("1. M'ogus Cape Verde")
    print("2. Spooky Dooky Cave")
    print("3. Town For Cool People")
    print("4. La Ferme Du Chagrin")
    print("5. Imposter Outpost")
    print("6. Fanum Tax Chateau")
    print("7. Boyardee Factory")
    print("8. Rizz Lizard Tour Boat Dock")
    print("9. Rizz Lizard's Sandbar (swim)")
    wherego = input("Where do you want to go? (1-9): ")
    if wherego == "1":
        if mogusmeet < 1:
            print("You arrive at the M'ogus Cape Verde Lighthouse. A foul beast known as a Rizz Lizard Noble towers over you. \n'So you're the one the King Rizz Lizard was warning us about?' the Noble mutters. \nThe Rizz Lizard has an indescribable hunger in his eyes. You ready yourself, preparing for a fight.")
            bossfight()
        else:
            print("I've already killed the Noble there. No point in going back")
    if wherego == "2":
        print("I'm in the Spooky Dooky Cave now")
    if wherego == "3":
        print("I'm in the Town For Cool People now")
    if wherego == "4":
        print("I'm at La Ferme Du Chagrin now")
    if wherego == "5":
        print("I'm at Imposter Outpost now")
    if wherego == "6":
        print("I'm in the Fanum Tax Chateau now")
    if wherego == "7":
        print("I'm back at the Boyardee Factory... Where it all started...")
    if wherego == "8":
        print("I'm at the Rizz Lizards Tour Boat Dock now")
    if wherego == "9":
        print("I swam all the way to the Rizz Lizard's Sandbar. \nI meet the King Rizz Lizard. \nI kill him. \nHe dies :(")
        sys.exit()

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
        elif ask == "4":
            travel()
        else:
            print("Not valid choice")
choice()