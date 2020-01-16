import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print("Bot is ready.")

@client.event 
async def on_member_join(member):
  print(f"{member} has joined a server.")

@client.event
async def on_member_remove(member):
  print(f"{member} has left a server.")

client.run("NjY3MjI5MDM3NzE3ODgwODMy.Xh_rnw.k6kljUjByurH3Rx6HEf5MWyXrmg")

