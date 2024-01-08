import discord
from discord.ext import commands, tasks


intents = discord.Intents.all()
PREFIX = "!"
bot = commands.Bot(command_prefix=PREFIX, intents=intents)


user_voice_channel = {}

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.event
async def on_member_remove(member: discord.Member):
    
    if member.id in user_voice_channel:
        del user_voice_channel[member.id]

@bot.command()
async def join_voice(ctx):
    
    if ctx.author.voice is None:
        await ctx.send("You are not in a voice channel.")
        return

    
    channel = ctx.author.voice.channel

    
    user_voice_channel[ctx.author.id] = channel

    
    vc = await channel.connect()
    await ctx.send(f'Joined {channel.name} voice channel.')




bot.run("توکن باتتون رو اینجا بزارید")