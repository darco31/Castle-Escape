from functions import P_STAT


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
    print(Fore.RED + Back.YELLOW + Style.BRIGHT + "\nThe Great Castle \
Escape\n")
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
        P_NAME = input("\nPlease enter a username: \n")
        print()
        if P_NAME == "":
            print("You need to enter a username to continue...\n")
            continue
        else:
            break

    P_STAT(f"\n Welcome {P_NAME}, good luck!\n", 2)
    P_STAT("\n You awake a little dazed and confused.", 2)
    P_STAT("\n You can vaguely hear rain crashing down on a tiled roof.", 2)
    P_STAT("\n The sound of thunder rings in the air.", 2)
    P_STAT("\n As your senses come back you try to recall the past ", 2)
    P_STAT("\n few hours,but everything is hazy.", 2)
    P_STAT("\n As you look around your surroundings ", 2)
    P_STAT("\n you appear to be in a room with", 2)
    P_STAT("\n a large wooden door and a small window on one ", 2)
    P_STAT("\n side of the room. The walls are stone and look damp.", 2)
    P_STAT("\n So do you have the guts to try and escape? (y or n) ", 1)
    # convert the player's input to lower_case
    answer = input("> \n").lower().strip()
    if answer == "y" or answer == 'yes':
        # player approches the small window
        small_window()
    elif answer == "n" or answer == 'no':
        # take player to play_again()
        P_STAT("\n Shame", 2)
        P_STAT(f"\n Enjoy the solitude and loniness of the tower {P_NAME}", 2)
        play_again()
    else:
        # else return player to start()
        start()


def small_window():
    """
    The users initial options in the game, go to window
    or use the door
    """
    P_STAT("\n You get up and walk towards the window.", 2)
    P_STAT("\n You peer out and can only see darkness", 2)
    P_STAT("\n Will you try open the window (Y or N)", 1)

    window_open = input("> \n").lower().strip()
    if window_open == "y":
        P_STAT("\n The window is sealed shut and ", 2)
        P_STAT("\n doesnt budge so you head towards the door", 2)
        large_door()
    elif window_open == "n":
        P_STAT("\n You ignore the window", 2)
        large_door()


def large_door():
    """
    User approches the large door in the first room and
    will decide to go either left or right
    """
    P_STAT("\n You walk towards the door and", 2)
    P_STAT("\n try the handle, to your surprise it opens", 2)
    P_STAT("\n Do you proceed through the door? (Y or N)", 1)

    proceed = input("> \n").lower().strip()

    if proceed == "y" or proceed == "yes":
        P_STAT("\n You step tentiviely through", 2)
        P_STAT("\n the door and peer from side to side", 2)
        P_STAT("\n You make out two more doors at either end of the hall", 2)
        P_STAT("\n There is a table with a drawer to your left", 2)
        P_STAT("\n Do you check the drawer? (Y or N) ", 1)

        drawer = input("> \n").lower()

        if drawer == "y" or drawer == "yes":
            P_STAT("\n You pull at the drawer and it opens,", 1)
            P_STAT("\n inside is a key and a small knife", 1)
        take_items()

    else:
        print("\n You move on")
        direction_choice()


def take_items():
    """
    Options for the user to take the items from the drawer
    """
    P_STAT("\n You you pick up the items from the drawer? (Y or N)", 1)
    pick_items = input("> \n").lower().strip()
    if pick_items == "y" or pick_items == "yes":
        P_STAT("\n You reach in and pick up both items and", 2)
        P_STAT("\n place them in your pockets. Maybe you can use the knife", 2)
        P_STAT("\n to open the window?", 2)
        back_to_window()
    else:
        print("\n You shut the drawer silently and move on")
        direction_choice()


def back_to_window():
    """
    Returns the player to the first room with the sealed window"
    """
    P_STAT(Fore.RED + "\n You return to the first room", 3)

    P_STAT("\n You look out the window again", 2)
    P_STAT("\n Do you try the window with the knife? (Y or N)", 1)

    open_window = input("> \n").lower().strip()

    if open_window == "y" or open_window == "yes":
        P_STAT("\n You jam the knife into the gap of the window pain", 2)
        P_STAT("\n the timber comes loose and the window pops open", 2)
        P_STAT("\n Success, you climb up and out side", 2)
        P_STAT("\n You peer through the dark and the rain and can just", 2)
        P_STAT("\n make out the sloping roof. You jump and to your horror ", 2)
        P_STAT("\n the tile gives way and you fall to your death.", 3)

        P_STAT(Fore.RED + '''
                              ??????           ??????
                              ??????           ??????
                            ???????????????????????????????????? ????????????
                            ??????????????????????????? ?????? ????????????
                            ???????????????????????????????????????????????????
                            ???????????????????????????????????????????????????

            ''', 2)
        play_again()

    else:
        P_STAT("\n Looking down into the dark bleak night", 2)
        P_STAT("\n you decide its best not to try and make your", 2)
        P_STAT("\n way back to the large door", 2)
        direction_choice()


