# Pokemon Battle Game


Welcome to the **Pokemon Battle Game**, an interactive command-line game where players select, battle, and manage Pokemon to compete in thrilling battles! This project consists of three main components: `backend.py`, `frontend.py`, and `main.py`. Each module contributes to creating a seamless gameplay experience, handling player selection, battle logic, and console-based UI using the `rich` library.

---
## Snapshots
![image](https://github.com/user-attachments/assets/47bbea72-7ad8-4e8a-a0e1-3578ad8f9611)
![image](https://github.com/user-attachments/assets/402420bc-994d-4c55-9d34-2abc6551bbca)
![image](https://github.com/user-attachments/assets/0cd4632d-b0e7-4f5b-86ce-139f1b6b0cd9)
![image](https://github.com/user-attachments/assets/c4630c55-e124-4d10-9161-f14309c5a574)



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
- `Player Pokemon Selection`: Players choose their Pokemon from a list.

- `Battle Preparation`: Players are prompted to select Pokemon for each battle.

- `Battle Execution`: The game processes battle results, applies fatigue, and health changes.

- `Potion/Poison Even`t`: Players may receive blessings, with a chance of being transformed into potions or poisons.

- `End Game`: A summary of all battles is displayed at the end.

## Modules
### main.py
This is the entry point of the game. It initializes the backend and frontend systems and starts the gameplay.

**Key Functions:**
- `Gameplay.run()`: Main loop handling the flow from Pokemon selection to battles.
- `Gameplay.loading_text()`: Displays loading animations.

### frontend.py
Handles all console outputs and user interactions using the rich library.

**Key Features:**
- `display_pokemon_array()`: Shows available Pokemon with stats in a styled table.
- `player_pokemon_selection()`: Collects player input for Pokemon selection.
- `pokemon_battle()`: Displays battle results and logs them.
- `potion_or_poison_display()`: Handles potion or poison events with blessings.
- `end_game()`: Displays the battle summary and concludes the game.

### backend.py
Manages game logic, player data, and battle summaries.

**Key Components:**
- `Player Class`: Stores each player’s Pokemon and battle state.
- `Backend Class`:
    - Handles Pokemon selection and battle logic.
    - Manages health, fatigue, and random events.
    - Logs each battle in a DataFrame for summary at the end.

## Features
- `Dynamic Pokemon Selection`: Choose from a variety of Pokemon with unique stats.
- `Battle System`: Compare Pokemon power to determine winners.
- `Health and Fatigue Management`: Players' Pokemon lose health over time.
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
