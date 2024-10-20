
# Discord Self-Bot: Number and Brand Guessing Automation

This Discord self-bot automates the process of guessing numbers or random brands in a Discord channel. It can be used to participate in prized events where the objective is to guess a random number or a brand name.

## Features
- **Number Guessing Mode:** Automatically attempts to guess random numbers from a specified range.
- **Brand Guessing Mode:** Automatically attempts to guess brands from a provided list.
- Adjusts rate-limiting automatically to comply with Discord's rate limits.
- Logs attempts and successful actions.
  
## Files

### 1. `main.py`
This is the core of the bot, handling the guessing logic, user interaction, and Discord events.

### 2. `config.json`
This configuration file contains bot settings like the token and channel ID.

Example:
```json
{
  "token": "YOUR_BOT_TOKEN",
  "channelID": 123456789012345678,
  "brainNamesTXT": "brands.txt"
}
```

- `token`: The bot token from Discord's developer portal.
- `channelID`: The ID of the Discord channel where the bot will operate.
- `brainNamesTXT`: The text file that contains a list of brands to guess.

### 3. `brands.txt`
This text file contains the list of brand names (one per line) for the bot to attempt in the brand guessing mode.

Example:
```
Nike
Adidas
Puma
```

### 4. `PyUtls.py`
A custom utility module that handles logging, input prompts, and system-related functions.

## Setup

### 1. Install Required Libraries

Make sure you have Python 3.8+ installed, then install the required dependencies:

```bash
pip install discord.py-self
```

### 2. Configure the Bot

Edit the `config.json` file with your bot's token and the ID of the Discord channel where it will guess numbers or brands.

### 3. Add Your Brand List

If you are using the brand guessing mode, add the list of brands to the `brands.txt` file (one brand per line).

### 4. Run the Bot

To start the bot, simply run:

```bash
python main.py
```

You will be prompted to choose between:
1. Number guessing mode (where you specify a range).
2. Brand guessing mode (where the bot reads from the `brands.txt` file).

### 5. Log Output

The bot will log actions and outcomes to the console, helping you track attempts, rate-limit warnings, and other useful information.

## Usage

When the bot is active:
- **Number Guessing Mode:** The bot will randomly guess numbers within a specified range in the designated Discord channel.
- **Brand Guessing Mode:** The bot will attempt to guess random brands from the list provided in `brands.txt`.

## Extra info

This project is for educational and personal use. Please ensure that you comply with Discord's Terms of Service, which restrict the use of self-bots on their platform.
all of this  ^^^ was chat gpt, dm me if u got questions `gs._`
