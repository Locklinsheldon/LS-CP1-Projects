word = input("Piggy Latin Converternatorinyzor: ")

vowel = ["a, e, i, o, u"]

rem = list(word)[0]

listy = list(word)

listy.remove(rem)

listy.append("a")

listy.append("y")

print(listy)

if vowel in word:
    