def direction_choice():
    """
    Player to choose weather to go left or right
    """
    P_STAT("\n Standing in the doorway you need to make a choice", 2)
    P_STAT("\n Left or Right", 1)
    
    player_choice = input("> \n").lower().strip()

    if player_choice == "left":
        go_left()
    else:
        go_right()


def go_left():
    """
    The user goes back to the large door in the first room
    """

    P_STAT("\n You head back out the large door and go left. ", 2)
    P_STAT("\n You approach the door at the left end of the corridor", 2)
    P_STAT("\n It creaks open and you peer inside, ", 2)
    P_STAT("\n the room is lit only by a single", 2)
    P_STAT("\n candle. There doesnt appear to be anybody in the room ", 2)
    P_STAT("\n so you proceed inside. Directley in front of you is", 2)
    P_STAT("\n an opening with what looks like a stairs going down.", 2)
    P_STAT("\n Do you go down the stairs, explore the room or turn back?", 2)
    P_STAT("\n Proceed or Explore or Turn Back?", 1)

    decsion = input("> \n").lower().strip()
    if decsion == "explore":
        explore_room()
    elif decsion == "proceed":
        proceed_down_stairs()
    else:
        P_STAT("\n You turn around and head back for the other door", 2)
        go_right()


def proceed_down_stairs():
    """
    Player goes down the stairs
    """
    P_STAT("\n You proceed towards the door", 2)
    P_STAT("\n Huggin the wall you sneak down the stairs", 2)
    P_STAT("\n At the bottom you are in a well lit room", 2)
    P_STAT("\n You listen intently, you can hear voices", 2)
    P_STAT("\n You peek around the corner and there are two men with", 2)
    P_STAT("\n swords? SWORDS? Where am I you think", 2)

    P_STAT("\n The backs are to you", 2)
    P_STAT("\n Do you attack or try sneak past", 2)

    attack_men = input("> \n").lower().strip()
    if attack_men == "attack":
        P_STAT("\n You charge at the two men who are surprised", 2)
        P_STAT("\n One swipe of the sword and you are ......", 2)
        P_STAT(Fore.RED + '''
                              ??????           ??????
                              ??????           ??????
                            ???????????????????????????????????? ????????????
                            ??????????????????????????? ?????? ????????????
                            ???????????????????????????????????????????????????
                            ???????????????????????????????????????????????????

            ''', 2)
        play_again()
    else:
        P_STAT("\n You put your back against the wall and", 2)
        P_STAT("\n snaek as quitely as you can past the two men", 2)


def explore_room():
    """
    Player decides to either explore this room or move doen the stairs
    that are in the room
    """
    P_STAT("\n As you look around the room you see some fruit in a", 2)
    P_STAT("\n bowl, you pick it up and eat fast while exploring", 2)
    P_STAT("\n You see an old belt which you think will come in handy", 2)
    P_STAT("\n so you pick it up put it on and tuck the knife into it.", 2)

    proceed_down_stairs()


def go_right():
    """
    PLayer decides to go to the right hand door
    """
    P_STAT("\n You head toward the door", 2)
    P_STAT("\n You try the door, it is locked", 2)
    P_STAT("\n You remember the key and try that, it opens", 2)
    P_STAT("\n You open the door and enter the room", 2)
    P_STAT("\n Looking around you notice 3 levers on the wall", 2)
    P_STAT("\n Do you try the levers? (Y or N", 1)

    try_lever = input("> \n").lower().strip()

    if try_lever == "y" or try_lever == "yes":
        P_STAT("\n You try the first lever, nothing happens", 2)
        P_STAT("\n Maybe its a combination of the levers", 2)
        P_STAT("\n Worth a go? (Y or N)", 2)
        
    try_combo = input("> \n").lower().strip()
    P_STAT("\n Which levers will you pick (1,2,3)", 2)
    

    if try_combo == "y" or try_combo == "yes":
        user = [1, 2, 3]
        if user == 1 and 2:
            pass
        else:
            P_STAT(Fore.RED + '''
                              ??????           ??????
                              ??????           ??????
                            ???????????????????????????????????? ????????????
                            ??????????????????????????? ?????? ????????????
                            ???????????????????????????????????????????????????
                            ???????????????????????????????????????????????????

            ''', 2)
        play_again()


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
        print(f"\n Sorry to see you go {P_NAME}")
        print("\n Please come back again")
        exit()
    else:
        # return to start()
        start()


start()
