import time, os
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

    #✅ Working
    def run(self) -> None: 
        self.pokemon_selection(self.player1, 4, False)
        self.pokemon_selection(self.player2, len(self.player1.pokemons), True)

        print("Preparing battle...")
        time.sleep(2)
        os.system('cls')

        self.battle_pokemon(self.player1)
        self.battle_pokemon(self.player2)


    #✅ Working
    def pokemon_selection(self, player, max_pick, restricted_pick=False) -> None: 
        while True:
            try:
                os.system('cls')
                print("Available Pokémon:\n")
                print(self.pokemon_array)

                # Get input from player (space-separated indexes)

                player_picks = list(map(int, input(f"Pick from 1 to {max_pick} Pokémon: ").split()))

                # Validate the number of picks
                if restricted_pick and len(player_picks) != max_pick:
                    print(f"You must pick exactly {max_pick} Pokémon. Try again.")
                    time.sleep(2)
                    continue

                if not restricted_pick and not (1 <= len(player_picks) <= max_pick):
                    print(f"You must pick between 1 and {max_pick} Pokémon. Try again.")
                    time.sleep(2)
                    continue


                # Validate if all selected indexes are within the valid range
                if any(pick < 0 or pick >= len(self.pokemon_array) for pick in player_picks):
                    print("One or more picks are out of range. Try again.")
                    time.sleep(2)
                    continue

                # Debug 🐞: Print selected Pokémon name from the original array
                print(f"Player selected Pokémon: {[str(self.pokemon_array[i, 0]) for i in player_picks]}") #✅ Working


                # Extract selected Pokémon based on player picks
                selected_pokemon = self.pokemon_array[np.array(player_picks), :]

                # Ensure the selected Pokémon array has the correct shape for stacking
                if player.pokemons.size == 0:
                    player.pokemons = selected_pokemon  # Directly assign if empty
                else:
                    player.pokemons = np.vstack((player.pokemons, selected_pokemon))

                # Remove the selected Pokémon from the original array
                self.pokemon_array = np.delete(self.pokemon_array, player_picks, axis=0)

                print("\n\n\nPlayer:\n")
                print(player.pokemons)
                time.sleep(3)

                break  # Exit loop on successful selection

            except ValueError as e:
                print(f"Invalid input. Error: {e}. Please enter valid numbers separated by spaces.")
                time.sleep(3)



    def battle_pokemon(self, player_pokemon) -> None:
        while True:
            try:
                # Print the player's available Pokémon
                print("Available Pokémon:\n", player_pokemon.pokemons)

                # Ask the player to select a Pokémon for battle
                battle_pick = int(input("Please select your battle Pokémon (index): "))

                # Validate the selection
                if battle_pick < 0 or battle_pick >= len(player_pokemon.pokemons):
                    print("Invalid selection. Please pick one of your available Pokémon.")
                    continue

                # Extract the selected Pokémon
                selected_pokemon = player_pokemon.pokemons[battle_pick, :]

                # Assign the selected Pokémon to the player's current Pokémon
                player_pokemon.current_pokemon = selected_pokemon

                # Remove the selected Pokémon from the player's available Pokémon
                player_pokemon.pokemons = np.delete(player_pokemon.pokemons, battle_pick, axis=0)

                print(f"Current battle Pokémon: {player_pokemon.current_pokemon}")
                break  # Exit loop on successful selection

            except ValueError as e:
                print(f"Invalid input. Error: {e}. Please enter a valid number.")
                time.sleep(3)








if __name__ == "__main__":
    _game = Gameplay()
    _game.run()

    print(f"\n\nplayer 1 pokemons: {_game.player1.pokemons}\n\n")
    print(f"\n\nplayer 2 pokemons: {_game.player2.pokemons}\n\n")

    print(f"\n\nplayer 1 battle pokemons: {_game.player1.current_pokemon}\n\n")
    print(f"\n\nplayer 2 battle pokemons: {_game.player2.current_pokemon}\n\n")

    print(f"Available pokemons", _game.pokemon_array)
    