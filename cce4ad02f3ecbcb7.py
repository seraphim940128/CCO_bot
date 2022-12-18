import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def 強化(ctx,a:int,b:int,c:int,d:int,e:int,f:int,g:int,h:int,i:int,j:int):
    await ctx.send(a*(1.08**b)*(1.06**c)*(1.048**d)*(1.04**e)*(1.076**f)*(1.072**g)*(1.072**h)*(1.028**(i-j-h-g-f-e-d-c-b))*(1.032**j))

@bot.command()
async def 光明(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/633600519511867394/981417946930896948/1652772909191.png")

bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="CCO", description="功能表:", color=0xeee657)
    embed.add_field(name="$強化 素質 詛咒 惡魔 棘刺 傳說 知性 聖龍 極光 次數 詛防", value="卷軸中間用空格 若無使用該卷軸填0", inline=False)
    await ctx.send(embed=embed)

bot.run('ODQ4ODIyMjAwOTMxNzEzMDc0.YLSNRw.Y9G3Ez4INuR7EkkSmvd2CyFaLpI')
