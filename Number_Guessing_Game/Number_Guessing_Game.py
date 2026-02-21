from random import randint


# Game class
class NumberGuessingGame:
    MIN_TARGET: int = 1
    MAX_TARGET: int = 10
    HARD_KEY: str = '3'
    GMD_KEY: str = '4'
    GMD_NAME: str = 'GUESSER MUST DIE'
    GMD_ATTEMPTS: int = 1

    def __init__(self):
        self._target: int = randint(self.MIN_TARGET, self.MAX_TARGET)
        self._max_attempts: int = 0
        self._current_attempts: int = 0
        self._difficulties: dict[str, tuple[str, int]] = {
            '1': ('EASY', 10),
            '2': ('MEDIUM', 5),
            '3': ('HARD', 3)
        }
        self._selected_mode: str | None = None

    def greet(self) -> None:
        '''Welcome new players'''

        print('Welcome to the Number Guessing Game!')
        print(
            f'I´m thinking of a number between '
            f'{self.MIN_TARGET} and {self.MAX_TARGET}.'
            )
        print('Guess the correct number.\n')

    def select_difficulty(self) -> None:
        '''Here we select the difficulty of the game.'''

        while True:
            print('Select the difficulty level:')
            for mode, (dif_name, dif_attempts) in self._difficulties.items():
                print(f'{mode}. {dif_name} ({dif_attempts} chances)')

            mode = input('\nEnter your choice: ')

            if mode in self._difficulties:
                dif_name, dif_attempts = self._difficulties[mode]
                self._max_attempts = dif_attempts
                self._selected_mode = mode
                print(f'\nDifficulty selected: {dif_name}')
                break
            else:
                print('\nPlease enter a valid option.\n')

    def make_guess(self) -> int:
        '''Input and validate a guess'''

        while True:
            try:
                player_guess: int = int(input('Enter your guess: '))
                break
            except ValueError:
                print('\nInvalid input. Please try again')

        return player_guess

    def guess(self) -> None:
        '''Main guessing logic'''

        print("Let's start the game\n")
        won: bool = False
        while self._current_attempts < self._max_attempts:
            attempts_left: int = self._max_attempts - self._current_attempts
            print(f'{attempts_left} attempt(s) are left.\n')

            player_guess: int = self.make_guess()

            self._current_attempts += 1

            if player_guess > self._target:
                print(f'Incorrect! Number is less than {player_guess}\n')
            elif player_guess < self._target:
                print(f'Incorrect! Number is more than {player_guess}\n')
            else:
                won = True
                break

        self.gameover(won)

    def gameover(self, won: bool) -> None:
        '''Depending of the game outcome we output
        a certain message and unlock features.'''

        if won:
            print("Congratulations. You've guessed correctly.\n")

            # If we have completed the game on hard for the first time
            # we unlock GMD mode.
            if (self._selected_mode == self.HARD_KEY and
                    self.GMD_KEY not in self._difficulties):
                self.unlock_must_die_dif()

        else:
            print(f'Game Over. The correct number was {self._target}\n')

        input('Press any key to continue...\n')

    def unlock_must_die_dif(self) -> None:
        '''Add GUESSER MUST DIE mode to the difficulties dictionary.'''

        print("New difficulty unlocked: Guesser Must Die")
        print("You can now select it after retrying the game.")
        self._difficulties[self.GMD_KEY] = (self.GMD_NAME, self.GMD_ATTEMPTS)

    def continue_game(self) -> bool:
        '''Option to retry'''

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

        return retry == 1

    def reset(self) -> None:
        '''Reset game state.'''

        self._target = randint(self.MIN_TARGET, self.MAX_TARGET)
        self._max_attempts = 0
        self._current_attempts = 0
        self._selected_mode = None


# Main game process
def main() -> None:
    game = NumberGuessingGame()
    while True:
        game.greet()
        game.select_difficulty()
        game.guess()

        if not game.continue_game():
            break

        game.reset()


# Execute main function when directly running this file.
if __name__ == '__main__':
    main()
