import discord
from discord.ext import commands
from discord.ext.commands import Bot

TOKEN = 'DEIN TOKEN'
bot = commands.Bot(command_prefix='+')
bot.remove_command('help')


@bot.event
# Einloggen
async def on_ready():
    print("Ich habe mich eingeloggt. Beep bop.")

@bot.event
async def on_message(message):
    if message.channel.id == DEINE channel ID:
        await message.add_reaction('emajio')
        await message.add_reaction('emajio')


bot.run (TOKEN, bot=True)
