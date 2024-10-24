# frontend.py
from backend import Backend
from rich.console import Console
from rich.table import Table
from rich.box import HEAVY  # Import correct box type

class Frontend:
    def __init__(self):
        # Initialize backend and console
        self.backend = Backend()
        self.console = Console()

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

# Example usage
if __name__ == "__main__":
    frontend = Frontend()
    frontend.display_battle_summary()
