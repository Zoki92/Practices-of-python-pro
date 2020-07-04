# shoddy procedural code
import random


class TicTacToe:
    options = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.human_choice = None
        self.computer_choice = None

    def print_options(self):
        print('(1) Rock\n(2) Paper\n(3) Scissors')

    def get_human_options(self):
        self.human_choice = self.options[int(input('Enter the number of your choice: ')) - 1]

    def get_computer_choice(self):
        self.computer_choice = random.choice(self.options)

    def when_human_choice_is_rock(self):
        if self.computer_choice == 'paper':
            print('Sorry, paper beat rock')
        elif self.computer_choice == 'scissors':
            print('Yes, rock beat scissors!')
        else:
            print('Draw!')

    def when_human_choice_is_paper(self):
        if self.computer_choice == 'scissors':
            print('Sorry, scissors beat paper')
        elif self.computer_choice == 'rock':
            print('Yes, paper beat rock!')
        else:
            print('Draw!')

    def when_human_choice_is_scissors(self):
        if self.computer_choice == 'rock':
            print('Sorry, rock beat scissors')
        elif self.computer_choice == 'paper':
            print('Yes, scissors beat paper!')
        else:
            print('Draw!')

    def print_choices(self):
        print(f'You chose {self.human_choice}')
        print(f'The computer chose {self.computer_choice}')

    def play(self):
        self.print_options()
        self.get_human_options()
        self.get_computer_choice()
        self.print_choices()
        if self.human_choice == 'rock':
            self.when_human_choice_is_rock()
        elif self.human_choice == 'paper':
            self.when_human_choice_is_paper()
        elif self.human_choice == 'scissors':
            self.when_human_choice_is_scissors


tic_tac_toe = TicTacToe()
tic_tac_toe.play()


def shoddy_procedural_code():
    options = ['rock', 'paper', 'scissors']

    print('(1) Rock\n(2) Paper\n(3) Scissors')
    human_choice = options[int(input('Enter the number of your choice: ')) - 1]
    print(f'You chose {human_choice}')
    computer_choice = random.choice(options)
    print(f'The computer chose {computer_choice}')
    if human_choice == 'rock':
        if computer_choice == 'paper':
            print('Sorry, paper beat rock')
        elif computer_choice == 'scissors':
            print('Yes, rock beat scissors!')
        else:
            print('Draw!')
    elif human_choice == 'paper':
        if computer_choice == 'scissors':
            print('Sorry, scissors beat paper')
        elif computer_choice == 'rock':
            print('Yes, paper beat rock!')
        else:
            print('Draw!')
    elif human_choice == 'scissors':
        if computer_choice == 'rock':
            print('Sorry, rock beat scissors')
        elif computer_choice == 'paper':
            print('Yes, scissors beat paper!')
        else:
            print('Draw!')


# shoddy_procedural_code()
