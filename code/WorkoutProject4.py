"""
This module is the main entry point for the NASA Image Viewer
application. It provides a user interface for the user to choose between
viewing images from the Mars Rover or the Earth Polychromatic Imaging Camera.
"""


from marsrover import runmarsrover
from earth import runearthimg


def main():
    ''' Main function to run the program. It prompts the
        user to choose an API to view images from.
    '''
    while True:
        user_input = input("Welcome to the NASA Image Viewer!\n"
                           "To view images from the Mars Rover, enter "
                           "'Mars'.\nTo view images from the Earth "
                           "Polychromatic Imaging Camera, "
                           "enter 'Earth'.\nTo quit, enter 'Q'\nYour choice: ")
        if user_input.lower() == 'q':
            break
        if user_input.lower() == 'mars':
            runmarsrover()
        elif user_input.lower() == 'earth':
            runearthimg()
        else:
            print('Invalid input. Please try again.')


if __name__ == '__main__':
    main()
