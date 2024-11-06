CharName = input("What is your character name?: ")

CharClass = input("1 = Wizard, 2 = Warrior, 3 = Rogue: ")

Stats = "Name:", CharName, "Class:", CharClass

Wizard = ("Health: 5, Strength: 7, Dexterity: 4, Intelligence: 20")

if CharClass == 1:
     Stat = Wizard + Stats

print(Stats)