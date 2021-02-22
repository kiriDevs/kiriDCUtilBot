from discord.ext.commands import Bot, Context
from yaml import safe_load as load_yaml

from commands.clear_command import clear_command

with open("../config/credentials.yml", "r") as credential_file:
    AUTH_TOKEN: str = load_yaml(credential_file)["DISCORD_BOT_TOKEN"]

with open("../config/config.yml", "r") as config_file:
    raw_prefix: str = load_yaml(config_file)["prefix"]
    raw_prefix_with_space: str = raw_prefix + " "
    PREFIXES: tuple = (raw_prefix_with_space, raw_prefix)

bot: Bot = Bot(command_prefix=PREFIXES, case_insensitive=True)


@bot.command(name="clear")
async def clear_chat(ctx: Context, message_amount_string: str):
    await clear_command(ctx, message_amount_string)


bot.run(AUTH_TOKEN)
