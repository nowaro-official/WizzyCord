from typing import Mapping, Optional
import discord
from discord.ext import commands
from .embed import EmbedTemplate

class HelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping: Mapping[Optional[commands.Cog], list[commands.Command]]):
        embed = EmbedTemplate.create_embed(
            title="Bot Hilfe",
            description="Hier ist eine Liste aller verfügbaren Befehle:",
            color=discord.Color.green()
        )

        for cog, cmds in mapping.items():
            command_list = [cmd.name for cmd in await self.filter_commands(cmds, sort=True)]
            if command_list:
                cog_name = getattr(cog, "qualified_name", "Keine Kategorie")
                embed.add_field(name=cog_name, value=", ".join(command_list), inline=False)

        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command: commands.Command):
        embed = EmbedTemplate.create_embed(
            title=f"Hilfe für {command.name}",
            description=command.help or "Keine Beschreibung verfügbar.",
            color=discord.Color.blue()
        )
        embed.add_field(name="Verwendung", value=f"`{self.get_command_signature(command)}`")

        await self.get_destination().send(embed=embed)

def setup(bot: commands.Bot):
    bot.help_command = HelpCommand()
