#🟧🟧🟧 Not yet tested

import time, os, sys, random
from backend import Backend
import numpy as np

from rich.text import Text
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich.box import HEAVY

class Frontend:
    #✅ Working
    def __init__(self, backend: Backend):
        self.backend = backend  # Use shared backend
        self.console = Console()


# ================================== Display ==============================================

#✅ Working
    def print_dual_panel(self, player1_message, player1_title, player1_style, 
                     player2_message, player2_title, player2_style):
        # Divide the console into two equal sections
        console_width = self.console.size.width // 2

        # Create aligned messages for both panels
        player1_aligned_message = Align.center(player1_message)
        player2_aligned_message = Align.center(player2_message)

        # Panel for Player 1 with heavy border
        panel1 = Panel(
            player1_aligned_message,
            title=player1_title,
            style=player1_style,
            border_style=player1_style,
            width=console_width,
            padding=(1, 1),
            box=HEAVY  # Use heavy border
        )

        # Panel for Player 2 with heavy border
        panel2 = Panel(
            player2_aligned_message,
            title=player2_title,
            style=player2_style,
            border_style=player2_style,
            width=console_width,
            padding=(1, 1),
            box=HEAVY  # Use heavy border
        )

        # Use a table to align the two panels side by side
        table = Table.grid(padding=1)
        table.add_column(justify="center", width=console_width)
        table.add_column(justify="center", width=console_width)
        table.add_row(panel1, panel2)

        # Print the table with the two side-by-side panels
        self.console.print(table)


    #✅ Working
    def print_panel(self, message, title, style, width_fraction=2):
            # Helper function to create and print a styled panel
            console_width = self.console.size.width // width_fraction
            aligned_message = Align.center(message)
            panel = Panel(
                aligned_message,
                title=title,
                style=style,
                border_style=style,
                width=console_width,
                padding=(1, 1)
            )
            self.console.print(panel, justify="left")


    ##✅ Working
    def intro(self):
        os.system('cls')

        message = "🏆 Winner: [green]+5 Health💚, +5 Power[/green]\n🔥 Loser: [red]-10 Health💔, +3 Power[/red]"

        # Print the panel with centered alignment
        self.console.print(Panel(Align.center("[bold blue]Pokemon Battle![/bold blue]", vertical="middle"), style="white", border_style="blue", box=HEAVY))
        self.console.print(Align.center("By: Sherwin P.Limosnero\n\n", vertical="middle"), style="white")
        

        self.console.print(Align.center("[yellow]🛈[/yellow]: After each selection, 👼 blesses your [green]pokemon[/green] with a [bold yellow]random value[/bold yellow].", vertical="middle"), style="white")
        self.console.print(Align.center("[yellow]🛈[/yellow]: 🧙 can exchange your [bold yellow]✨blessing✨[/bold yellow] for a [purple]random effect[/purple].", vertical="middle"), style="white")
        self.console.print(Align.center("[yellow]🛈[/yellow]: [purple]random effect[/purple] could be [bold green]💚 potion[/bold green] or [bold red]💔 poison[/bold red].", vertical="middle"), style="white")
        self.console.print(Align.center("[yellow]🛈[/yellow]: [italic]After every battle, ⚔️ pokemon lose [bold red]-2 Health💔[/bold red] due to [red]fatigue[/red][/italic].", vertical="middle"), style="white")
        self.console.print(Align.center("[yellow]🛈[/yellow]: To finish the battle, both players must use all their pokemons.", vertical="middle"), style="white")
        self.console.print(Align.center(message, vertical="middle"), style="white")
        
        self.console.print(Panel(Align.center("[bold green]PRESS ENTER TO START[/bold green] or [bold red]type 'q' to quit[/bold red]", vertical="middle"), style="white", border_style="yellow", box=HEAVY))
        # Wait for user input to continue or quit
        self.wait_for_start()

    #✅ Working
    def wait_for_start(self):
        user_input = input().strip().lower()

        if user_input == 'q':
            self.console.print("[bold red]Game exited. Goodbye![/bold red]", style="white")
            sys.exit()  # Quit the program
        else:
            self.console.print("[bold green]Game starting...[/bold green]", style="white")

# =========================================================================================


