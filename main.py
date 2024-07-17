import townLoop

# first, we want to create a Menu class
class Menu:
    # we define our options with our starting (self) method
    def __init__(self):
        self.options = [
            "1. Start new game",
            "2. Continue game",
            "3. Exit"
        ]

    # then, we want to create a method to display each of the options
    def display(self):
        print("\nPlease choose one of the following options:")
        for option in self.options:
            print(option)

    # then, we want to create a method to get the player's choice
    def get_choice(self):
        while True: # loop until the player chooses to exit
            try:
                choice = input("Select an option to start: ")
                if choice in ["1", "2", "3"]:
                    return choice
                else:
                    print("Invalid input. Please enter a number between 1 and 3.")

            except ValueError:
                print("Invalid input. Please enter a valid option")


# now we want to create a Game class
class Game:
    # we define the beginning with our starting (self) method
    def __init__(self):
        print("Welcome to That One Text Adventure!") # welcome the player to our game --> non-repeatable line
        self.menu = Menu() # call the Menu() class and assign it to self.menu
        self.first_area = townLoop.FirstArea() # we create an instance of the firstArea class from the townLoop.py file
        self.game_state = None

    # and we define the start_new_game method
    def start_new_game(self):
        print("Okay, starting a new game!")
        self.first_area.new_game_welcome() # call this method from the FirstArea class

    # and we define the continue_game method
    def continue_game(self):
        print("Continuing your game!")
        self.first_area.continue_game_welcome() # call this method from the FirstArea class

    # and we define the exit_game method
    def exit_menu(self):
        print("Exiting the menu. See you later!")
        exit(0)


    # now we define the main (self) method
    def main(self):
        while True:
            # first, we display the options
            self.menu.display()

            # then, we get a choice and save it in a "choice" variable
            choice = self.menu.get_choice()

            if choice == "1": # handle the first choice
                self.start_new_game() # go ahead and start a new game
                break # end the while loop here

            elif choice == "2": # handle the second choice
                self.continue_game() # go ahead and continue the current game
                break # end the while loop here

            elif choice == "3": # handle the third choice
                self.exit_menu() # go ahead and exit the menu


if __name__ == "__main__":
    game = Game() # call the Game class
    game.main() # call the main method of the game
