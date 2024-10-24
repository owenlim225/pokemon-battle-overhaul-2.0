import time, os
from backend import Backend, Player


from rich.text import Text
from rich.console import Console
from rich.table import Table
from rich.align import Align
from rich.box import HEAVY  # Import correct box type

class Frontend:
    def __init__(self):
        # Initialize backend and console
        self.backend = Backend()
        self.player = Player()

        self.console = Console()

    #✅ Working
    def display_pokemon_array(self):
        """Display the Pokémon array from backend using a rich table."""
        # Create a rich table with a heavy border
        table = Table(border_style="bold white", box=HEAVY, title="Available Pokémon")

        # Add columns for the Pokémon attributes
        table.add_column("Index", justify="center")
        table.add_column("Name", justify="center")
        table.add_column("Health", justify="center")
        table.add_column("Power", justify="center")

        # Populate the table with Pokémon data from backend
        for idx, pokemon in enumerate(self.backend.pokemon_array):
            table.add_row(
                str(idx),  # Index
                str(pokemon[0]),  # Name
                str(pokemon[1]),  # Health
                str(pokemon[2]),  # Power
            )

        # Print the table center-aligned
        self.console.print(Align.center(table))


    #✅ Working
    def player_pokemon_selection(self, player, max_pick, restricted_pick=False) -> None: 
        """Handle player Pokémon selection with backend logic."""
        while True:
            try:
                os.system('cls')

                # Display the available Pokémon
                self.display_pokemon_array()

                # Get input from player (space-separated indexes)
                player_picks = list(map(int, input(f"Pick from 1 to {max_pick} Pokémon: ").split()))


                # Validate the number of picks
                if restricted_pick and len(player_picks) != max_pick:
                    error_message = Text(f"You must pick exactly {max_pick} Pokémon. Try again.", style="red")
                    self.console.print(error_message)
                    time.sleep(2)
                    continue

                if not restricted_pick and not (1 <= len(player_picks) <= max_pick):
                    error_message = Text(f"You must pick between 1 and {max_pick} Pokémon. Try again.", style="red")
                    self.console.print(error_message)
                    time.sleep(2)
                    continue

                # Validate if all selected indexes are within the valid range
                if any(pick < 0 or pick >= len(self.backend.pokemon_array) for pick in player_picks):
                    error_message = Text("One or more picks are out of range. Try again.", style="red")
                    self.console.print(error_message)
                    time.sleep(2)
                    continue


                # Call backend to handle selection logic
                self.backend.player_pokemon_selection(player, player_picks)

                # Display the selected Pokémon
                self.display_selected_pokemon(player)

                break  # Exit loop on successful selection

            except ValueError as e:
                self.console.print(f"[bold red]Invalid input:[/bold red] {e}. Please try again.")
                time.sleep(3)

    #✅ Working
    def display_selected_pokemon(self, player):
        """Display the player's selected Pokémon with green names."""
        # Start the message with "Player 1 Selected Pokémon: " in white
        message = Text("Player 1 Selected Pokémon: ", style="white")

        # Append each Pokémon name in green, separated by commas
        for idx, pokemon in enumerate(player.pokemons):
            message.append(f"{pokemon[0]}", style="green")
            if idx < len(player.pokemons) - 1:  # Add a comma if not the last Pokémon
                message.append(", ", style="white")

        # Print the styled message to the console
        self.console.print(message)


    #✅ Working
    def display_battle_summary(self):
        battle_summary = self.backend.battle_summary

        # Create a rich table with a heavy border
        table = Table(border_style="bold white", box=HEAVY)  # Use HEAVY correctly

        # Add columns to the table
        for column in battle_summary.columns:
            table.add_column(column, justify="center")

        # Add rows to the table (if any)
        for _, row in battle_summary.iterrows():
            table.add_row(*[str(item) for item in row])

        # Print the table using rich
        self.console.print(table)


    #✅ Working
    def end_game(self) -> None:
        """Handle game end and display the battle summary."""
        os.system('cls')

        # Display game end message with green text
        end_message = Text("\t\t\t\t      Battle Summary\n", style="red")
        self.console.print(end_message)

        # Display battle summary
        self.display_battle_summary()

        # Print a thank-you message in green
        thank_you_message = Text("\n\n\t\t\t\tThank you for playing!\n\n\n\n", style="green")
        self.console.print(thank_you_message)

        time.sleep(10)
        os._exit(0)  # Exit the game

# Example usage
if __name__ == "__main__":
    f = Frontend()
    f.player_pokemon_selection(f.player, max_pick=4, restricted_pick=False)
    
    