# ==================================== Battle related ====================================
    #✅ Working
    def display_battle_results(self, player_1, player_2, battle_data) -> None:
        def print_winner(winner_message, border_style):
            # Helper function to print winner announcement and health update
            self.console.print(Panel(Align.center(winner_message), border_style=border_style))
            time.sleep(3)
            os.system('cls')

            self.console.print(Align.center("\n[bold green]Health Update[/bold green]\n"))
            self.print_dual_panel(
            f"[bold blue]{player_1.current_pokemon[0]}:[/bold blue] [bold white]{battle_data['player_1_original_health']}[/bold white] -> "
            f"[{'bold green' if battle_data['winner'] == 'player 1' else 'bold red'}]{player_1.current_pokemon[1]}[/{'bold green' if battle_data['winner'] == 'player 1' else 'bold red'}]",
            player_1_emoji, "blue",
            f"[bold red]{player_2.current_pokemon[0]}:[/bold red] [bold white]{battle_data['player_2_original_health']}[/bold white] -> "
            f"[{'bold green' if battle_data['winner'] == 'player 2' else 'bold red'}]{player_2.current_pokemon[1]}[/{'bold green' if battle_data['winner'] == 'player 2' else 'bold red'}]",
            player_2_emoji, "red"
        )

        # Start battle message
        self.console.print(Align.center(f"[bold yellow]Battle {self.backend.battle_count}![/bold yellow]", vertical="middle"))

        # Display Pokemon information using dual panels
        self.print_dual_panel(
            f"{player_1.current_pokemon[0]}", "[bold]Player 1[/bold]", "blue",
            f"{player_2.current_pokemon[0]}", "[bold]Player 2[/bold]", "red"
        )

        time.sleep(3)
        # Determine and print winner or draw
        if battle_data["winner"] == "player 1":
            self.console.print(
                Panel(Align.center(f"[bold yellow]{player_1.current_pokemon[2]}[/bold yellow] > {player_2.current_pokemon[2]}"), 
                border_style="blue")
            )
            winner_message = "🏆[bold blue]Player 1[/bold blue] wins!🏆"
            player_1_emoji, player_2_emoji = "🏆", "🔥"
        

        elif battle_data["winner"] == "player 2":
            self.console.print(
                Panel(Align.center(f"{player_1.current_pokemon[2]} < [bold yellow]{player_2.current_pokemon[2]}[/bold yellow]"), 
                border_style="red")
            )
            winner_message = "🏆[bold red]Player 2[/bold red] wins!🏆"
            player_1_emoji, player_2_emoji = "🔥", "🏆"
        

        else:
            self.console.print(
                Panel(Align.center(f"{player_1.current_pokemon[2]} = {player_2.current_pokemon[2]}"), 
                border_style="yellow")
            )
            winner_message = "🔥[bold yellow]It's a draw![/bold yellow]🔥"
            player_1_emoji = player_2_emoji = "🔥"
        time.sleep(3)

        # Print winner message and health updates
        print_winner(winner_message, "yellow")
        time.sleep(4)
        

    #✅ Working
    def fatigue_factor_display(self, player_1, player_2):    
        # Decrease health of both current Pokemon by 2
        player_1_health_adjustment = max(0, int(player_1.current_pokemon[1]) - 2)
        player_2_health_adjustment = max(0, int(player_2.current_pokemon[1]) - 2)

        # Message and style configuration for both players
        player1_message = f"[bold blue]{player_1.current_pokemon[0]}:[/bold blue] [bold white]{player_1.current_pokemon[1]}[/bold white] -> [bold red]{player_1_health_adjustment}[/bold red]"
        player2_message = f"[bold red]{player_2.current_pokemon[0]}:[/bold red] [bold white]{player_2.current_pokemon[1]}[/bold white] -> [bold red]{player_2_health_adjustment}[/bold red]"
        player1_title = "[bold]Player 1[/bold]"
        player2_title = "[bold]Player 2[/bold]"
        player1_style = "blue"
        player2_style = "red"

        # Display fatigue information using dual panel
        os.system('cls')
        self.console.print(Align.center("\nAll pokemons feel [bold red]fatigued...[bold red]", vertical="middle"))
        self.console.print(Align.center("[italic grey]all pokemon suffered [red]-2 health[/red] points[italic grey]\n", vertical="middle"))
        self.print_dual_panel(
            player1_message, player1_title, player1_style,
            player2_message, player2_title, player2_style
        )

        # Add delay and clear screen
        time.sleep(6)
        os.system('cls')





    #✅ Working
    def pokemon_battle(self, player_1, player_2) -> None:
        os.system('cls')  # Clear terminal

        battle_data = self.backend.handle_battle(player_1, player_2)
        self.display_battle_results(player_1, player_2, battle_data)

        # Log battle in a data frame
        self.backend.add_battle(player_1.current_pokemon, player_2.current_pokemon, battle_data["winner"])


    #✅ Working
    def potion_or_poison_display(self, player, player_name, backend):
        # Handles the frontend display for potion or poison interaction with the player
        rand_val = self.backend.potion_or_poison_calculation(player)

        

        # Blessing message
        message = f"[white]     An 👼 blessed your pokemon!\nYour [bold green]{player.current_pokemon[0]}[/bold green] received [/white][bold]{rand_val} blessings![/bold]"
        self.print_panel(message, f"{player_name} Blessings!", "yellow")

        self.console.print("\n🧙: Would you like to trade your [bold yellow]blessings[/bold yellow] for a [bold purple]random effect?[/bold purple]\n")

        try:
            user_choice = input("[Y/N]: ").strip().lower()
            if user_choice not in ["y", "n"]:
                raise ValueError("Invalid choice. Please enter 'Y' or 'N'.")

            os.system('cls')

            if user_choice == "y":
                self.print_panel("[bold]🧙 casted a [purple]spell...[/purple][/bold]", "✨Random Effect✨", "blue")
                time.sleep(2)

                # Determine if the effect is poison or potion
                effect = random.choice(["poison", "potion"])
                new_power = max(0, int(player.current_pokemon[2]) + (rand_val if effect == "potion" else -rand_val))
                
                # Prepare the effect panel message with correct markup
                effect_title = "💔Poison💔" if effect == "poison" else "💚Potion💚"
                if effect == "poison":
                    effect_message = (
                        f"Your blessing turned into [bold red]poison![/bold red] {player.current_pokemon[0]} lost power!"
                    )
                    power_change_message = (
                        f"[bold green]{player.current_pokemon[0]}'s[/bold green] power: [bold]{player.current_pokemon[2]}[/bold] -> "
                        f"[bold red]{new_power}[/bold red]"
                    )
                else:
                    effect_message = (
                        f"Your blessing turned into [bold green]potion![/bold green] {player.current_pokemon[0]} gained power!"
                    )
                    power_change_message = (
                        f"[bold green]{player.current_pokemon[0]}'s[/bold green] power: [bold]{player.current_pokemon[2]}[/bold] -> "
                        f"[bold green]{new_power}[/bold green]"
                    )
                player.current_pokemon[2] = new_power

                # Print the effect panel
                self.print_panel(f"{effect_message}\n{power_change_message}", effect_title, "white")
                time.sleep(2)

                # Reset the blessing value
                player.current_pokemon[3] = 0
                self.console.print("\n[bold yellow]The blessing has been used and is now reset to 0.[/bold yellow]")
            else:
                print("\nYou kept your blessings untouched.")

            time.sleep(4)
            os.system('cls')

        except ValueError as e:
            print(f"Error: {e}. Please try again.")
            self.potion_or_poison_display(player, player_name, backend)  # Retry on error



