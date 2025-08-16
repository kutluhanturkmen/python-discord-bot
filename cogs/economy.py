from discord.ext import commands

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.balances = {}  # Basit memory store

    @commands.command()
    async def balance(self, ctx):
        user = ctx.author.id
        balance = self.balances.get(user, 0)
        await ctx.send(f"{ctx.author.mention}, bakiyen: {balance} 💰")

def setup(bot):
    bot.add_cog(Economy(bot))
