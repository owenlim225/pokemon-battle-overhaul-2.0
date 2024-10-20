import numpy as np
from backend import Backend
from frontend import Frontend

class Player:
    def __init__(self) -> None:
        # Array to store Pokemon: (name, power) tuples
        self.pokemons = np.empty((0, 2), dtype=object)

        # Current Pokémon in battle, initially None
        self.current_pokemon = None

        # Array to track used Pokémon
        self.used_pokemons = np.empty((0, 2), dtype=object)
        
        # Number of wins
        self.wins = 0



class Gameplay:
    def __init__(self) -> None:
        self.pokemon_array = np.array([
            ["Bulbasaur", 100, 60],
            ["Charmander", 100, 55],
            ["Eevee", 100, 52],
            ["Gengar", 100, 70],
            ["Jigglypuff", 100, 45],
            ["Machamp", 100, 75],
            ["Mewtwo", 100, 90],
            ["Pikachu", 100, 50],
            ["Snorlax", 100, 80],
            ["Squirtle", 100, 58]
        ])

        # Players 
        self.player1 = Player()
        self.player2 = Player()

    


    def run(self) -> None:
        max_pick = 4

        while True:
            try:
                print("Available Pokémon:\n")
                print(self.pokemon_array)

                # Get input from player (space-separated indexes)
                player_picks = list(map(int, input(f"Pick from 1 to {max_pick} Pokémon: ").split()))

                # Validate the number of picks
                if len(player_picks) > max_pick:
                    print(f"You can only pick up to {max_pick} Pokémon. Try again.")
                    continue

                # Validate if all selected indexes are within the valid range
                if any(pick < 0 or pick >= len(self.pokemon_array) for pick in player_picks):
                    print("One or more picks are out of range. Try again.")
                    continue

                # Debug 🐞: Print selected Pokémon from the original array
                print(f"Player 1 selected Pokémon: {[self.pokemon_array[i] for i in player_picks]}")

                # Extract selected Pokémon based on player picks
                selected_pokemon = self.pokemon_array[np.array(player_picks), :]

                # Ensure the selected Pokémon array has the correct shape for stacking
                if self.player1.pokemons.size == 0:
                    self.player1.pokemons = selected_pokemon  # Directly assign if empty
                else:
                    self.player1.pokemons = np.vstack((self.player1.pokemons, selected_pokemon))

                # Remove the selected Pokémon from the original array
                self.pokemon_array = np.delete(self.pokemon_array, player_picks, axis=0)

            

                break  # Exit loop on successful selection

            except ValueError as e:
                print(f"Invalid input. Error: {e}. Please enter valid numbers separated by spaces.")




if __name__ == "__main__":
    _game = Gameplay()
    _game.run()
    print("\n\n\nTite\n\n", _game.player1.pokemons)