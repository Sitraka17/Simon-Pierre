import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_choice(options):
    while True:
        choice = input("Enter your choice (1 or 2): ").strip()
        if choice in options:
            return choice
        else:
            print("Invalid choice. Please enter 1 or 2.")

def scene_1():
    clear_screen()
    slow_print("Welcome to the Text-based Adventure Game: Peter and Jesus")
    slow_print("In this game, you will make choices that affect the outcome.")
    slow_print("Let's begin...")
    slow_print("\n--- Scene 1 ---")
    slow_print("You are Peter, standing by the Sea of Galilee. Jesus approaches you.")
    slow_print("Jesus: 'Peter, do you trust me?'")
    slow_print("1. 'Yes, Lord, I trust you.'")
    slow_print("2. 'I have doubts, Lord.'")
    choice = get_choice(['1', '2'])
    if choice == '1':
        scene_2_trust()
    else:
        scene_2_doubt()

def scene_2_trust():
    clear_screen()
    slow_print("\n--- Scene 2 ---")
    slow_print("Jesus: 'Good, Peter. Your trust will guide you through the storms of life.'")
    slow_print("A storm begins to brew on the sea.")
    slow_print("Jesus: 'Peter, come to me on the water.'")
    slow_print("1. Step out of the boat and walk on the water.")
    slow_print("2. Stay in the boat and wait for the storm to pass.")
    choice = get_choice(['1', '2'])
    if choice == '1':
        scene_3_trust_walk()
    else:
        scene_3_trust_wait()

def scene_2_doubt():
    clear_screen()
    slow_print("\n--- Scene 2 ---")
    slow_print("Jesus: 'Peter, doubt can be a heavy burden. Trust in me and you will find peace.'")
    slow_print("A storm begins to brew on the sea.")
    slow_print("Jesus: 'Peter, come to me on the water.'")
    slow_print("1. Step out of the boat and walk on the water.")
    slow_print("2. Stay in the boat and wait for the storm to pass.")
    choice = get_choice(['1', '2'])
    if choice == '1':
        scene_3_doubt_walk()
    else:
        scene_3_doubt_wait()

def scene_3_trust_walk():
    clear_screen()
    slow_print("\n--- Scene 3 ---")
    slow_print("You step out of the boat and begin to walk on the water towards Jesus.")
    slow_print("Jesus: 'Well done, Peter. Your faith is strong.'")
    slow_print("You reach Jesus and the storm calms.")
    moral_message("Trust and faith can help you overcome any obstacle.")

def scene_3_trust_wait():
    clear_screen()
    slow_print("\n--- Scene 3 ---")
    slow_print("You stay in the boat and wait for the storm to pass.")
    slow_print("Jesus: 'Peter, sometimes patience is also a virtue.'")
    slow_print("The storm eventually calms and you reach Jesus safely.")
    moral_message("Patience and trust go hand in hand in navigating life's challenges.")

def scene_3_doubt_walk():
    clear_screen()
    slow_print("\n--- Scene 3 ---")
    slow_print("You step out of the boat but begin to sink as doubt fills your mind.")
    slow_print("Jesus: 'Peter, why did you doubt?'")
    slow_print("Jesus reaches out and saves you from the water.")
    moral_message("Doubt can hold you back, but trust can lift you up.")

def scene_3_doubt_wait():
    clear_screen()
    slow_print("\n--- Scene 3 ---")
    slow_print("You stay in the boat, gripped by doubt.")
    slow_print("Jesus: 'Peter, it is okay to have doubts, but do not let them consume you.'")
    slow_print("The storm eventually calms and you reach Jesus safely.")
    moral_message("Even in doubt, there is hope. Trust can guide you through uncertainty.")

def moral_message(message):
    slow_print("\n--- Moral Message ---")
    slow_print(message)
    slow_print("Thank you for playing. Remember, trust and faith can guide you through life's challenges.")
    slow_print("Would you like to play again? (yes/no)")
    play_again = input().strip().lower()
    if play_again == 'yes':
        main()
    else:
        slow_print("Goodbye!")

def main():
    clear_screen()
    slow_print("Welcome to the Text-based Adventure Game: Peter and Jesus")
    slow_print("In this game, you will make choices that affect the outcome.")
    slow_print("Let's begin...")
    scene_1()

if __name__ == "__main__":
    main()
