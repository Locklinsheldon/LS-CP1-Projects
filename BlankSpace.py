import random
def display_intro():print("Welcome to the Mystic Forest Adventure!")
print("You find yourself at the edge of a dark, mysterious forest.")
print("Your goal is to find the hidden treasure and escape safely.")
def make_choice(options):for i,option in enumerate(options,1):print(f"{i}. {option}")
while True:
try:choice=int(input("Enter your choice: "))
if 1<=choice<=len(options):return choice
else:print("Invalid choice. Try again.")
except ValueError:print("Please enter a number.")
def explore_forest():print("You venture deeper into the forest...")
events=["You encounter a friendly woodland creature.","You find a shimmering portal.","You discover an ancient ruins.","You come across a bubbling stream."]
print(random.choice(events))
def find_treasure():print("Congratulations! You've found the hidden treasure!")
print("It's a chest filled with gold coins and magical artifacts.")
def face_challenge():print("Oh no! You've encountered a challenge!")
challenges=["A giant spider blocks your path.","A riddle-speaking owl demands an answer.","A magical barrier requires a spell to pass."]
print(random.choice(challenges))
if random.random()<0.5:print("You successfully overcome the challenge!")
return True
else:print("You fail to overcome the challenge.")
return False
def play_game():display_intro()
treasure_found=False
while not treasure_found:
print("\nWhat would you like to do?")
choice=make_choice(["Explore the forest","Search for treasure","Face a challenge","Exit the forest"])
if choice==1:explore_forest()
elif choice==2:
if random.random()<0.3:find_treasure()
treasure_found=True
else:print("No treasure here. Keep searching!")
elif choice==3:
if face_challenge():
if random.random()<0.4:find_treasure()
treasure_found=True
elif choice==4:print("You decide to leave the forest. Game over!")
return
if treasure_found:print("Congratulations! You've won the game!")
if __name__=="__main__":play_game()