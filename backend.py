import numpy as np

class Backend:
    def select_pokemon_array(pokemon_array, user_input):
        choice_index = map(int, user_input.split())

        # Check if the index is valid
        if choice_index < 0 or choice_index >= pokemon_array.shape[0]:
            print(f"Invalid index. Please provide an index between 0 and {pokemon_array.shape[0] - 1}.")
            return
    
        # Get the Pokémon's row
        pokemon_to_transfer = pokemon_array[choice_index]

        # Add it to the selected_pokemon_array
        selected_pokemon_array = np.vstack((selected_pokemon_array, pokemon_to_transfer))


        # Remove it from the original array
        pokemon_array = np.delete(pokemon_array, choice_index, axis=0)
