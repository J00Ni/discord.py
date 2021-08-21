import discord
from discord.ext import commands

TOKEN = 'DEIN TOKEN'
bot = commands.Bot(command_prefix='+')
bot.remove_command('help')


@bot.event
async def on_ready():
    print("Ich habe mich eingeloggt. Beep bop.")

bot.run(TOKEN)
