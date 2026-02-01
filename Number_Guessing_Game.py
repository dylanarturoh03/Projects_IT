from random import randint


# Game class
class NumberGuessingGame:
    def __init__(self):
        self._target: int = randint(1, 20)
        self._attempts: int = 0
        self._current_attempts: int = 0

    # Welcome new players
    def greet(self) -> None:
        print('Welcome to the Number Guessing Game!')
        print('I´m thinking of a number between 1 and 20.')
        print('Guess the correct number.\n')

    # Here we select the difficulty of the game
    def select_difficulty(self) -> None:
        while True:
            print('Select the difficulty level:')
            print('1. Easy (10 chances)')
            print('2. Medium (5 chances)')
            print('3. Hard (3 chances)\n')

            difficulty = input('Enter your choice: ')

            if difficulty == '1':
                self._attempts = 10
                print('\nDifficulty selected: Easy')
                break
            elif difficulty == '2':
                self._attempts = 5
                print('\nDifficulty selected: Medium')
                break
            elif difficulty == '3':
                self._attempts = 3
                print('\nDifficulty selected: Hard')
                break
            else:
                print('\nPlease enter a valid option.\n')

    # Input a guess
    def make_guess(self) -> int:
        while True:
            try:
                n: int = int(input('Enter your guess: '))
                break
            except ValueError:
                print('\nInvalid input. Please Try Again')

        return n

    # Main guessing logic
    def guess(self) -> None:
        print("Let's start the game\n")
        won: bool = False
        while self._current_attempts < self.attempts:
            self.increment_attempts()
            attempts_left = self._attempts - self._current_attempts
            print(f'{attempts_left + 1} attempt(s) are left.\n')

            n: int = self.make_guess()

            if n == self._target:
                won = True
                break
            elif n < self._target:
                print(f'Incorrect! Number is more than {n}\n')
            elif n > self._target:
                print(f'Incorrect! Number is less than {n}\n')

        self.gameover(won)

    # Increase number of attempts made
    def increment_attempts(self) -> None:
        self._current_attempts += 1

    # Depending of the game outcome we output a certain message
    def gameover(self, flag: bool) -> None:
        if flag:
            print("Congratulations. You've guessed correctly.\n")
        else:
            print(f'Game Over. The correct number was {self._target}\n')

        input('Press any key to continue...\n')

    # Option to retry
    def continue_game(self) -> bool:
        print('Do you wish to continue?')
        print('1 - Restart')
        print('0 - Finish')

        while True:
            try:
                retry = int(input('\nSelect your choice: '))

                if retry not in (0, 1):
                    print('Choice must be 0 or 1.')
                else:
                    break

            except ValueError:
                print('Invalid option. Please enter a number')

        return bool(retry)


# Main process
if __name__ == '__main__':
    while True:
        game = NumberGuessingGame()
        game.greet()
        game.select_difficulty()
        game.guess()

        if not game.continue_game():
            break
