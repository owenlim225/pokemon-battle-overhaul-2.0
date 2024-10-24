import time, os
from backend import Backend

from rich.text import Text
from rich.console import Console
from rich.table import Table
from rich.box import HEAVY  # Import correct box type

class Frontend:
    def __init__(self):
        # Initialize backend and console
        self.backend = Backend()
        self.console = Console()

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
    frontend = Frontend()
    frontend.end_game()
