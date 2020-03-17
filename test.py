import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print("Bot iss ready.")

@client.command()
async def ping(ctx):
  await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
  responses = ["Yes", "No"]

  await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

client.run("NjY3MjI5MDM3NzE3ODgwODMy.XiHYYA.NHuVk-L1MuVRhfDracTuQPR_a_s")

