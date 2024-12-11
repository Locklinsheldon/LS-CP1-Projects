print("You have been a slave to the Chef Boyardee Factory for years, and it's all thanks to the Rizz Lizards that showed up on that sorrowful day. \nThe eight Rizz Lizard Nobles That rule every piece of real estate in the land of M'ogus have been tormenting the people. Do you want to watch \neverything from the sidelines? Or do you want to step up and do something? Your choice. You can quit your job and head out for adventure, or you \ncan stay and let the land of M'ogus crumble.\n \n")

employment_status = input("stay or leave?: ")
if employment_status == "stay": 
    print("Okay. whatever. I guess the land of M'ogus doesn't matter that much.")
    quit
elif employment_status == "leave": 
    print("Yippee, now the game can begin. \nAs you leave the building, several mind controlled guards grab you and through you outside the Boyardee walls. Now, with your newly found freedom,")
else:
    print(" I dont't think that's an option :(")
    quit

def choice():
    while True:
        print("What would you like to do")
choice()