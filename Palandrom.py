#Locklin Sheldon, SkillPractice: Palandrom
pospal = input("Insert Word: ")
revpal = pospal[::-1]
print(revpal)
str(pospal)
str(revpal)
if revpal == pospal:
    print("This IS a palandrom :).")
if revpal != pospal:
    print("This is NOT a palandrom :(")
