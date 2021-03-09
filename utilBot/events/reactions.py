# -*- coding: UTF-8 -*-
from typing import Optional

from discord import Client, Guild, Member, RawReactionActionEvent, Role


async def raw_reaction_add(
    payload: RawReactionActionEvent, data_tree: dict, client: Client
):
    assert isinstance(payload.emoji.name, str)
    emoji_name: str = payload.emoji.name
    message_id: int = payload.message_id

    if data_tree[message_id][emoji_name]:
        assert isinstance(payload.guild_id, int)
        guild_id: int = payload.guild_id
        guild: Optional[Guild] = client.get_guild(guild_id)
        assert isinstance(guild, Guild)

        grant_role_id: int = data_tree[message_id][emoji_name]
        grant_role: Optional[Role] = guild.get_role(grant_role_id)

        if isinstance(grant_role, Role):
            assert isinstance(payload.member, Member)
            member: Member = payload.member
            await member.add_roles(
                grant_role,
                reason="Self-Assignment using Reaction "
                + f"'{emoji_name}' on message '{message_id}",
            )
        else:
            print(
                f"Invalid roleID '{grant_role_id}' for reaction "
                + "'{emoji_name}' on message {message_id}!"
            )


async def raw_reaction_remove(
    payload: RawReactionActionEvent, data_tree: dict, client: Client
):
    assert isinstance(payload.emoji.name, str)
    emoji_name: str = payload.emoji.name
    message_id: int = payload.message_id

    if data_tree[message_id][emoji_name]:
        assert isinstance(payload.guild_id, int)
        guild_id: int = payload.guild_id
        guild: Optional[Guild] = client.get_guild(guild_id)
        assert isinstance(guild, Guild)

        remove_role_id: int = data_tree[message_id][emoji_name]
        remove_role: Optional[Role] = guild.get_role(remove_role_id)

        if isinstance(remove_role, Role):
            assert isinstance(payload.member, Member)
            member: Member = payload.member
            await member.remove_roles(
                remove_role,
                reason="Self-Removal using Reaction "
                + f"'{emoji_name}' on message '{message_id}'",
            )