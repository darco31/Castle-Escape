# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


# Creator: Stephen Darcy
# Date:
# Project 3 - The code Institute
import time

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


TIME_ELAPSED = 2


def start():
    """
    Starts the game, gives a narrative to set the scene and asks
    if the player would like to play or not.
    """
    print(Fore.RED + Back.YELLOW + Style.BRIGHT + 
                    "\n The Great Castle Escape\n")
    time.sleep(TIME_ELAPSED)
    print(Fore.CYAN + '''
                                     T~~
                                     |
                                     /"\\
                             T~~     |'| T~~
                         T~~ |    T~ WWWW|
                         |  /"\   |  |  |/\T~~
                         /"\ WWW  /"\ |' |WW|
                         WWWWW/\| /   \|'/\|/"\\
                         |   /__\/]WWW[\/__\WWWW
                         |"  WWWW'|I_I|'WWWW'  |
                         |   |' |/  -  \|' |'  |
                         |'  |  |LI=H=LI|' |   |
                         |   |' | |[_]| |  |'  |
                         |   |  |_|###|_|  |   |
                         '---'--'-/___\-'--'---'
                     \n
                        Can you escape the castle!\n''')
    while True:
        # set P_NAME to a global variable.
        global P_NAME
        P_NAME = input("Please enter a username: \n")
        print()
        if P_NAME == "":
            print("You need to enter a username to continue...\n")
            continue
        else:
            break

    print(f"Welcome {P_NAME}, good luck!\n\n")
    print("\n You awake a little dazed and confused.")
    time.sleep(TIME_ELAPSED)
    print("\n You can vaguely hear rain crashing down on a tiled roof.")
    time.sleep(TIME_ELAPSED)
    print("\n The sound of thunder rings in the air.")
    time.sleep(TIME_ELAPSED)
    print("\n As your senses come back you try to recall the past few hours,\
but everything is hazy.")
    time.sleep(TIME_ELAPSED)
    print("\n As you look around your surroundings you appear to be in a room \
with")
    print("\n a large wooden door and a small window on one side of the room.")
    print("\n The walls are stone and look damp.") 
    time.sleep(TIME_ELAPSED)

    print("\n So do you have the guts to try and escape? (y or n) ")
    # convert the player's input to lower_case
    answer = input("> \n").lower().strip()
    if answer == "y":
        # player approches the small window
        small_window()
    elif answer == "n":
        # take player to play_again()

        print("\n Shame")
        time.sleep(TIME_ELAPSED)
        print("\n Enjoy the solitude and loniness of the tower")
        play_again()
    else:
        # else return player to start()
        start()


def small_window():
    """
    The users initial options in the game, go to window
    or use the door
    """
    print("\n You get up and walk towards the window.")
    time.sleep(TIME_ELAPSED)
    print("\n You peer out and can only see darkness")
    time.sleep(TIME_ELAPSED)
    print("\n Will you try open the window (y or n)")

    window = input("> \n").lower().strip()

    if window == "y":
        print("\n The window is sealed shut \
and doesnt budge so you head \
towards the door")
        time.sleep(TIME_ELAPSED)
        large_door()
    elif window == "n":
        print("\n You ignore the window,turn and head for the door")
        large_door()


def large_door():
    """
    User approches the large door in the first room and \

    """
    print("\n You walk towards the door and \
try the handle, to your surprise it opens")
    print("\n Do you proceed through the door?")

    proceed = input("> \n").lower().strip()

    if proceed == "y":
        print("\n You step tentiviely through \
the door and peer from side to side")
        print("\n You can make out two more doors at either end of the hall")
        print("\n There is a table with a drawer to your left")
        print("\n Do you check the drawer? (y or n) ")

        drawer = input("> \n").lower()

        if drawer == "y":
            print("\n You pull at the drawr and it opens, inside is a key and\
 a small knife")
        take_items()

    else:
        print("\n You close the drawer and move on")


def take_items():
    """
    Options for the user to take the items from the drawer
    """
    print("\n You you pick up the items from the drawer? (y or n)")

    pick_items = input("> \n").lower().strip()

    if pick_items == "y":
        print("\n You reach in and pick up both items and \
place them in your pockets. Maybe you can use the knife \
to open the window?")
        back_to_window()
    else:
        print("\n You shut the drawer silently and move on")


def back_to_window():
    """
    Returns the player to the first room with the sealed window"
    """
    print("Back in the first room")

    print("\n You look out the window again and decide its safe")
    print("\n Do you try the window with the knife? (y or n)")

    open_window = input("> \n").lower().strip()

    if open_window == "y":
        print("\n You jam the knife into the gap[ of the window pain \
the timber comes loose and the window pops open \
Success, you climb up and out side")
        print("\n You peer down through the dark and the rain and can just make \
out the sloping roof. You jump and to your horror the tile \
gives way and you fall to your death.")

        print(Fore.RED + '''
  ╔╗           ╔╗
  ║║           ║║
╔═╝║╔══╗╔══╗ ╔═╝║
║╔╗║║╔╗║╚ ╗║ ║╔╗║
║╚╝║║║═╣║╚╝╚╗║╚╝║
╚══╝╚══╝╚═══╝╚══╝
                 
            ''')     
        play_again()

    else:
        print("\n You jam the knife into the gap of the window pain \
the timber comes loose and the window pops open \
Success, but")
        
        print("\n Looking down into thte dark bleak night \
you decide its best not to try jump and make your \
way back inside")
        return_inside()


def return_inside():

    print("\n Ahhh I am back where I started. You head back out \
the large door and go left. ")
    time.sleep(TIME_ELAPSED)
    print("\n You approach the door at the left end of the corridor \
It creaks open and you peer inside, the room is lit only by a single \
candle. There doesnt appear to be anybody in the room so you \
proceed inside. Directley in front of you is an opening \
with what looks like a stairs going down.")
    time.sleep(TIME_ELAPSED)
    print("\n Do you proceed down the stairs, explore the room or turn back? \
(proceed or explore or tuen back)")
    decsion = input("> \n").lower().strip()
    if decsion == "explore":
        explore_room()
    elif decsion == "proceed":
        print("\n You decide to head down the stairs")
    else:
        print("\n You turn around and head back for the other door")


def explore_room():
    """
    Player desides to either explore this room or move doen the stairs
    that are in the room
    """
    print("\n As you look around the room you see some fruit in a \
bowl, you pick it up and eat fast while contiuing t o explore")
    time.sleep(TIME_ELAPSED)
    print("\n You see an old belt which you think will come in handy \
so you pick it up put it on and tuck the knife into it.")


def play_again():
    """
    Asks the player is they would like to play again
    """
    print("\n DO YOU WANT TO PLAY AGAIN (y or n)")
    # convert the player's input to lower_case
    answer = input("> \n").lower().strip()
    if answer == "y":
        # take player to start()
        start()
    elif answer == "n":
        # exit() the program
        print("\n Sorry to see you go")
        print("\n Please come back again")
        exit()
    else:
        # return to start()
        start()


start()
