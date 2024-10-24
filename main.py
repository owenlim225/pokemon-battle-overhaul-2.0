v4.0-(stable-ver)
import time, os, random
import numpy as np
import pandas as pd
from backend import Backend
from frontend import Frontend

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


class Gameplay:
    #✅ Working
    def __init__(self) -> None:
        self.battle_count = 0

        # Initialize a battle summary DataFrame
        self.battle_summary = pd.DataFrame(columns=[
            "Player 1 Pokemon", "Player 1 Health", "Player 1 Power",
            "Player 2 Pokemon", "Player 2 Health", "Player 2 Power",
            "Winner"
        ])


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

        # Players 
        self.player_1 = Player()
        self.player_2 = Player()


    #✅ Working
    def add_battle(self, player1_pokemon, player2_pokemon, winner):
        """Adds a battle entry to the summary."""
        # Create a copy of the Pokémon data to avoid changes affecting the record
        player1_data = player1_pokemon.copy()
        player2_data = player2_pokemon.copy()

        new_entry = pd.DataFrame([{
            "Player 1 Pokemon": player1_data[0],
            "Player 1 Health":  player1_data[1],
            "Player 1 Power":   player1_data[2],
            "Player 2 Pokemon": player2_data[0],
            "Player 2 Health":  player2_data[1],
            "Player 2 Power":   player2_data[2],
            "Winner":           winner
        }])

        # Concatenate the new entry to the existing battle summary
        self.battle_summary = pd.concat([self.battle_summary, new_entry], ignore_index=True)

        # Increment battle count
        self.battle_count += 1


    #✅ Working
    def end_game(self) -> None:
        """Handle game end and display the battle summary."""
        os.system('cls')
        print("The game ends\n")
        print(self.battle_summary)
        print("\n\nThank you for playing!")
        time.sleep(10)
        os._exit(0)  # Exit the game


    #✅ Working
    def prompt_pokemon_change(self, player, player_name) -> bool:
        """Prompts the player to change their battle Pokémon. Returns True if changed, False otherwise."""
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
        """Allows the player to swap their current battle Pokémon with one from their available Pokémon."""
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
            

        # Draw
        else:
            print(f"          {player_1.current_pokemon[2]} = {player_2.current_pokemon[2]}")
            print(f"\n\nIt's a draw!\n\n")
            winner = "Draw"

        self.add_battle( player_1.current_pokemon, player_2.current_pokemon, winner)
       

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
    def player_pokemon_selection(self, player, max_pick, restricted_pick=False) -> None: 
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


    #✅ Working
    def choose_battle_pokemon(self, player) -> None:
        while True:
            try:
                # Check if the player has available Pokémon
                if player.pokemons.size == 0:
                    print("You have no available Pokémon to select.")
                    return  # Exit the function if no Pokémon are available

                # Print the player's available Pokémon
                print("Available Pokémon:\n")
                for i, pokemon in enumerate(player.pokemons):
                    print(f"{i}: {pokemon[0]} (Health: {pokemon[1]}, Power: {pokemon[2]})")

                # Ask the player to select a Pokémon for battle
                battle_pick = int(input("Please select your battle Pokémon (index): "))

                # Validate the selection
                if battle_pick < 0 or battle_pick >= len(player.pokemons):
                    print("Invalid selection. Please pick one of your available Pokémon.")
                    continue

                # Extract the selected Pokémon
                selected_pokemon = player.pokemons[battle_pick, :]

                # Assign the selected Pokémon to the player's current Pokémon
                player.current_pokemon = selected_pokemon

                # Remove the selected Pokémon from the player's available Pokémon
                player.pokemons = np.delete(player.pokemons, battle_pick, axis=0)

                print(f"Current battle Pokémon: {player.current_pokemon}")
                break  # Exit loop on successful selection

            except ValueError as e:
                print(f"Invalid input. Error: {e}. Please enter a valid number.")
                time.sleep(3)


    #✅ Working
    def fatigue_factor(self, player_1, player_2) -> None:
        # Decrease health of both current Pokémon by 2
        player_1_health_adjustment = max(0, int(player_1.current_pokemon[1]) - 2)
        player_2_health_adjustment = max(0, int(player_2.current_pokemon[1]) - 2)

        print("Both of your pokémons feel fatigued. Both lost 2 health points...")
        print(f"{player_1.current_pokemon[0]}: {player_1.current_pokemon[1]} -> {player_1_health_adjustment}")
        print(f"{player_2.current_pokemon[0]}: {player_2.current_pokemon[1]} -> {player_2_health_adjustment}")
        time.sleep(3)
        os.system('cls')


    #✅ Working
    def run(self) -> None:
        _in_battle = True

        # Player Pokémon selection
        self.player_pokemon_selection(self.player_1, 4, False)
        self.player_pokemon_selection(self.player_2, len(self.player_1.pokemons), True)

        print("\nPreparing pokemon...\n")
        time.sleep(2)
        os.system('cls')

        #✅ Working
        # Main game loop
        while _in_battle:
            print("\nPreparing battle...\n")
            time.sleep(2)
            os.system('cls')

            #✅ Working
            if not self.battle_count:
                self.choose_battle_pokemon(self.player_1)
                self.choose_battle_pokemon(self.player_2)
            else:
                #✅ Working
                # Players choose their battle Pokémon
                if not self.prompt_pokemon_change(self.player_1, "Player 1"):
                    print("Player 1 keeps the same Pokémon.")
                if not self.prompt_pokemon_change(self.player_2, "Player 2"):
                    print("Player 2 keeps the same Pokémon.")


            print("\nPreparing...\n")
            time.sleep(2)
            os.system('cls')

            #✅ Working
            # Apply potion or poison effects
            self.potion_or_poison(self.player_1)
            self.potion_or_poison(self.player_2)

            # Start of battle
            print(f"\nPreparing battle {self.battle_count}...\n")
            time.sleep(2)
            os.system('cls')
            time.sleep(5)

            #✅ Working
            # Execute the battle and apply fatigue adjustments
            self.pokemon_battle(self.player_1, self.player_2)  # Main battle
            time.sleep(7)
            self.fatigue_factor(self.player_1, self.player_2)  # Fatigue adjustments
            time.sleep(7)

            # ===============================Debugger===============================
            # print("debug\nself.player_1.used_pokemons", self.player_1.used_pokemons)
            # print("len(self.player_1.pokemons)", len(self.player_1.pokemons))
            # print("self.player_2.used_pokemons", self.player_2.used_pokemons)
            # print("len(self.player_2.pokemons)", len(self.player_2.pokemons))
            # ======================================================================

            #✅ Working
            # Check if all Pokémon have been used 
            if self.player_1.used_pokemons == len(self.player_1.pokemons) and \
               self.player_2.used_pokemons == len(self.player_2.pokemons):
                try:
                    print("All pokemons were used in the battle.\n")
                    user_choice = input("Would you like to continue the battle? [Y/N]: ").strip().lower()
                    if user_choice not in ["y", "n"]:
                        raise ValueError("Invalid choice. Please enter 'Y' or 'N'.")
                        
                    if user_choice == "n": 
                        break
                    else:
                        continue

                except ValueError as e:
                    print(f"Error: {e}. Please try again.")
            else:
                continue
                    
        #✅ Working
        # End the game
        self.end_game()


if __name__ == "__main__":
    _game = Gameplay()
    _game.run()


    # print(f"\n\nplayer 1 pokemons: {_game.player_1.pokemons}\n\n")
    # print(f"\n\nplayer 2 pokemons: {_game.player_2.pokemons}\n\n")

    # print(f"\n\nplayer 1 battle pokemons: {_game.player_1.current_pokemon}\n\n")
    # print(f"\n\nplayer 2 battle pokemons: {_game.player_2.current_pokemon}\n\n")

    # print(f"Available pokemons", _game.pokemon_array)
    

