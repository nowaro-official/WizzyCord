import discord
from discord.ext import commands
from .embed import EmbedTemplate

class HelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        embed = EmbedTemplate.create_embed(
            title="Bot Hilfe",
            description="Hier ist eine Liste aller verfügbaren Befehle:",
            color=discord.Color.green()
        )

        for cog, commands in mapping.items():
            command_list = [command.name for command in commands if not command.hidden]
            if command_list:
                cog_name = getattr(cog, "qualified_name", "Keine Kategorie")
                embed.add_field(name=cog_name, value=", ".join(command_list), inline=False)

        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
        embed = EmbedTemplate.create_embed(
            title=f"Hilfe für {command.name}",
            description=command.help or "Keine Beschreibung verfügbar.",
            color=discord.Color.blue()
        )
        embed.add_field(name="Verwendung", value=f"`{self.get_command_signature(command)}`")

        await self.get_destination().send(embed=embed)

def setup(bot):
    bot.help_command = HelpCommand()
