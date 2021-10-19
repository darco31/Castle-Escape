# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


# Creator: Stephen Darcy
# Date:
# Project 3 - The code Institute


import time

TIME_ELAPSED = 2

print("""
      pass
     """)


def start():
    """
    Satrts the game, gives a narrative to set the scene and asks
    if the player would like to play or not.
    """
    print("\n The Great Castle Escape\n")

    print("\n You awake a little dazed and confused.")
    time.sleep(TIME_ELAPSED)
    print("\n You can vaguely hear rain crashing down on a tiled roof.")
    time.sleep(TIME_ELAPSED)
    print("\n The sound of thunder rings in the air.")
    time.sleep(TIME_ELAPSED)
    print("\n As your senses come back you try to recall the past few hours, \
but everything is hazy.")
    time.sleep(TIME_ELAPSED)
    print("\n As you look around your surroundings \
you appear to be in a room \
with just a large wooden door and a \
mall window on one side of the room. \
The walls are stone and look damp.")
    time.sleep(TIME_ELAPSED)

    print("\n So do you have the guts to try and escape? (y or n) ")
    # convert the player's input to lower_case
    answer = input(">").lower()
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
    print("\n Will you try open the window")

    window = input(">").lower()

    if window == "y":
        print("\n The window is sealed shut \
and doesnt budge so you head \
towards the door")
        large_door()
    elif window == "n":
        print("\n You ignore the window,turn and head for the door")


def large_door():
    """
    User approches the large door in the first room and \

    """
    print("\n You walk towards the door and \
try the handle, to your surprise it opens")
    print("\n Do you proceed through the door?")

    proceed = input(">").lower()

    if proceed == "y":
        print("\n You step tentiviely through \
the door and peer from side to side")
        print("\n You can make out two more doors at either end of the hall")
        print("\n There is a table with a drawer to your left")
        print("\n Do you check the drawer? (y or n) ")

        drawer = input(">").lower()

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
    print("\n You you pick up the items from the drawer? (y or n")

    pick_items = input(">").lower()

    if pick_items == "y":
        print("\n You reach in and pick up both items and \
place them in your pockets")
    else:
        print("\n You shut the drawer silently")


def play_again():
    """
    Asks the player is they would like to play again
    """
    print("\n DO YOU WANT TO PLAY AGAIN (y or n)")
    # convert the player's input to lower_case
    answer = input(">").lower()
    if answer == "y":
        # take player to start()
        start()
    elif answer == "n":
        # exit() the program
        print("\n Sorry to see you go")
        print("\n Granny hopes you will return")
        exit()
    else:
        # return to start()
        start()


start()
