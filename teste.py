import emoji 
from random import choice
from time import sleep

def show_the_result(win=0, lose=0):
    """This function shows the results of the game, printing the result of the choices by computer
    and player.
    Attention, this function needs to be accompained by the choices_to_emojis function.

    Exemple:
        when 'whin' parameter receives number 1, the function print that the play is winner.
        However the parameter lose receive the number 1, the it'll print the computer(PC) is the winner.

    Args:
        win (str): parameter from match comparison.
        lose (str): parameter from match comparison.

    Return: 
        no returns.
        
    """
    if win == 1:
        print(f"You win!!! i chose {choices_to_emoji(choice_by_pc)}, and you {choices_to_emoji(player_choice)}.")
    if lose == 1:
        print(f"You lose!! i chose {choices_to_emoji(choice_by_pc)}, and you {choices_to_emoji(player_choice)}.")


def choices_to_emoji(choice):
    """This function returns the emojis to be used to show them.

    Exemple:
        if it's receive the 'rock' word it'll retunr ':right-facing_fist:' and with the emojize's
        function help it's shows the punch emoji.

    Args:
        choice (str): receive the argument from input or random lists.

    returns:
        Retuns the usable emoji[punsh, high-five hand and vulcan salute from emoji library] to put
        in any print or frame.
    """
    match(choice):
        case "rock":
            return emoji.emojize(":right-facing_fist:")
        case "paper":
            return emoji.emojize(":hand_with_fingers_splayed:")
        case "scissor":
            return emoji.emojize( ":vulcan_salute:")
            

possibilities_to_choose = ["rock", "paper", "scissor"]

while player_choice:="" != "end":
    choice_by_pc = choice(possibilities_to_choose)
    player_choice = str(input("pick one! rock, paper or scissor ")).lower().strip("")
    print("="*20 + "Joquempo" + "="*20)
    sleep(1)
    if player_choice not in possibilities_to_choose:
        print("You need to chose right, the possibilties are: rock, pape or scissor")
        continue
    
    match(choice_by_pc, player_choice):
        case["rock", "scissor"]:
            show_the_result(lose=1)        
        case["paper", "rock"]:
            show_the_result(lose=1)
        case["scissor", "paper"]:
            show_the_result(lose=1)
        case["rock", "paper"]:
            show_the_result(win=1)
        case["paper", "scissor"]:
            show_the_result(win=1)
        case["scissor", "rock"]:
            show_the_result(win=1)
        case[_, _]:
            print(f"We have a draw!!! I chose {choices_to_emoji(choice_by_pc)}, and you too!")
        
