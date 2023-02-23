from random import choice
from time import sleep
import emoji 


def show_who_win(choice_by_pc):
    print(f"You win!!! i chose {emoji_pc(choice_by_pc)}, and you {emoji_player(player_choice)}.")

def show_who_lose(choice_by_pc):
    print(f"You lose!! i chose {emoji_pc(choice_by_pc)}, and you {emoji_player(player_choice)}.")

def emoji_pc(choice_by_pc):
    match(choice_by_pc):
        case "rock":
            return emoji.emojize(":right-facing_fist:")
        case "paper":
            return emoji.emojize(":hand_with_fingers_splayed:")
        case "scissor":
            return emoji.emojize( ":vulcan_salute:")

def emoji_player(player_choice):
    if player_choice == "rock":
        return(emoji.emojize(":right-facing_fist:"))
    elif player_choice == "paper":
        return(emoji.emojize(":hand_with_fingers_splayed:"))
    elif player_choice == "scissor":
        return(emoji.emojize(":vulcan_salute:"))

possibilities_to_choose = ["rock", "paper", "scissor"]

choice_by_pc = ""
player_choice = str("")

while player_choice != "end":
    
    choice_by_pc = choice(possibilities_to_choose)
    print(choice_by_pc)
    player_choice = str(input("pick one! rock, paper or scissor ")).lower().strip("")

    print("="*20 + "Joquempo" + "="*20)
    sleep(1)

    match(choice_by_pc, player_choice):
        case["rock", "scissor"]:
            show_who_lose(choice_by_pc)        
        case["paper", "rock"]:
            show_who_lose(choice_by_pc)
        case["scissor", "paper"]:
            show_who_lose(choice_by_pc)
        case["rock", "paper"]:
            show_who_win(choice_by_pc)
        case["paper", "scissor"]:
            show_who_win(choice_by_pc)
        case["scissor", "rock"]:
            show_who_win(choice_by_pc)
        case[_, _]:
            print(f"We have a draw!!! I chose {emoji_pc(choice_by_pc)}, and you too!")
