num = int(input("Insert: "))

fornum = "Commafied: {:,}"

fournum = "4 Decimal points: {:.4f}"

pernum = int(num*100)

dolnum = "Dollar decimal: {:.2f}"

print(fornum.format(num))

print(fournum.format(num))

print(pernum,"%")

print(dolnum.format(num))