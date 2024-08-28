import discord
from discord.ext import commands, tasks
import random

class StatusChanger:
    def __init__(self, bot):
        self.bot = bot
        self.statuses = [
            "mit Discord",
            "Hilfe: !help",
            "Version 1.0",
        ]

    def start(self):
        self.change_status.start()

    def stop(self):
        self.change_status.cancel()

    @tasks.loop(minutes=5.0)
    async def change_status(self):
        new_status = random.choice(self.statuses)
        await self.bot.change_presence(activity=discord.Game(name=new_status))

def setup(bot):
    status_changer = StatusChanger(bot)
    status_changer.start()
    return status_changer
