#Locklin Sheldon, ProficiencyTest: Graded Quiz
score = 0

first = input("2 + 2 = ")
if first == "fish":
    score += 1
second = input("Mr.s LaRose is the best teacher (y/n): ")
if second == "y":
    score += 1
third = input("What word is spelt incorrectly in every dictionary?: ")
if third == "incorrectly":
    score += 1
fourth = input("What starts with 'e' and ends with 'e', but only has one letter in it?: ")
if fourth == "envelope":
    score + 1
fifth = input("fish - 2 = ")
if fifth == "half a fish":
    score += 1
print("Congrats you have received", score, "points of the available 5!")
