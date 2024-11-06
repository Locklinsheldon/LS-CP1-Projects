CharName = input("What is your character name?: ")
CharClass = input("Wizard, Warrior, or Rogue: ")
CharRace = input("Dwarf, Human, Ogre, Mrs. LaRose: ")

Wizard = "Health: 5, Strength: 7, Dexterity: 4, Intelligence: 20"
Warrior = "Health: 19, Strength: 20, Dexterity: 13, Intelligence: 3"
Rogue = "Health: 9, Strength: 13, Dexterity: 20, Intelligence: 18"

Dbonus = "+3 Health"
Hbonus = "+2 Intelligence"
Obonus = "+7 Strength"
Lbonus = "+20 All"

Dwarf = ("Dwarf")
Human = ("Human")
Ogre = ("Ogre")
Mrs_LaRose = ("Mrs. LaRose")

Stats = f"Name: {CharName}, Class: "

Bonus = ("")

if CharClass == "Wizard":
    Stats += f"Wizard, {Wizard}"
elif CharClass == "Warrior":
    Stats += f"Warrior, {Warrior}"
elif CharClass == "Rogue":
    Stats += f"Rogue, {Rogue}"
else:
    print("ur dum")

if CharRace == "Dwarf":
    Bonus = Dbonus
elif CharRace == "Human":
   Bonus = Hbonus
elif CharRace == "Ogre":
    Bonus = Obonus
elif CharRace == "Mrs. LaRose":
   Bonus = Lbonus
else:
    print("ur not vary smert")

print(Stats)

print(f"Race: {CharRace}, Bonus: {Bonus}")