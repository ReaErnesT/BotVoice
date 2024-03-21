import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
PREFIX = "!"
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Paste Your Token Bot
token = "-"

user_voice_channel = {}

@bot.event
async def on_ready():
    print('Bot Online Shod')

@bot.command()
async def join (ctx):
    if ctx.author.voice is None:
        embed = disnake.Embed(
            title='Error ❌',
            description='Shoma Dar Chnaeel Soti Hozor Nadarid ',
            color=disnake.Color.red()
        )
        await ctx.send(embed=embed)
        return

    channel = ctx.author.voice.channel

    user_voice_channel[ctx.author.id] = channel

    vc = await channel.connect()
    embed = disnake.Embed(
        title='Success ✅',
        description=f"Bot Vard Channel {channel.name} Shod",
        color=disnake.Color.green()
    )
    await ctx.send(embed=embed)

bot.run(token)
