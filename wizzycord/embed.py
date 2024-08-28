from typing import Any, Dict, List, Optional
import discord

class EmbedTemplate:
    @staticmethod
    def create_embed(
        title: str,
        description: str,
        color: discord.Color = discord.Color.blue(),
        **kwargs: Any
    ) -> discord.Embed:
        """
        Erstellt ein Discord Embed mit den angegebenen Parametern.
        
        :param title: Der Titel des Embeds
        :param description: Die Beschreibung des Embeds
        :param color: Die Farbe des Embeds (Standard: Blau)
        :param kwargs: Zusätzliche Felder für das Embed
        :return: discord.Embed Objekt
        """
        embed = discord.Embed(title=title, description=description, color=color)
        
        for key, value in kwargs.items():
            match key:
                case "fields":
                    for field in value:
                        embed.add_field(name=field["name"], value=field["value"], inline=field.get("inline", True))
                case "footer":
                    embed.set_footer(text=value.get("text", ""), icon_url=value.get("icon_url", ""))
                case "thumbnail":
                    embed.set_thumbnail(url=value)
                case "image":
                    embed.set_image(url=value)
                case "author":
                    embed.set_author(name=value.get("name", ""), url=value.get("url", ""), icon_url=value.get("icon_url", ""))
        
        return embed
