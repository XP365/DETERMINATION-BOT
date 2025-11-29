import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random
import webserver

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handeler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='*', intents=intents)

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "message" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} please work")

    await bot.process_commands(message)

@bot.command()
async def save(ctx):
    flavortexts = [
        "(The shadow of the ruins looms above, filling you with determination. HP fully restored.)",
        "(Knowing the mouse might one day leave its hole and get the cheese... It fills you with determination.)",
        "(Playfully crinkling through the leaves fills you with determination. HP fully restored.)",
        "(Seeing such a cute, tidy house in the RUINS gives you determination)",
        "The cold atmosphere of a new land... it fills you with determination.",
        "The convenience of that lamp still fills you with determination.",
        "Knowing the mouse might one day find a way to heat up the spaghetti... It fills you with determination.",
        "Knowing that dog will never give up trying to make the perfect snowdog... It fills you with determination.",
        "Snow can always be broken down and rebuilt into something more useful. This simple fact fills you with determination.",
        "The sight of such a friendly town fills you with determination.",
        "The sound of rushing water fills you with determination.",
        "A feeling of dread hangs over you...) (But you stay determined.",
        "Knowing the mouse might one day extract the cheese from the mystical crystal...",
        "It fills you with determination.",
        "The serene sound of a distant music box... It fills you with determination.",
        "The sound of muffled rain on the cavetop... It fills you with determination.",
        "The waterfall here seems to flow from the ceiling of the cavern... Occasionally, a piece of trash will flow through... and fall into the bottomless abyss below. Viewing this endless cycle of worthless garbage... It fills you with determination.",
        "Partaking in worthless garbage fills you with determination.",
        "The feeling of your socks squishing as you step gives you determination.",
        "You feel a calming tranquility. You're filled with determination...",
        "You feel... something You're filled with de**temmie**nation",
        "(The wind is howling. You're filled with determination...)",
        "(The howling wind is now a breeze. This gives you determination...)",
        "The wind has stopped. You're filled with determination...",
        "Seeing such a strange laboratory in a place like this... You're filled with determination.",
        "The wooshing sound of steam and cogs... it fills you with determination.",
        "The fact that Nixy was able to code this in one night... it fills you with determination",
        "An ominous structure looms in the distance... You're filled with determination.",
        "Knowing the mouse might one day hack the computerized safe and get the cheese... It fills you with determination.",
        "The smell of cobwebs fills the air... You're filled with determination.",
        "A huge structure lies north. You're filled with determination.",
        "The relaxing atmosphere of this hotel... it fills you with determination.",
        "The air is filled with the smell of ozone... it fills you with determination.",
        "Behind this door must be the elevator to the King's castle. You're filled with determination.",
        "It seems SAVEing really is impossible... but maybe, there is something else you can SAVE..."


    ]
    randomint = random.randint(0, len(flavortexts) - 1)
    
    print(randomint)
    await ctx.send(flavortexts[randomint])



logging.basicConfig(
    level=logging.DEBUG,
    filename='discord.log',
    filemode='w',
    encoding='utf-8'
)

bot.run(token)
