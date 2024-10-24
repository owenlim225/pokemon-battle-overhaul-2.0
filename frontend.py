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


    # 🟧 Not tested yet
    def player_pokemon_selection(self, player, max_pick, restricted_pick=False):
        """Wrap backend's player_pokemon_selection with rich display."""
        while True:
            try:
                os.system('cls')

                # Display available Pokémon
                self.display_pokemon_array()

                # Get input from player
                player_picks = list(map(int, input(f"Pick from 1 to {max_pick} Pokémon: ").split()))

                # Call the backend selection logic
                self.backend.player_pokemon_selection(player, max_pick, restricted_pick)

                # Display selected Pokémon using rich
                table = Table(title="Selected Pokémon", border_style="blue", show_lines=True)
                table.add_column("Name", justify="center")

                for pokemon in player.pokemons:
                    table.add_row(str(pokemon[0]))

                self.console.print(table)
                break  # Exit loop on success

            except ValueError as e:
                self.console.print(f"[bold red]Invalid input:[/bold red] {e}. Please try again.")
                time.sleep(3)

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
    f.display_pokemon_array()