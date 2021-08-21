import discord
from discord.ext import commands

TOKEN = 'DEIN TOKEN'
bot = commands.Bot(command_prefix='+')
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f"{bot.user.name} ist nun eingeloogt!")
    
@bot.event
async def on_message(message):
    if message.channel.id == DeineChannelId:   # Die Channel ID des Kanals in dem der Bot automatisch reagieren soll.
        await message.add_reaction('😀') #Dies kann beliebig oft für weitere Kanäle wiederholt werden.
    else:
        return

bot.run(TOKEN)
