# kiriDCUtilBot
A simple Discord bot written in Python, using [discord.py](https://discordpy.readthedocs.io), supposed to provide you
with basic tools that can be of use on many Discord servers, not depending on their type or purpose. Everyone is invited
to comment on my code, report any mistakes / bugs or suggest new features, or even implement them themselves.



# Content
1. [Key Features](#key-features)
2. [Hosting](#hosting)
3. [Setup instructions](#setup-instructions)
    1. [Install all dependencies on your system](#install-all-dependencies-on-your-system)
        1. [Manually using pip](#manually-using-pip)
        2. [Automatically using pipenv](#automatically-using-pipenv)
    2. [Download the source code to your system](#download-the-source-code-to-your-system)
    3. [Configuration](#configuration)
4. [Running the bot](#running-the-bot)



# Key Features
- All configuration is saved per Discord-Server, allowing for use on multiple servers without hosting multiple instances
- Configurable command prefix (Especially useful on larger servers with multiple bots)
- Complete configurability of all settings per server 
- Open Source



# Hosting
For the time being, I will not host a public instance of the Discord-Bot myself. Therefore, to use it, you have to 
download the source code found in this repository to a machine that you want to host your own instance on. A simple
[Raspberry Pi](https://raspberrypi.org) should be enough for this use case. Since it comes with Python preinstalled and
is very small, it is a great 24/7 computer to run things like this on.



# Setup instructions
Since I will not host a public instance of this bot, you will have to host your own instance on a computer, as stated
[above](#hosting). Here are some basic instructions to get you started:

## Install all dependencies on your system
### Manually using pip
-- Dependencies following shortly --

### Automatically using pipenv
- Run `pip install pipenv` to install the "pipenv" package from pip, if not already done
- Do Step 3.2 ([Download the source code to your system](#download-the-source-code-to-your-system))
- Run `pipenv install` to create a new virtual environment and have pipenv download all necessary packages automatically
  based on the `Pipfile.lock` inluded with the code.


## Download the source code to your system
- Through git clone: `git clone https://github.com/kiriDevs/kiriDCUtilBot`
- By clicking on `Download Code` on the [GitHub Repositiory Page](https://github.com/kiriDevs/kiriDCUtilBot) and
  extracting the downloaded archive in a new folder
   
  
## Configuration
1. Fill out credentials in `credentials.yml`
    - `DISCORD_BOT_TOKEN`
        1. Go to [Discord's Developer Portal](https://discord.com/developers)
        2. Log in with your Discord account (if you aren't already)
        3. Create a new application (This will also be the default name for your bot, but you can change them
           independently later)
        4. In the menu for your new app, go to the "Bot" section in the left-hand menu
        5. Click on "Add Bot" to create a bot account for your application
        6. If you only want to use the bot for yourself, you will want to turn of "Public Bot" so only you can add
           your bot to new servers.
        7. Under "Token", click on "Click to Reveal Token" to reveal your bot token
        8. Copy it into the `credentials.yml`, next to `DISCORD_BOT_TOKEN: `
        9. Do any other settings you might want to do (bot's username, icon, ...). You can still change these
           settings later.
        10. Go to the "OAuth2" menu in the left sidebar.
        11. Scroll down and check the checkbox next to "bot" in the "Scopes" section.
        12. Copy the link below the checkboxes and open it in a browser to add your bot to a server.

# Running the bot
Since the bot needs to continue to run if you log out, you can't just execute the Python file and leave. To keep the
python instance with the bot running, I recomment using `screen`. Screen is an easy-to-use tool for most Linux and
MacOS-Systems. To install it, use `sudo apt-get install screen`. Afterwards, you can use
`screen -AmdS discordBot python3 /path/to/source/code/utilBot.py` to create a new screen instance in detached state,
with the name "discordBot", running the command `python3 /path/to/source/code/utilBot.py`. If you want to see what's
happening in the console of this hidden terminal, use `screen -x discordBot`, if you called the screen "discordBot"
before. To detach again, press `CTRL + A`, then `CTRL + D`. To stop the bot, attach using `screen -x discordBot`, then
press `CTRL + C`.

**Your bot will now run until the computer is turned off, a critical error occurs or you stop it.**
