from typing import List

from discord import Message, TextChannel
from discord.ext.commands import Context


async def clear_command(ctx: Context, message_amount_string: str):
    if not isinstance(ctx.channel, TextChannel):
        await ctx.send(
            "This command can only be used in a TextChannel on a server!"
        )
        return

    try:
        message_amount: int = int(message_amount_string)
    except ValueError:
        await ctx.send("Please enter a valid number of messages to delete!")
        return

    message_amount += 1  # Adding one for the message that contains the command

    deleted_messages: List[Message] = await ctx.channel.purge(
        limit=message_amount
    )
    deleted_number: int = len(deleted_messages)
    await ctx.send(
        f"**Success**! Deleted {deleted_number} messages!", delete_after=3
    )

    # Cleanup - Removing potentially larger variables from RAM
    del deleted_messages
