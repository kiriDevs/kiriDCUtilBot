# -*- coding: UTF-8 -*-
from discord import RawReactionActionEvent
from discord.ext.commands import Bot, Context
from yaml import safe_load as load_yaml

from utilBot.commands.clear_command import clear_command
from utilBot.events.reactions import raw_reaction_add, raw_reaction_remove

with open("../config/credentials.yml", "r") as credential_file:
    AUTH_TOKEN: str = load_yaml(credential_file)["DISCORD_BOT_TOKEN"]

with open("../config/config.yml", "r") as config_file:
    raw_prefix: str = load_yaml(config_file)["prefix"]
    raw_prefix_with_space: str = raw_prefix + " "
    PREFIXES: tuple = (raw_prefix_with_space, raw_prefix)

with open(
    "../config/reactionroles.yml", "r", encoding="UTF-8"
) as reaction_role_file:
    REACTION_DATA_TREE = load_yaml(reaction_role_file)
    print(REACTION_DATA_TREE)

bot: Bot = Bot(command_prefix=PREFIXES, case_insensitive=True)


@bot.command(name="clear")
async def clear_chat(ctx: Context, message_amount_string: str):
    await clear_command(ctx, message_amount_string)


@bot.event
async def on_raw_reaction_add(payload: RawReactionActionEvent):
    global REACTION_DATA_TREE
    await raw_reaction_add(payload, REACTION_DATA_TREE, bot)


async def on_raw_reaction_remove(payload: RawReactionActionEvent):
    global REACTION_DATA_TREE
    await raw_reaction_remove(payload, REACTION_DATA_TREE, bot)


bot.run(AUTH_TOKEN)
