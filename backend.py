#🟧🟧🟧 Not yet tested
import time, os, random
import numpy as np
import pandas as pd

class Player:
    def __init__(self) -> None:
        # Array to store Pokemon: (name, power) tuples
        self.pokemons = np.empty((0, 2), dtype=object)

        # Current Pokémon in battle, initially None
        self.current_pokemon = None

        # Array to track used Pokémon
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

    
    #✅ Working
    def prompt_pokemon_change(self, player, player_name) -> bool:
        # Prompts the player to change their battle Pokémon. Returns True if changed, False otherwise
        try:
            user_choice = input(f"{player_name}: Would you like to change your battle Pokémon? [Y/N]: ").strip().lower()
            if user_choice not in ["y", "n"]:
                raise ValueError("Invalid choice. Please enter 'Y' or 'N'.")

            if user_choice == "y":
                self.change_battle_pokemon(player)
                return True  # Pokémon was changed

            return False  # Player keeps the same Pokémon

        except ValueError as e:
            print(f"Error: {e}. Please try again.")
            return self.prompt_pokemon_change(player, player_name)


    #✅ Working
    def change_battle_pokemon(self, player) -> None:
        # Allows the player to swap their current battle Pokémon with one from their available Pokémon
        try:
            # Display the available Pokémon with their indexes
            print("Available Pokémon:")
            for i, pokemon in enumerate(player.pokemons):
                print(f"{i}: {pokemon[0]} (Health: {pokemon[1]}, Power: {pokemon[2]})")

            # Ask the user to select the index of the Pokémon to swap
            index = int(input("Select your new battle Pokémon: "))

            # Validate the input index
            if index < 0 or index >= len(player.pokemons):
                raise ValueError("Invalid index. Please select a valid Pokémon.")

            # If there's already a Pokémon in `current_pokemon`, add it back to the list
            if player.current_pokemon is not None and player.current_pokemon.size > 0:
                player.pokemons = np.vstack([player.pokemons, player.current_pokemon])

            # Update `current_pokemon` with the selected Pokémon
            player.current_pokemon = player.pokemons[index]

            # Remove the selected Pokémon from `pokemons`
            player.pokemons = np.delete(player.pokemons, index, axis=0)

            print(f"\n{player.current_pokemon[0]} is now ready for battle!\n")
            player.used_pokemons += 1

        except ValueError as e:
            print(f"Error: {e}. Please try again.")


    #✅ Working
    def pokemon_battle(self, player_1, player_2) -> None:
        os.system('cls') #clear terminal 

        print("\n\nBattle start!\n\n")
        print(f"Player 1: {player_1.current_pokemon[0]} vs {player_2.current_pokemon[0]}: Player 2\n")

        # Player 1 wins
        if int(player_1.current_pokemon[2]) > int(player_2.current_pokemon[2]):
            print(f"          {player_1.current_pokemon[2]} > {player_2.current_pokemon[2]}")
            print(f"\n\nPlayer 1 wins!\n\n")
            player_1.wins += 1
            winner = "player 1"

            # Adjust health
            player_1_health_adjustment = int(player_1.current_pokemon[1]) + 5  # Increase health of winning Pokémon
            player_2_health_adjustment = max(0, int(player_2.current_pokemon[1]) - 10)  # Decrease health of losing Pokémon

            print("Health")
            print(f"{player_1.current_pokemon[0]}: {player_1.current_pokemon[1]} -> {player_1_health_adjustment}")
            print(f"{player_2.current_pokemon[0]}: {player_2.current_pokemon[1]} -> {player_2_health_adjustment}")

            # Adjust health permanently (in-place)
            player_1.current_pokemon[1] = int(player_1.current_pokemon[1]) + 5  # Increase health of the winning Pokémon
            player_2.current_pokemon[1] = max(0, int(player_2.current_pokemon[1]) - 10)
            
            # Add battle to pd frame
            self.add_battle(player_1.current_pokemon, player_2.current_pokemon, winner)

        # Player 2 wins
        elif int(player_1.current_pokemon[2]) < int(player_2.current_pokemon[2]):
            print(f"          {player_1.current_pokemon[2]} < {player_2.current_pokemon[2]}")
            print(f"\n\nPlayer 2 wins!\n\n")
            player_2.wins += 1
            winner = "player 2"

            # Adjust health
            player_1_health_adjustment =  max(0, int(player_1.current_pokemon[1]) - 10)  # Decrease health of losing Pokémon
            player_2_health_adjustment = int(player_2.current_pokemon[1]) + 5  # Increase health of winning Pokémon

            print("Health")
            print(f"{player_1.current_pokemon[0]}: {player_1.current_pokemon[1]} -> {player_1_health_adjustment}")
            print(f"{player_2.current_pokemon[0]}: {player_2.current_pokemon[1]} -> {player_2_health_adjustment}")
            
            # Adjust health permanently (in-place)
            player_1.current_pokemon[1] = max(0, int(player_1.current_pokemon[1]) - 10)
            player_2.current_pokemon[1] = int(player_2.current_pokemon[1]) + 5  # Increase health of the winning Pokémon
            
            # Add battle to pd frame
            self.add_battle(player_1.current_pokemon, player_2.current_pokemon, winner)

        # Draw
        else:
            print(f"          {player_1.current_pokemon[2]} = {player_2.current_pokemon[2]}")
            print(f"\n\nIt's a draw!\n\n")
            winner = "Draw"

            # Add battle to pd frame
            self.add_battle(player_1.current_pokemon, player_2.current_pokemon, winner)

        

    #✅ Working
    def potion_or_poison(self, player) -> None:
        # Generate or reuse the blessing value
        if player.current_pokemon.shape[0] <= 3 or int(player.current_pokemon[3]) == 0:
            rand_val = random.randint(10, 15)
            if player.current_pokemon.shape[0] <= 3:
                player.current_pokemon = np.append(player.current_pokemon, rand_val)
            else:
                player.current_pokemon[3] = rand_val
                
            print(f"\n👼 passed by and gave your {player.current_pokemon[0]} {rand_val} blessings!!")
        else:
            rand_val = int(player.current_pokemon[3])
            print(f"\n👼 saw that your {player.current_pokemon[0]} still has {rand_val} blessings.")

        print("\n🧙 asked if you like to trade your blessings for a random effect.\n")

        try:
            user_choice = input("[Y/N]: ").strip().lower()
            if user_choice not in ["y", "n"]:
                raise ValueError("Invalid choice. Please enter 'Y' or 'N'.")

            if user_choice == "y":
                print("\n🧙 casted a spell...")

                # If user agrees, the blessing val of the current pokemon removed. Reduce the power lvl as per choice.           
                if random.choice(["poison", "potion"]) == "poison":
                    new_power = max(0, int(player.current_pokemon[2]) - rand_val)
                    print(f"\nYour blessing turned into poison! Your {player.current_pokemon[0]} lost power!")
                    print(f"{player.current_pokemon[0]}: {player.current_pokemon[2]} -> {new_power}")
                    player.current_pokemon[2] = new_power
                
                # Retain the blessing val and will be asked to be used up again later.
                else:
                    new_power = int(player.current_pokemon[2]) + rand_val
                    print(f"\nYour blessing turned into potion! Your {player.current_pokemon[0]} gained power!")
                    print(f"{player.current_pokemon[0]}: {player.current_pokemon[2]} -> {new_power}")
                    player.current_pokemon[2] = new_power

                # Reset the blessing value to 0 after use
                player.current_pokemon[3] = 0
                print(f"\nThe blessing has been used and is now reset to 0.")

            else:
                print("\nYou kept your blessings untouched.")

        except ValueError as e:
            print(f"Error: {e}. Please try again.")


    #✅ Working
    def player_pokemon_selection(self, player, player_picks):
        # Process player Pokémon selection
        # Extract selected Pokémon based on player picks
        selected_pokemon = self.pokemon_array[np.array(player_picks), :]

        # Add selected Pokémon to the player's collection
        if player.pokemons.size == 0:
            player.pokemons = selected_pokemon  # Assign directly if empty
        else:
            player.pokemons = np.vstack((player.pokemons, selected_pokemon))

        # Remove the selected Pokémon from the original array
        self.pokemon_array = np.delete(self.pokemon_array, player_picks, axis=0)
        
        #🐞 Debugger ======================
        # print("debug:", player.pokemons)
        #==================================


    #✅ Working
    def choose_battle_pokemon(self, player) -> None:
        # Process the player's selection of a Pokémon for battle
        if player.pokemons.size == 0:
            print("You have no available Pokémon to select.")
            return  # Exit if no Pokémon are available

        # Get the player's selected Pokémon index
        while True:
            try:
                battle_pick = int(input("Please select your battle Pokémon (index): "))

                # Validate the input index
                if battle_pick < 0 or battle_pick >= len(player.pokemons):
                    print("Invalid selection. Please pick one of your available Pokémon.")
                    continue

                # Assign the selected Pokémon to the player's current Pokémon
                player.current_pokemon = player.pokemons[battle_pick]

                # Remove the selected Pokémon from the player's available Pokémon
                player.pokemons = np.delete(player.pokemons, battle_pick, axis=0)
                break  # Exit loop on successful selection

            except ValueError as e:
                print(f"Invalid input. Error: {e}. Please enter a valid number.")


    #✅ Working
    def fatigue_factor(self, player_1, player_2) -> None:
        # Decrease health of both current Pokémon by 2
        player_1_health_adjustment = max(0, int(player_1.current_pokemon[1]) - 2)
        player_2_health_adjustment = max(0, int(player_2.current_pokemon[1]) - 2)

        print("Both of your pokémons feel fatigued. Both lost 2 health points...")
        print(f"{player_1.current_pokemon[0]}: {player_1.current_pokemon[1]} -> {player_1_health_adjustment}")
        print(f"{player_2.current_pokemon[0]}: {player_2.current_pokemon[1]} -> {player_2_health_adjustment}")
        time.sleep(2)
        os.system('cls')





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