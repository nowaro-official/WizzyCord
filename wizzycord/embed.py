import discord

class EmbedTemplate:
    @staticmethod
    def create_embed(title, description, color=discord.Color.blue(), **kwargs):
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
            if key == "fields":
                for field in value:
                    embed.add_field(name=field["name"], value=field["value"], inline=field.get("inline", True))
            elif key == "footer":
                embed.set_footer(text=value.get("text", ""), icon_url=value.get("icon_url", ""))
            elif key == "thumbnail":
                embed.set_thumbnail(url=value)
            elif key == "image":
                embed.set_image(url=value)
            elif key == "author":
                embed.set_author(name=value.get("name", ""), url=value.get("url", ""), icon_url=value.get("icon_url", ""))
        
        return embed