# =========================================================================================





# ==================================== Selection related ==================================

    #✅ Working
    def display_selected_pokemon(self, player):
        # Display the player's selected Pokemon with green names
        # Start the message with "Player 1 Selected Pokemon: " in white
        message = Text("Player 1 Selected Pokemon: ", style="white")

        # Append each Pokemon name in green, separated by commas
        for idx, pokemon in enumerate(player.pokemons):
            message.append(f"{pokemon[0]}", style="green")
            if idx < len(player.pokemons) - 1:  # Add a comma if not the last Pokemon
                message.append(", ", style="white")

        # Print the styled message to the console
        self.console.print(message)


    #✅ Working
    def display_pokemon_array(self):
        # Display the Pokemon array from backend using a rich table
        # Create a rich table with a heavy border
        table = Table(border_style="bold white", box=HEAVY, title="Available Pokemon")

        # Add columns for the Pokemon attributes
        table.add_column("Index", justify="center")
        table.add_column("Name", justify="center")
        table.add_column("Health", justify="center")
        table.add_column("Power", justify="center")

        # Populate the table with Pokemon data from backend
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
    def display_player_pokemons(self, player, player_name):
        # Display the player's available Pokemon using a rich table
        if player.pokemons.size == 0:
            self.console.print("[bold red]You have no available Pokemon to select.[/bold red]")
            return False  # Return if no Pokemon are available
        
        # Create a rich table with a heavy border
        table = Table(border_style="bold white", box=HEAVY, title=f"[bold green]{player_name}'s pokemon[/bold green]")

        # Add columns for Pokemon attributes
        table.add_column("Index", justify="center")
        table.add_column("Name", justify="center")
        table.add_column("Health", justify="center")
        table.add_column("Power", justify="center")

        # Populate the table with Pokemon data
        for idx, pokemon in enumerate(player.pokemons):
            table.add_row(
                str(idx),
                str(pokemon[0]),
                str(pokemon[1]),
                str(pokemon[2])
            )

        # Print the table to the console
        self.console.print(table)
        return True  # Return True if there are available Pokemon


    #✅ Working
    def display_battle_summary(self, battle_summary):
        # Create a rich table with a heavy border
        table = Table(border_style="bold white", box=HEAVY)

        # Add columns to the table
        for column in battle_summary.columns:
            table.add_column(column, justify="center")

        # Add rows to the table (if any)
        for _, row in battle_summary.iterrows():
            table.add_row(*[str(item) for item in row])

        # Print the table using rich
        self.console.print(Align.center(table), style="white")


    # ✅ Working
    def end_game(self, player_1, player_2) -> None:
        os.system('cls')

        # Print the panel with centered alignment
        self.console.print(Panel(Align.center("Battle Summary", vertical="middle"), style="white", border_style="yellow", box=HEAVY))
        
        self.print_dual_panel(
            f"Win: {player_1.wins}", "[bold]Player 1[/bold]", "blue",
            f"Win: {player_2.wins}", "[bold]Player 2[/bold]", "red"
        )

        # Fetch the latest battle summary and display it
        battle_summary = self.backend.battle_summary
        if battle_summary.empty:
            self.console.print("[bold yellow]No battles were recorded.[/bold yellow]")
        else:
            self.display_battle_summary(battle_summary)

        # Overall champion
        overall_champion = self.backend.get_overall_winner()
        self.console.print(Panel(Align.center(f"[bold]  champion[/bold]:\n[bold yellow]🏆{overall_champion}🏆[/bold yellow]", vertical="middle"), style="white", border_style="yellow", box=HEAVY))
        

        # Print a thank-you message in green
        self.console.print(Align.center("\n\nThank you for playing!\n\n", vertical="middle"), style="green")


        time.sleep(10)
        os._exit(0)

    
