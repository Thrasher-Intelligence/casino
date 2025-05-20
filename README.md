# Nasty Boyz Casino App

A command-line casino game application that currently features poker.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.6 or higher
- Git

### Clone the Repository

If you're new to Git, here's how to clone this repository to your local machine:

```bash
# Open your terminal/command prompt and navigate to where you want to store the project
# Then run this command to clone the repository
git clone https://github.com/yourusername/casino.git

# Navigate into the project directory
cd casino
```

### Setting Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Running the Game

Once you have cloned the repository and set up your environment, you can run the game with:

```bash
# Make sure you're in the casino directory
python main.py
```

Follow the on-screen prompts to select and play a game.

## Available Games

1. **Poker** - Classic poker game

## Project Structure

- `engine/` - Core game mechanics and card utilities
- `games/` - Individual game implementations
- `ui/` - User interface components

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or new games.

## License

This project is licensed under the MIT License - see the LICENSE file for details.