import discord , random , os
from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)



@bot.command()
async def resim(ctx):
    img_name = random.choice(os.listdir("resim"))
    with open(f'resim/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)





bot.run("MTI1NDgzMTU5NDUxOTQwMDUyMA.GA8j-X.KBF4nMQBYuQDx5RtXSxg5rH7AfLJmI2DK_ENcU")