# =========================================================================================





# ==================================== Input related =====================================

    #✅ Working
    def player_pokemon_selection(self, player, max_pick, restricted_pick=False) -> None: 
        # Handle player Pokemon selection with backend logic
        while True:
            try:
                os.system('cls')

                # Display the available Pokemon
                self.display_pokemon_array()

                # Get input from player (space-separated indexes)
                player_picks = list(map(int, input(f"Pick from 1 to {max_pick} Pokemon: ").split()))


                # Validate the number of picks
                if restricted_pick and len(player_picks) != max_pick:
                    error_message = Text(f"You must pick exactly {max_pick} Pokemon. Try again.", style="red")
                    self.console.print(error_message)
                    time.sleep(2)
                    continue

                if not restricted_pick and not (1 <= len(player_picks) <= max_pick):
                    error_message = Text(f"You must pick between 1 and {max_pick} Pokemon. Try again.", style="red")
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

                # Display the selected Pokemon
                self.display_selected_pokemon(player)
                time.sleep(2)

                break  # Exit loop on successful selection

            except ValueError as e:
                self.console.print(f"[bold red]Invalid input:[/bold red] {e}. Please try again.")
                time.sleep(2)


    #✅ Working
    def choose_battle_pokemon(self, player, player_name):
        # Handle the display and selection of a Pokemon for battle
        os.system('cls')

        # Display available Pokemon using Rich table
        if not self.display_player_pokemons(player, player_name):
            return  # Exit if no Pokemon are available

        while True:
            try:
                self.backend.choose_battle_pokemon(player)
                self.console.print(f"[bold green]You selected {player.current_pokemon[0]} for battle![/bold green]")
                break  # Exit loop on successful selection

            except ValueError as e:
                self.console.print(f"[bold red]Error: {e}. Please enter a valid number.[/bold red]")

        time.sleep(2)


    #✅ Working
    def prompt_pokemon_change(self, player, player_name) -> bool:
        if player.pokemons.size == 0:
            self.console.print(f"[bold red]{player_name}, you have no available Pokemon to change.[/bold red]")
            return False  # No Pokemon available

        while True:
            self.console.print(
                f"[bold cyan]{player_name}[/bold cyan]: Would you like to change your [bold red]battle Pokemon?[/bold red] [Y/N]: ", 
                end=""
            )
            # Collect the user input
            user_choice = input().strip().lower()

            if user_choice in ["y", "n"]:
                if user_choice == "y":
                    self.change_battle_pokemon(player)  # Perform the swap
                    return True  # Pokemon was changed
                return False  # Keep the current Pokemon
            else:
                self.console.print("[bold red]Invalid choice. Please enter 'Y' or 'N'.[/bold red]")


    #✅ Working
    def pokemon_change_prompt(self):
        for player, name in [(self.backend.player_1, "Player 1"), (self.backend.player_2, "Player 2")]:
            if not self.prompt_pokemon_change(player, name):
                self.console.print(f"[bold gray italic]{name} keeps the same Pokemon.[/bold gray italic]")


    #✅ Working
    def change_battle_pokemon(self, player) -> None:
        # Allows the player to swap their current battle Pokemon with one from their available Pokemon
        try:
            # Helper function to create and print a styled panel
            def print_panel(message, title, style, width_fraction=2):
                console_width = self.console.size.width // width_fraction
                aligned_message = Align.center(message)
                panel = Panel(
                    aligned_message,
                    title=title,
                    style=style,
                    border_style=style,
                    box=HEAVY,
                    width=console_width,
                    padding=(1, 1)
                )
                self.console.print(panel, justify="left")

            # Create a message with available Pokémon and their details
            message = "\n".join(
                f"[bold white][bold yellow]{i}[/bold yellow]: {pokemon[0]} "
                f"Health: [bold green]{pokemon[1]}[/bold green], "
                f"Power: [bold red]{pokemon[2]}[/bold red][/bold white]"
                for i, pokemon in enumerate(player.pokemons)
            )

            # Print the styled panel with Pokémon details
            print_panel(message, "[italic]Available Pokemon[/italic]", "blue")


            # Ask the user to select the index of the Pokemon to swap
            index = int(input("Select your new battle Pokemon: "))

            # Validate the input index
            if index < 0 or index >= len(player.pokemons):
                raise ValueError("Invalid index. Please select a valid Pokemon.")

            # If there's already a Pokemon in `current_pokemon`, add it back to the list
            if player.current_pokemon is not None and player.current_pokemon.size > 0:
                player.pokemons = np.vstack([player.pokemons, player.current_pokemon])

            # Update `current_pokemon` with the selected Pokemon
            player.current_pokemon = player.pokemons[index]

            # Remove the selected Pokemon from `pokemons`
            player.pokemons = np.delete(player.pokemons, index, axis=0)

            self.console.print(f"\n[bold green]{player.current_pokemon[0]}[/bold green] is now ready for battle!\n")
            player.used_pokemons += 1
            time.sleep(3)
            os.system('cls')

        except ValueError as e:
            self.console.print(f"[red]Error: {e}. Please try again.[/red]")


    #✅ Working
    def check_all_pokemons_used(self):
        # Checks if all Pokemon have been used and prompts the user to continue or end the battle.
        if (
            self.backend.player_1.used_pokemons == len(self.backend.player_1.pokemons)
            and self.backend.player_2.used_pokemons == len(self.backend.player_2.pokemons)
        ):
            try:
                end_message = Text("All pokémons were used in the battle.\n", style="blue")
                self.console.print(end_message)

                user_choice = input("Would you like to continue the battle? [Y/N]: ").strip().lower()

                if user_choice not in ["y", "n"]:
                    raise ValueError("Invalid choice. Please enter 'Y' or 'N'.")

                return user_choice == "y"  # Returns True if 'Y', False if 'N'
            
            except ValueError as e:
                self.console.print(f"[bold red]Error: {e}. Please Try again.[/bold red]")
                return self.check_all_pokemons_used()  # Retry on error
        else:
            return True  # Continue if not all Pokemon are used


# =========================================================================================





# Debugging
# if __name__ == "__main__":
#     backend_instance = Backend()    
#     f = Frontend(backend_instance) 
#     f.intro()

#     f.backend.add_battle(["Pikachu", 100, 50], ["Charizard", 120, 60], "Player 1")
#     f.backend.add_battle(["Pikachu", 100, 50], ["Charizard", 120, 60], "Player 2")
#     f.backend.add_battle(["Pikachu", 100, 50], ["Charizard", 120, 60], "Player 3")
#     f.backend.add_battle(["Pikachu", 100, 50], ["Charizard", 120, 60], "Player 4")
    
#     f.end_game()

    