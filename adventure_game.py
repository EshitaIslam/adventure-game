import time

print("You find yourself in a dark dungeon.")
time.sleep(2)
print("In front of you are two passageways.")
time.sleep(2)

print("")
print("Enter 1 to knock on the door of the house.")
print("Enter 2 to peer into the cave.")
choice = input("(Please enter 1 or 2.)\n")
valid_choice = choice == "1" or choice == "2"

while(not valid_choice):
    if choice == "1":
        print("User chose 1")
    elif choice == "2":
        print("User chose 2")
    else:
        print("")
        print("Enter 1 to knock on the door of the house.")
        print("Enter 2 to peer into the cave.")
        choice = input("(Please enter 1 or 2.)\n")
        valid_choice = choice == "1" or choice == "2"