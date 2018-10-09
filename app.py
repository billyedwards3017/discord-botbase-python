import discord
import random
import asyncio
import json
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient

try:
    with open("config.json") as file:
        config = json.load(file)
        pprint(config)
except:
    print("There was an error reading from the config file, please ensure you have one!")
    exit()

if not discord.opus.is_loaded():
    try:
        discord.opus.load_opus('opus')
    except:
        print("There was an error loading Opus, ignoring...")

prefix = config["prefix"]
token = config["token"]
client = commands.Bot(command_prefix = prefix)
		
@client.event
async def on_ready():
	print("Bot is a GO!!")
	print("TD: {}".format(client.user.name))
	
@client.command(pass_context=True)
async def test(ctx):
	await client.say("AHA! I AM ALIVE!")

@client.command(pass_context=True)
async def whoami(ctx):
	await client.say("You are: " +ctx.message.author.mention)	
	
client.run(token)