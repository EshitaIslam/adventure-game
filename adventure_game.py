import time
import random
      
def print_pause(message):
    print(message)
    time.sleep(random.choice([1, 2]))

def get_random_enemy():
    enemy = random.choice(['troll', 'pirate', 'wicked fairie', 'dragon', 'gorgon'])
    return enemy

def intro(enemy):
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.")

def get_choice(choices):        
    
    print("")
    for choice in choices:
        print_pause(choice)
    print("What would you like to do?")

    selected_choice = ""
    while not (selected_choice == "1" or selected_choice == "2"):       
        selected_choice = input("Please enter 1 or 2: ")
        
    return selected_choice
    
def house(enemy, weapons_picked, special_weapon):    
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")

    if not special_weapon in weapons_picked:        
        print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.")
    
    choice = get_choice(["Enter 1 to fight", "Enter 2 to run away"])
    if choice == "1":
        if special_weapon in weapons_picked:
            print_pause(f"As the {enemy} moves to attack, you unsheath your new sword.")
            print_pause(f"The {special_weapon} shines brightly in your hand as you brace yourself for the attack.")
            print_pause(f"But the {enemy} takes one look at your shiny new toy and runs away!")
            print_pause(f"You have rid the town of the {enemy}. You are victorious!")
        else:            
            print_pause("You do your best...")
            print_pause(f"But your dagger is no match for the {enemy}.")
            print_pause("You have been defeated!")
    elif choice == "2":
        field(enemy, weapons_picked, special_weapon)

def cave(enemy, weapons_picked, special_weapon):
    # Things that happen to the player in the cave
    print_pause("You peer cautiously into the cave.")
    
    if not special_weapon in weapons_picked:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause(f"You have found the magical {special_weapon}")
        print_pause("You discard your silly old dagger and take the sword with you.")
        weapons_picked.append(special_weapon)
    else:
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now")
    
    print_pause("You walk back out to the field.")
    
    choice = get_choice(["Enter 1 to knock on the door of the house.","Enter 2 to peer into the cave."])
    if choice == "1":
        house(enemy, weapons_picked, special_weapon)
    elif choice == "2":
        cave(enemy, weapons_picked, special_weapon)

def field(enemy, weapons_picked, special_weapon):
    print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
    print_pause("")
    choice = get_choice(["Enter 1 to knock on the door of the house.","Enter 2 to peer into the cave."])
    if choice == "1":
        house(enemy, weapons_picked, special_weapon)
    elif choice == "2":
        cave(enemy, weapons_picked, special_weapon)

def play_game():
    enemy = get_random_enemy()
    weapons_picked = []
    special_weapon = "Sword of Ogorth"
    
    intro(enemy)
    choice = get_choice(["Enter 1 to knock on the door of the house.","Enter 2 to peer into the cave."])
    if choice == "1":
        house(enemy, weapons_picked, special_weapon)
    elif choice == "2":
        cave(enemy, weapons_picked, special_weapon)

play_game()