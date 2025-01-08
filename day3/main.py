print(r'''

                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where go you want to go? Type "left" or "right"').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake.'
                    ' type"wait" to wait for a boat.'
                    ' Type "swim" to swim across ').lower()
    if choice2 == "wait":
        choice3 = input('you arrive at the island unharmed. '
                        'There is house with three doors. '
                        'One red, One yellow and one blue.')
        if choice3 == "red":
            print("it is a room full of fire. Game over.")
        elif choice3 == "yellow":
            print("you found the treasure. You win!")
        elif choice3 == "blue":
            print("you entered a room full of beasts.Game Over.")
        else:
            print("you chose a door that does not exist.Game Over.")
else:
    print("You fell into a hole.Game Over.")
