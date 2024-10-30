import time, os, sys
from backend import Backend
from frontend import Frontend

class Gameplay:
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

        # Player Pokémon selection
        self.frontend.player_pokemon_selection(self.backend.player_1, 4, False)
        self.frontend.player_pokemon_selection(self.backend.player_2, len(self.backend.player_1.pokemons), True)

        self.loading_text("Preparing pokemon")

        #✅ Working
        # Main game loop
        while _in_battle:
            self.loading_text("Preparing battle")

            #✅ Working
            if not self.backend.battle_count:
                self.frontend.choose_battle_pokemon(self.backend.player_1, "Player 1")
                self.frontend.choose_battle_pokemon(self.backend.player_2, "Player 2")
            else:
                #✅ Working
                # Players choose their battle Pokémon
                if not self.backend.prompt_pokemon_change(self.backend.player_1, "Player 1"):
                    print("Player 1 keeps the same Pokémon.")
                if not self.backend.prompt_pokemon_change(self.backend.player_2, "Player 2"):
                    print("Player 2 keeps the same Pokémon.")


            self.loading_text("Preparing")

            #✅ Working
            # Apply potion or poison effects with frontend display and backend logic
            self.frontend.potion_or_poison_display(self.backend.player_1, "Player 1", self.backend)
            self.frontend.potion_or_poison_display(self.backend.player_2, "Player 2", self.backend)



            # Start of battle
            self.loading_text(f"Preparing battle {self.backend.battle_count}")


            #✅ Working
            # Execute the battle and apply fatigue adjustments
            self.backend.pokemon_battle(self.backend.player_1, self.backend.player_2)  # Main battle
            time.sleep(2)
            self.backend.fatigue_factor(self.backend.player_1, self.backend.player_2)  # Fatigue adjustments
            time.sleep(2)

            # ===============================Debugger===============================
            # print("debug\nself.backend.player_1.used_pokemons", self.backend.player_1.used_pokemons)
            # print("len(self.backend.player_1.pokemons)", len(self.backend.player_1.pokemons))
            # print("self.backend.player_2.used_pokemons", self.backend.player_2.used_pokemons)
            # print("len(self.backend.player_2.pokemons)", len(self.backend.player_2.pokemons))
            # ======================================================================

            # Check if all Pokémon have been used
            if not self.frontend.check_all_pokemons_used():
                _in_battle = False  # Break out of the loop if the user chooses 'N'
                    

        #✅ Working
        self.frontend.end_game() # End the game

if __name__ == "__main__":
    backend_instance = Backend()    
    _game = Gameplay(backend_instance) 
    _game.run()


    # frontend = Frontend()
    # frontend.end_game()