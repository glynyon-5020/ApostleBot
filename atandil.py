import json
import discord
from discord.ext import commands
from discord import Client

# handle tokens
with open('./data/config.json') as config_file:
    config = json.load(config_file)


atandil_token = config['bot_token']

intents = discord.Intents.default()
intents.message_content = True

atandil = Client(intents=intents)

@atandil.event
async def on_ready():
    print(f'We have logged in as {atandil.user}')

@atandil.event
async def on_message(message):
    if message.author == atandil.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# atandil = commands.Bot(command_prefix='!')

# @bot.command()
# async def ping(ctx):
#     await ctx.send("Pong!")

atandil.run(atandil_token)