import time, os
from backend import Backend, Player
from rich.console import Console

class Gameplay:
    def __init__(self) -> None:
        self.backend = Backend()
        self.console = Console()

        # Players 
        self.player_1 = Player()
        self.player_2 = Player()

    #✅ Working
    def run(self) -> None:
        _in_battle = True

        # Player Pokémon selection
        self.backend.player_pokemon_selection(self.player_1, 4, False)
        self.backend.player_pokemon_selection(self.player_2, len(self.player_1.pokemons), True)

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
            if not self.backend.battle_count:
                self.backend.choose_battle_pokemon(self.player_1)
                self.backend.choose_battle_pokemon(self.player_2)
            else:
                #✅ Working
                # Players choose their battle Pokémon
                if not self.backend.prompt_pokemon_change(self.player_1, "Player 1"):
                    print("Player 1 keeps the same Pokémon.")
                if not self.backend.prompt_pokemon_change(self.player_2, "Player 2"):
                    print("Player 2 keeps the same Pokémon.")


            print("\nPreparing...\n")
            time.sleep(2)
            os.system('cls')

            #✅ Working
            # Apply potion or poison effects
            self.backend.potion_or_poison(self.player_1)
            self.backend.potion_or_poison(self.player_2)

            # Start of battle
            print(f"\nPreparing battle {self.backend.battle_count}...\n")
            time.sleep(2)
            os.system('cls')
            time.sleep(5)

            #✅ Working
            # Execute the battle and apply fatigue adjustments
            self.backend.pokemon_battle(self.player_1, self.player_2)  # Main battle
            time.sleep(7)
            self.backend.fatigue_factor(self.player_1, self.player_2)  # Fatigue adjustments
            time.sleep(5)

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
        self.frontend.end_game()

if __name__ == "__main__":
    _game = Gameplay()
    _game.run()
