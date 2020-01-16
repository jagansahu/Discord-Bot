import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print("Bot is ready.")

@client.command()
async def clear(ctx, amount=5):
  await ctx.channel.purge(limit=amount)

client.run("NjY3MjI5MDM3NzE3ODgwODMy.Xh_rnw.k6kljUjByurH3Rx6HEf5MWyXrmg")
