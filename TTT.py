count = 1
for row in range(3):
    for col in range(3):
        print(count, end = " ")
        count += 1      
    print()   

ask = input("Type the number you want to place x on: ")

if ask == "1":
    for row in range(3):
        for col in range(3):
            if ask == "1":
                if row == 0 and col == 0:
                        print("x")
                        x = 0
            else:
                print(count, end = " ")
        print()