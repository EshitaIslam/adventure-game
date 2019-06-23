import time
import random
      
def print_pause(message):
    print(message)
    time.sleep(2)

def get_random_enemy():
    enemy = random.choice(['troll', 'pirate', 'wicked fairie', 'dragon', 'gorgon'])
    return enemy

def intro(enemy):
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here, and has been terrifying the nearby willage")
    print_pause("In front of you is a house")
    print_pause("In your right is a dark cave")

def get_choice(choices):        
    
    print("")
    for choice in choices:
        print_pause(choice)
    print("What would you like to do?")

    selected_choice = ""
    while not (selected_choice == "1" or selected_choice == "2"):       
        selected_choice = input("(Please enter 1 or 2.)\n")
        
    return selected_choice
    
def house():
    # Things that happen to the player in the house
    print("Player inside the house")

def cave():
    # Things that happen to the player in the cave
    print("Player In the cave")

def field():
    print("Player In the field")

def play_game():
    enemy = get_random_enemy()
    
    intro(enemy)
    choice = get_choice(["Enter 1 to knock on the door of the house.","Enter 2 to peer into the cave."])
    if choice == "1":
        house()
    elif choice == "2":
        cave()

play_game()