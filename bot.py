import discord
from discord.ext import commands
from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Cogs yükleme
initial_extensions = ["cogs.general", "cogs.economy"]

if __name__ == "__main__":
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı!")

bot.run(TOKEN)
