import numpy
import discord
import asyncio
import time
from bscscan import BscScan
import requests
from discord.ext import commands
from discord.ext.commands import Bot

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
YOUR_API_KEY = "6EVAPAQT7CD2N7H8QPZBCIW1SFXEK6WAP6"

#async def bscapi():


@client.event
async def on_ready():
  print(client.user.name)
  print(client.user.id)
  print("online")
  YOUR_API_KEY = "7NDVCQ7CZDA7R4X6R49B46RK8UXGVQSGDQ"

  activity = discord.Game(name="0xTheDoctor is coding...")
  while True:
    async with BscScan(YOUR_API_KEY) as bsc:
      num = await bsc.get_acc_balance_by_token_contract_address(
        contract_address="0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56",
        address="0x6B76A98Cc9a4D01F7616e53557Be368401f70802")
      num1 = int(num[:-18])
      numcomma = format(num1, ',d')
      #print(numcomma)

    activity = discord.Game(name=numcomma + " BUSD")
    await client.change_presence(status=discord.Status.online,
                                 activity=activity)
    for guild in client.guilds:
      await guild.me.edit(nick="BUSD | " + numcomma)


@client.command(pass_context=True)
async def ping(ctx):
  await ctx.send('Hello')


client.run(
  'MTA0ODIwNjExNzIyMzgwOTE2NQ.GcWK_B.FmRZV1aNyirOwjNzI5qzkWcOuRCZW4FagNqGAg')
