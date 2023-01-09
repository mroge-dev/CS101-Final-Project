# Title: Aphid's Revenge - A Text based Adventure Game
# Name: Michael Rogers
# Date: 1/8/2023
# This game was started as a project in my first programming class. I made a few updates and corrections to use it for the CS101 final project in Codecademy.

# display game title and instructions to the user
def show_instructions():
    print('Aphid\'s Revenge: A Text Adventure Game')
    print('\nCollect 6 items to win the game, or be slain by the Queen of the Ants.')
    print('\nTo move through the Anthill use the following commands: go South, go North, go East, go West')
    print('To add an item to the inventory use the command: get \'item name\', where the item is shown in status message.')
    #print('\nTo display the map, type the command: map')
    print('\nTo end the game, type the command: quit')
    print('\nCommands must be typed exactly or an error will occur.')
    print('\n\nA map for the Queen\'s Anthill is show below.\n')

# displays map
def show_map():
    print('*****************************************************************')
    print('*                                                               *')
    print('*            Soldier Qtrs   <--> Ant Armory  --> Queen\'s Lair   *')
    print('*                   |                |                          *')
    print('*    Shaft <--> Main Tunnel <--> Colony Detritus                *')
    print('*                   |                |                          *')
    print('*            Worker Qtrs    <--> Aphid Farm                     *')
    print('*                                                               *')
    print('*****************************************************************')


# function that outputs the player's status
def show_player_status(current_room, inventory, rooms):
    # display the player's current location
    print('\nYou are in the', current_room)
    # display the player's inventory
    print('Inventory: ', inventory)
    # references dictionary rooms to get inventory value of current room
    if 'item' in rooms[current_room]:
        current_item = rooms[current_room].get('item')
        if current_item not in inventory:
            print('You see the {}'.format(current_item))


# Lose condition message- Game Over
def you_lose_message():
    lose_message = """
                        You have entered the Queen's Lair unprepared.\n
                        The Queen easily avoids your feeble attacks and rips through your inadequate defenses.\n
                        \nYou have been slain by the Queen of the Ants.\n
                        \nThanks for playing Aphid's Revenge. Hope you enjoyed it."""
    return lose_message


# Win condition message - Winner
def you_win_message():
    victory_message = """
                        You enter the Queen's Lair undetected due to the effects of your handy Ant Pheromone Cloak.\n 
                        You throw a Honeydew Grenade to confuse and disorient the Queen while you swing your Hornet Stinger Glaive and draw first blood.\n
                        The Queen quickly recovers and attacks viciously. However, your Beetle Armor soaks up the majority of the damage.\n
                        You know you cannot take much more. You blow the Oogpister Beetle Whistle.\n
                        Your Oogpister Beetle bursts into the lair and attacks the Queen.\n
                        With the Queen distracted, you move in with all your Aphid strength and behead the Queen with your Praying Mantis Greatsword.\n
                        The headless Queen flails around frantically as her head rolls toward the Oogpister Beetle, who immediately unleashes a bombardment of corrosive acid, dissolving the Queen's severed head.\n
                        The Queen's body falls to the ground, lifeless.\n
                        \nYou have slain the Queen of the Ants.\n
                        \nThanks for playing Aphid's Revenge. Hope you enjoyed it."""
    return victory_message


def main():
    # define an inventory, which starts with zero items
    inventory = []

    # define a dictionary that links the direction of rooms to the other rooms and also contains the item in room
    rooms = {
        'Secret Entrance Shaft': {'East': 'Main Tunnel'},
        'Main Tunnel': {'North': 'Soldier Quarters', 'East': 'Colony Detritus', 'South': 'Worker Quarters',
                        'West': 'Secret Entrance Shaft', 'item': 'Ant Pheromone Cloak'},
        'Worker Quarters': {'North': 'Main Tunnel', 'East': 'Aphid Farm', 'item': 'Oogpister Beetle Whistle'},
        'Soldier Quarters': {'East': 'Ant Armory', 'South': 'Main Tunnel', 'item': 'Hornet Stinger Glaive'},
        'Colony Detritus': {'North': 'Ant Armory', 'South': 'Aphid Farm', 'West': 'Main Tunnel',
                            'item': 'Beetle Armor'},
        'Aphid Farm': {'North': 'Colony Detritus', 'West': 'Worker Quarters', 'item': 'Honeydew Grenades'},
        'Ant Armory': {'East': 'Queen\'s Lair', 'South': 'Colony Detritus', 'West': 'Soldier Quarters',
                       'item': 'Praying Mantis Greatsword'},
        'Queen\'s Lair': {'West': 'Ant Armory', 'item': 'Queen of the Ants'},
    }

    # Place player in start room
    current_room = 'Secret Entrance Shaft'

    # Show Game Instructions and map to Player
    show_instructions()
    show_map()

    # loop till win or loss conditions met
    while True:

        # get player status and return current item to check victory conditions
        show_player_status(current_room, inventory, rooms)

        # Has the player finished the game (Win or Lose)
        # conditional to exit while loop if item in room is Queen of the Ants
        if current_room == 'Queen\'s Lair':
            if len(inventory) < 6:
                # print losing message
                print(you_lose_message())
                break
            else:
                # conditional to exit while loop when player collects all items
                # print winning message
                print(you_win_message())
                break

        # a graphical divider for input and player command
        print('-' * 35)
        # Get commands from player
        user_input = input('Enter your move:\n')

        # quit game
        if user_input == 'quit':
            quit()

        #if user_input =='map':
        #    show_map()

        # validate that user input has two words and if not print error message
        check_user_input = user_input.split()

        if len(check_user_input) < 2:
            print(
                'Invalid input! Action commands require two words. Please refer to game instructions for proper input.')
            continue

        # splits user input into action and command
        # Action command is "Go [direction]"
        action, command = user_input.split(" ", 1)
        if (action == 'go') and (
                command == 'North' or command == 'South' or command == 'East' or command == 'West'):
            # Test for the existence of a key in rooms dictionary
            # Assign current room to value of the direction key
            if command in rooms[current_room]:
                current_room = rooms[current_room][command]
            else:
                print('You can\'t go that way!')
        # Action command starts with 'get'
        elif action == 'get':
            room_item = rooms[current_room].get('item')
            if room_item == command:
                # check if the same item in inventory
                if room_item in inventory:
                    print('You already have that item!. Please enter next action.')
                # append new item to inventory
                else:
                    inventory.append(room_item)
                    print('{} retrieved!'.format(room_item))
            else:
                print('Can\'t get {}!'.format(command))
        # Else the action is invalid
        else:
            # print an error message
            print('Invalid Action! Please see instructions at beginning of game for valid actions.')


# calls the main function for gameplay
main()
