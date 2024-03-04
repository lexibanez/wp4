from marsrover import runmarsrover
from earth import runearthimg


def main():
    while True:
        user_input = input("Welcome to the NASA Image Viewer!\nTo view images from the Mars Rover, enter 'Mars'.\nTo view images from the Earth Polychromatic Imaging Camera, enter 'Earth'.\nTo quit, enter 'Q'\nYour choice: ")
        if user_input.lower() == 'q':
            break
        elif user_input.lower() == 'mars':
            runmarsrover()
        elif user_input.lower() == 'earth':
            runearthimg()
        else:
            print('Invalid input. Please try again.')


if __name__ == '__main__':
    main()