#🟧🟧🟧 Not yet tested
import time, os, random
import numpy as np
import pandas as pd

#✅ Working
class Player:
    def __init__(self) -> None:
        # Array to store Pokemon: (name, power) tuples
        self.pokemons = np.empty((0, 2), dtype=object)

        # Current Pokemon in battle, initially None
        self.current_pokemon = None

        # Array to track used Pokemon
        self.used_pokemons = 0
        
        # Number of wins
        self.wins = 0



class Backend:
    #✅ Working
    def __init__(self) -> None:
        # Players 
        self.player_1 = Player()
        self.player_2 = Player()


        self.battle_count = 0

        # Initialize a battle summary DataFrame
        self.battle_summary = pd.DataFrame(columns=[
            "Player 1 Pokemon", "Health", "Power",
            "Player 2 Pokemon", "Health", "Power",
            "Winner"
        ])

    # =============================🐞 Unit testing===============================
        # self.add_sample_data()
        
    # def add_sample_data(self):
    #     sample_data = [
    #         ["Pikachu", 35, 55, "Charmander", 39, 52, "Player 1"],
    #         ["Squirtle", 44, 48, "Bulbasaur", 45, 49, "Player 2"],
    #     ]
    #     for row in sample_data:
    #         self.battle_summary.loc[len(self.battle_summary)] = row
    # ======================================================================

        self.pokemon_array = np.array([
                # Name         Health  Power Lvl   blessing
                ["Bulbasaur",   100,      85,        0],
                ["Charmander",  90,       90,        0],
                ["Eevee",       95,       80,        0],
                ["Gengar",      85,       100,       0],
                ["Jigglypuff",  105,      75,        0],
                ["Machamp",     110,      105,       0],    
                ["Mewtwo",      80,       120,       0],
                ["Pikachu",     90,       85,        0],
                ["Snorlax",     110,      95,        0],
                ["Squirtle",    105,      85,        0]
        ])  

    #🟧🟧🟧 Not yet tested
    def get_overall_winner(self):
        # Count the number of wins for Player 1 and Player 2
        player_1_wins = self.player_1.wins
        player_2_wins = self.player_2.wins

        # Determine the overall winner
        if player_1_wins > player_2_wins:
            return "Player 1"
        elif player_2_wins > player_1_wins:
            return "Player 2"
        else:
            return "It's a tie!"

    #✅ Working
    def player_pokemon_selection(self, player, player_picks):
        # Process player Pokemon selection
        # Extract selected Pokemon based on player picks
        selected_pokemon = self.pokemon_array[np.array(player_picks), :]

        # Add selected Pokemon to the player's collection
        if player.pokemons.size == 0:
            player.pokemons = selected_pokemon  # Assign directly if empty
        else:
            player.pokemons = np.vstack((player.pokemons, selected_pokemon))

        # Remove the selected Pokemon from the original array
        self.pokemon_array = np.delete(self.pokemon_array, player_picks, axis=0)
        
        #🐞 Debugger ======================
        # print("debug:", player.pokemons)
        #==================================


    #✅ Working
    def potion_or_poison_calculation(self, player):
            # Calculates the effect of potion or poison on the player's current Pokemon 
            # Generate blessing value if needed
            if player.current_pokemon.shape[0] <= 3 or int(player.current_pokemon[3]) == 0:
                rand_val = random.randint(10, 15)
                if player.current_pokemon.shape[0] <= 3:
                    player.current_pokemon = np.append(player.current_pokemon, rand_val)
                else:
                    player.current_pokemon[3] = rand_val
            else:
                rand_val = int(player.current_pokemon[3])
            
            return rand_val  # Return the blessing value to be used in the frontend logic


    #✅ Working
    def choose_battle_pokemon(self, player) -> None:
        # Process the player's selection of a Pokemon for battle
        if player.pokemons.size == 0:
            print("You have no available Pokemon to select.")
            return  # Exit if no Pokemon are available

        # Get the player's selected Pokemon index
        while True:
            try:
                battle_pick = int(input("Please select your battle Pokemon (index): "))

                # Validate the input index
                if battle_pick < 0 or battle_pick >= len(player.pokemons):
                    print("Invalid selection. Please pick one of your available Pokemon.")
                    continue

                # Assign the selected Pokemon to the player's current Pokemon
                player.current_pokemon = player.pokemons[battle_pick]

                # Remove the selected Pokemon from the player's available Pokemon
                player.pokemons = np.delete(player.pokemons, battle_pick, axis=0)
                break  # Exit loop on successful selection

            except ValueError as e:
                print(f"Invalid input. Error: {e}. Please enter a valid number.")


    #✅ Working
    def handle_battle(self, player_1, player_2) -> dict:
        # Original health of the player's current pokemon
        player_1_original_health = player_1.current_pokemon[1]
        player_2_original_health = player_2.current_pokemon[1]

        # Adjusted health of the player's current pokemon based on the winner
        if int(player_1.current_pokemon[2]) > int(player_2.current_pokemon[2]):
            winner = "player 1"
            player_1.wins += 1
            player_1.current_pokemon[1] = int(player_1.current_pokemon[1]) + 5 # 5 points incrase on health of the winner
            player_2.current_pokemon[1] = max(0, int(player_2.current_pokemon[1]) - 10) # 10 points decrease on health of the loser


        elif int(player_1.current_pokemon[2]) < int(player_2.current_pokemon[2]):
            winner = "player 2"
            player_2.wins += 1
            player_2.current_pokemon[1] = int(player_1.current_pokemon[1]) + 5
            player_1.current_pokemon[1] = max(0, int(player_2.current_pokemon[1]) - 10)

        else:
            winner = "Draw"

        return {
            "winner": winner,
            "player_1_original_health": player_1_original_health,
            "player_1_health": player_1.current_pokemon[1],
            "player_2_original_health": player_2_original_health,
            "player_2_health": player_2.current_pokemon[1],
        }


    #✅ Working
    def add_battle(self, player1_pokemon, player2_pokemon, winner):
        # print(f"Adding battle: {player1_pokemon[0]} vs {player2_pokemon[0]}, Winner: {winner}")

        # Create copies to avoid modifying original data
        player1_data = player1_pokemon.copy()
        player2_data = player2_pokemon.copy()


        # Create a new entry as a list
        new_entry = [
            player1_data[0], player1_data[1], player1_data[2],  # Player 1 data
            player2_data[0], player2_data[1], player2_data[2],  # Player 2 data
            winner  # Winner of the battle
        ]

        # Add the new entry to the battle summary DataFrame
        self.battle_summary.loc[len(self.battle_summary)] = new_entry

        # Increment the battle count
        self.battle_count += 1


    # #✅ Working
    # def fatigue_factor(self, player_1, player_2) -> None:
    #     # Decrease health of both current Pokemon by 2
    #     player_1_health_adjustment = max(0, int(player_1.current_pokemon[1]) - 2)
    #     player_2_health_adjustment = max(0, int(player_2.current_pokemon[1]) - 2)

    #     print("Both of your pokémons feel fatigued. Both lost 2 health points...")
    #     print(f"{player_1.current_pokemon[0]}: {player_1.current_pokemon[1]} -> {player_1_health_adjustment}")
    #     print(f"{player_2.current_pokemon[0]}: {player_2.current_pokemon[1]} -> {player_2_health_adjustment}")
    #     time.sleep(2)
    #     os.system('cls')





#======================🐞 Debugger ======================
# if __name__ == "__main__":
#     backend = Backend()
#     player1_pokemon = ["Pikachu", 35, 55]
#     player2_pokemon = ["Charmander", 39, 52]
#     backend.add_battle(player1_pokemon, player2_pokemon, "player1")
#     backend.add_battle(player1_pokemon, player2_pokemon, "player2")
#     backend.add_battle(player1_pokemon, player2_pokemon, "player3")
#     backend.add_battle(player1_pokemon, player2_pokemon, "player4")
#     backend.add_battle(player1_pokemon, player2_pokemon, "player5")
#     backend.add_battle(player1_pokemon, player2_pokemon, "player6")
#     backend.add_battle(player1_pokemon, player2_pokemon, "player7")
#     backend.add_battle(player1_pokemon, player2_pokemon, "player8")

#     print(backend.battle_summary)
#========================================================