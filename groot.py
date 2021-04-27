from dotenv import load_dotenv
import logging
import os
import random
import discord

load_dotenv()
logging.basicConfig()
bot = discord.Client()

groot_styles = [
    'i am groot.',
    'I AM GROOT.',
    'I aM gRooT.',
    'i am groooooot!'
]

@bot.event
async def on_ready():
    print(f'{bot.user} is now online.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'groot' in message.content.lower():
        msg = random.choice(groot_styles)
        await message.channel.send(msg)

bot.run(os.getenv('TOKEN'))