import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import os
import json

# handle tokens
with open("./data/config.json") as config_file:
    config = json.load(config_file)

intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="$", intents=intents)


@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")


token = config["bot_token"]
test_server_id = 820053634598567984

initial_extensions = []

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == "__main__":
    for extension in initial_extensions:
        client.load_extension(extension)

client.run(token)
