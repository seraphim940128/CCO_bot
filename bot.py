import discord
from discord.ext import commands
bot = commands.Bot(command_prePix ='!')

@bot.event
async def on_ready():
    print("bot is online")



bot.run('ODQ4ODIyMjAwOTMxNzEzMDc0.YLSNRw.Y9G3Ez4INuR7EkkSmvd2CyFaLpI')
