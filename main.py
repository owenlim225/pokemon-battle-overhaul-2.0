#🟧🟧🟧 Not yet tested

# # Module installer
# import pkg_handler
# pkg_handler.initialize_packages()


import time, os, sys
from backend import Backend
from frontend import Frontend

class Gameplay:
    #✅ Working
    def __init__(self, backend: Backend) -> None:
        self.backend = backend  # Use shared backend
        self.frontend = Frontend(backend)  # Pass same backend to frontend


    #✅ Working
    def loading_text(self, text):
        os.system('cls')
        for i in range(1, 4):
            sys.stdout.write(f"\r{text}{'.' * i}")  # Overwrites the same line
            sys.stdout.flush()  # Ensures the output is updated immediately
            time.sleep(1)
        time.sleep(1)
        os.system('cls')  # Final cle


    #✅ Working
    def run(self) -> None:
        _in_battle = True
        self.frontend.intro()

        # Player Pokémon selection
        self.frontend.player_pokemon_selection(self.backend.player_1, 4, False)
        self.frontend.player_pokemon_selection(self.backend.player_2, len(self.backend.player_1.pokemons), True)

        self.loading_text("Preparing pokemon")


        # Main game loop
        while _in_battle:
            if self.backend.battle_count:
                self.loading_text("Preparing next battle")

            if not self.backend.battle_count:
                self.frontend.choose_battle_pokemon(self.backend.player_1, "Player 1")
                self.frontend.choose_battle_pokemon(self.backend.player_2, "Player 2")
            else:
                self.frontend.pokemon_change_prompt()  # Players choose their battle Pokémon
                time.sleep(2)

            self.loading_text("Preparing")

            # Apply potion or poison effects with frontend display and backend logic
            self.frontend.potion_or_poison_display(self.backend.player_1, "Player 1", self.backend)
            self.frontend.potion_or_poison_display(self.backend.player_2, "Player 2", self.backend)

            # Start of battle
            self.loading_text(f"Preparing battle No.{self.backend.battle_count}")

            # Execute the battle and apply fatigue adjustments
            self.frontend.pokemon_battle(self.backend.player_1, self.backend.player_2)  # Main battle
            time.sleep(2)
            self.frontend.fatigue_factor_display(self.backend.player_1, self.backend.player_2)  # Fatigue adjustments
            time.sleep(2)

            

            # Check if all Pokémon have been used
            if not self.frontend.check_all_pokemons_used():
                _in_battle = False  # Break out of the loop if the user chooses 'N'
            else:
                # Activate `check_all_pokemons_used` every 3rd battle after all Pokémon are used
                if self.backend.battle_count >= 3 and self.backend.battle_count % 3 == 0:
                    if not self.frontend.check_all_pokemons_used():
                        _in_battle = False

        self.frontend.end_game(self.backend.player_1, self.backend.player_2)  # End the game




if __name__ == "__main__":
    backend_instance = Backend()    
    _game = Gameplay(backend_instance) 
    _game.run()
    


    # frontend = Frontend()
    # frontend.end_game()