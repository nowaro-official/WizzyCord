import discord
from discord.ext import commands
from .db import Database

class Blacklist:
    def __init__(self, db_path="blacklist.db"):
        self.db = Database(db_path)

    async def setup(self):
        await self.db.execute('''
            CREATE TABLE IF NOT EXISTS blacklist (
                user_id INTEGER PRIMARY KEY
            )
        ''')

    async def add_user(self, user_id: int):
        await self.db.execute('INSERT OR IGNORE INTO blacklist (user_id) VALUES (?)', (user_id,))

    async def remove_user(self, user_id: int):
        await self.db.execute('DELETE FROM blacklist WHERE user_id = ?', (user_id,))

    async def is_blacklisted(self, user_id: int) -> bool:
        result = await self.db.fetchone('SELECT 1 FROM blacklist WHERE user_id = ?', (user_id,))
        return bool(result)

class BlacklistCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.blacklist = Blacklist()

    async def cog_load(self):
        await self.blacklist.setup()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def blacklist(self, ctx, user: discord.User):
        await self.blacklist.add_user(user.id)
        await ctx.send(f"{user.name} wurde zur Blacklist hinzugefügt.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unblacklist(self, ctx, user: discord.User):
        await self.blacklist.remove_user(user.id)
        await ctx.send(f"{user.name} wurde von der Blacklist entfernt.")

    @commands.Cog.listener()
    async def on_command(self, ctx):
        if await self.blacklist.is_blacklisted(ctx.author.id):
            await ctx.send("Du bist auf der Blacklist und darfst keine Befehle verwenden.")
            raise commands.CheckFailure("User is blacklisted")

def setup(bot):
    bot.add_cog(BlacklistCog(bot))
