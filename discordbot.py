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

#Clears msgs
@client.command()
async def clear(ctx, amount=5):
  await ctx.channel.purge(limit=amount)

#kicks selected member
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)

#bans selected member
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'Banned {member.mention}')

#unbans selected member
@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'Unbanned {user.mention}')
      return

#Token received from discord server
client.run("NjY3MjI5MDM3NzE3ODgwODMy.XnBQlg.aMFDWG94TxGqmkyEVjyFSAWposU") 

