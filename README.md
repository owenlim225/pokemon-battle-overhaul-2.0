# Pokémon Battle Game

Welcome to the **Pokémon Battle Game**, an interactive command-line game where players select, battle, and manage Pokémon to compete in thrilling battles! This project consists of three main components: `backend.py`, `frontend.py`, and `main.py`. Each module contributes to creating a seamless gameplay experience, handling player selection, battle logic, and console-based UI using the `rich` library.

---

## Table of Contents

- [Installation](#installation)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [Gameplay Flow](#gameplay-flow)
- [Modules](#modules)
  - [main.py](#mainpy)
  - [frontend.py](#frontendpy)
  - [backend.py](#backendpy)
- [Features](#features)
- [Requirements](#requirements)
- [License](#license)

---

## Installation

Make sure you have Python installed. If not, download and install it from [Python's official website](https://www.python.org/).

Clone the repository and install dependencies:

```bash
git clone <your-repository-url>
cd <your-project-directory>
pip install -r requirements.txt
```

## How to Run
After installation, you can start the game by executing the following command:

```bash
python main.py
```

## Project Structure

```bash
.
├── main.py          # Entry point of the game
├── backend.py       # Backend logic including player data and battle handling
├── frontend.py      # Console interface using rich library
└── requirements.txt # Python dependencies
```

## Gameplay Flow
- `Player Pokémon Selection`: Players choose their Pokémon from a list.

- `Battle Preparation`: Players are prompted to select Pokémon for each battle.

- `Battle Execution`: The game processes battle results, applies fatigue, and health changes.

- `Potion/Poison Even`t`: Players may receive blessings, with a chance of being transformed into potions or poisons.

- `End Game`: A summary of all battles is displayed at the end.

## Modules
### main.py
This is the entry point of the game. It initializes the backend and frontend systems and starts the gameplay.

**Key Functions:**
- `Gameplay.run()`: Main loop handling the flow from Pokémon selection to battles.
- `Gameplay.loading_text()`: Displays loading animations.

### frontend.py
Handles all console outputs and user interactions using the rich library.

**Key Features:**
- `display_pokemon_array()`: Shows available Pokémon with stats in a styled table.
- `player_pokemon_selection()`: Collects player input for Pokémon selection.
- `pokemon_battle()`: Displays battle results and logs them.
- `potion_or_poison_display()`: Handles potion or poison events with blessings.
- `end_game()`: Displays the battle summary and concludes the game.

### backend.py
Manages game logic, player data, and battle summaries.

**Key Components:**
- `Player Class`: Stores each player’s Pokémon and battle state.
- `Backend Class`:
    - Handles Pokémon selection and battle logic.
    - Manages health, fatigue, and random events.
    - Logs each battle in a DataFrame for summary at the end.

## Features
- `Dynamic Pokémon Selection`: Choose from a variety of Pokémon with unique stats.
- `Battle System`: Compare Pokémon power to determine winners.
- `Health and Fatigue Management`: Players' Pokémon lose health over time.
- `Potion/Poison Events`: Random blessings with risks of negative effects.
- `Battle Summary`: View a detailed summary at the end of the game.
- `Console UI with Rich`: Beautifully formatted tables, panels, and text.

## Requirements
Install the required Python packages by running:
```bash
pip install -r requirements.txt
```

### Dependencies:
- `rich`: For beautiful console outputs.
- `numpy`: For efficient data manipulation.
- `pandas`: For battle summary management.


## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you wish.

Enjoy the game! If you encounter any issues or have suggestions for improvements, feel free to contribute or raise an issue. Happy battling! 🎮