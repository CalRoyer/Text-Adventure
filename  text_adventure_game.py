 import random

# ASCII art for the game's title
intro_art =  '''
 _______ __   __ _______                                             
|       |  | |  |       |                                            
|_     _|  |_|  |    ___|                                            
  |   | |       |   |___                                             
  |   | |       |    ___|                                            
  |   | |   _   |   |___                                             
 _______|_______|________ _______ _______ __   __ ______   _______   
|       |    _ | |       |   _   |       |  | |  |    _ | |       |  
|_     _|   | || |    ___|  |_|  |  _____|  | |  |   | || |    ___|  
  |   | |   |_||_|   |___|       | |_____|  |_|  |   |_||_|   |___   
  |   | |    __  |    ___|       |_____  |       |    __  |    ___|  
  |   | |   |  | |   |___|   _   |_____| |       |   |  | |   |___   
 _______|___| ___________________________|_______|___|  |_|_______|  
|       |  | |  |       |       |       |                            
|   _   |  | |  |    ___|  _____|_     _|                            
|  | |  |  |_|  |   |___| |_____  |   |                              
|  |_|  |       |    ___|_____  | |   |                              
|      ||       |   |___ _____| | |   |                              
|____||_|_______|_______|_______| |___|                             
'''

# Introduction function
def intro(name):
    print(intro_art)
    print(f"Welcome to the Treasure Quest, {name}!")
    print("Your goal is to find the hidden treasure in the Lost Forest.")
    print("Your health is 50, it represents your ability to survive. If it drops to 0, you lose.")
    print("Make wise decisions, as your health will affect the outcome of your journey!")
    print("Good luck!\n")

# Random event function
def random_event(score):
    event_outcome = random.choice(["gain", "lose"])
    points = random.randint(5, 15)
    if event_outcome == "gain":
        print(f"Lucky you! You gain {points} health points.\n")
        return score + points
    else:
        print(f"Unfortunate! You lose {points} health points.\n")
        return max(score - points, 0)

# Game section function
def game_section(path, score):
    print(f"You chose the {path} path. Let's see where it leads...\n")
    
    # First decision in the section
    choice1 = input("You encounter a fork. Do you go 'left' or 'right'? (left/right): ").lower()
    if choice1 == "left":
        print("You find a sparkling stream with fresh water.")
        score = random_event(score)
    elif choice1 == "right":
        print("You find an old bridge that looks unstable.")
        score = random_event(score)
    else:
        print("Invalid choice. You lose 5 health points for hesitating.\n")
        score = max(score - 5, 0)

    if score == 0:
        print("You are too weak to continue your journey. Game over!")
        exit()

    # Second decision in the section
    choice2 = input("You hear rustling nearby. Do you 'investigate' or 'ignore' it? (investigate/ignore): ").lower()
    if choice2 == "investigate":
        print("You find a hidden stash of supplies!")
        score = random_event(score)
    elif choice2 == "ignore":
        print("You cautiously move on, avoiding potential danger.")
        score = random_event(score)
    else:
        print("Invalid choice. You lose 5 health points for indecision.\n")
        score = max(score - 5, 0)

    if score == 0:
        print("You are too weak to continue your journey. Game over!")
        exit()

    # Third decision in the section
    choice3 = input("You see a cave ahead. Do you 'enter' it or 'walk past'? (enter/walk past): ").lower()
    if choice3 == "enter":
        print("The cave contains ancient carvings and a treasure map!")
        score = random_event(score)
    elif choice3 == "walk past":
        print("You avoid the cave but find a hidden path leading deeper into the forest.")
        score = random_event(score)
    else:
        print("Invalid choice. You lose 5 health points for hesitation.\n")
        score = max(score - 5, 0)

    if score == 0:
        print("You are too weak to continue your journey. Game over!")
        exit()

    return score

# Main game function
def main():
    name = input("What is your name?: ")
    main_menu()
    intro(name)
    score = 50  # Starting health

    # First path choice
    path = input("Do you choose the 'well-traveled' or 'overgrown' path? (well-traveled/overgrown): ").lower()
    if path == "well-traveled":
        score = game_section("well-traveled", score)
    elif path == "overgrown":
        score = game_section("overgrown", score)
    else:
        print("Invalid choice. You stumble and lose 10 health points.\n")
        score = max(score - 10, 0)

    if score == 0:
        print("You are too weak to continue your journey. Game over!")
        exit()

    # Final decision
    print("You reach the heart of the forest and find a locked chest.")
    final_choice = input("Do you 'open' the chest or 'leave' it? (open/leave): ").lower()
    if final_choice == "open":
        if score >= 60:
            print("Congratulations! Your health and perseverance have paid off. You find the treasure and win!")
        else:
            print("You lack the strength to open the chest. The treasure remains hidden.")
    elif final_choice == "leave":
        print("You decide to leave the chest and end your journey with your health intact.")
    else:
        print("Invalid choice. You lose 5 health points for indecision.\n")
        score = max(score - 5, 0)

    print(f"Your final health is {score}. Thanks for playing!")

# Main menu function
def main_menu():
    while True:
        print("Main Menu:")
        print("1. Start Game")
        print("2. Quit")
        choice = input("Enter your choice (1 to start, 2 to quit): ")
        
        if choice == '1':
            return  # Exit the loop and start the game
        elif choice == '2':
            print("Thanks for playing! Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.\n")

# Start the game
if __name__ == "__main__":
    main()