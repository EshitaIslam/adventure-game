import time
      

def print_pause(message):
    print(message)
    time.sleep(2)

def intro():
    print_pause("You find yourself in a dark dungeon.")
    print_pause("In front of you are two passageways.")

def get_choice():    
    valid_choice = False
    choice = ""
    while not valid_choice:
        print("")
        print("Enter 1 to knock on the door of the house.")
        print("Enter 2 to peer into the cave.")
        choice = input("(Please enter 1 or 2.)\n")
        valid_choice = (choice == "1" or choice == "2")

    if choice == "1":
        house()
    elif choice == "2":
        cave()

def house():
    # Things that happen to the player in the house
    print("Player inside the house")

def cave():
    # Things that happen to the player in the cave
    print("Player In the cave")

def field():
    print("Player In the field")



intro()
get_choice()