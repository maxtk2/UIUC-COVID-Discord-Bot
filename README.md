# UIUC COVID Discord Bot
## Authors: Max Knutson & Thailer Lietz

This is a Discord bot that periodically retrieves data from the [UIUC On-Campus COVID-19 Testing Data Dashboard](https://go.illinois.edu/COVIDTestingData). The user can see this data through summaries and graphs through various commands. An explanation of the data retrieved can be found on [this webpage](https://covid19.illinois.edu/on-campus-covid-19-testing-data-dashboard/).

![example](https://github.com/maxtk2/UIUC-COVID-Discord-Bot/blob/main/Example%20Images/Basic%20functionality.JPG?raw=true)

Contact me if you want this bot in your server! My email is maxtk2@illinois.edu.

## Commands
- -ping: Prints the ping of the bot.
- -data: Prints an embed containing a summary of COVID data.

## Getting Started

### Requirements
- Python 3.8.5
- discord</k>.py 1.6.0
- playwright 0.171.1
- pandas 1.2.0

### Setting Up
1. [Create a Discord bot and invite it to your server.](https://discordpy.readthedocs.io/en/latest/discord.html)
2. Clone this repo and go to its directory.
    ```
    git clone https://github.com/maxtk2/UIUC-COVID-Discord-Bot.git
    cd UIUC-COVID-Discord-Bot/
    ```
3. Copy the file `config_example.py` as `config.py`.
    ```
    cp config_example.py config.py
    ```
4. In `config.py`, assign the `token` variable to be your bot's token.
5. Run `main.py`.
    ```
    python3 main.py
    ```
