
tl = ""
tc = ""
tr = ""
ml = ""
mc = ""
mr = ""
bl = ""
bc = ""
br = ""

grid = [[tl,tc,tr],
        [ml,mc,mr],
        [bl,bc,br]]

def choice():
    global tl, tc, tr, ml, mc, mr, bl, bc, br, grid
    print("User = X, Ai = O")
    where = input("where would you like to go first?: ")
    print("1. Top left")
    print("2. Top Center")
    print("3. Top Right")
    print("4. Middle Left")
    print("5. Middle Center")
    print("6. Middle Right")
    print("7. Bottom Left")
    print("8. Bottom Center")
    print("9. Bottom Right")

    if where == "1":
        tl += "x"
        print(grid)
choice()

