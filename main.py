#Imports
import discord
import discord.utils
from discord.ext import commands
from discord.utils import get
import asyncio
from webserver import keep_alive
import os
import json
import requests
import random
import datetime
#Commands Handler- DO NOT TOUCH
client = commands.Bot(command_prefix=">")
member = discord.Member


#Matrixes
playingwith = ["with Aikar | >accinfo" , "with MoreMoople | >accinfo" , "with Krysyy | >accinfo" , "with Chickeneer | >accinfo"]
#Removes the default help command.
client.remove_command('help')

#Starts the bot, and adds a status to it
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name= random.choice(playingwith)))
  print('Bot is ready child')

#WORK IN PROGRESS COMMAND
@client.command()
async def setvotetimer(ctx , username1 = "Null"):
  await ctx.send("Would you like a twelve hour reminder or a twenty-four hour reminder?")
  remindtime = await client.wait_for("message")
  if remindtime.content == "12":
    await asyncio.sleep(43200)
    await ctx.send(f"{ctx.author.mention}, it's time to vote!")
  elif remindtime.content == "24":
    await asyncio.sleep(86400)
    await ctx.send(f"{ctx.author.mention}, it's time to vote!")
  
  
#Account Info- AKA the main command  
@client.command()
async def accinfo(ctx , * , username1 = "Null"):
  url = "https://empireminecraft.com/api/pinfo.php?name=" + username1
  status = requests.get(url)
  data = status.text
  parse_json = json.loads(data)
  groups = parse_json["user_group"]
  votebon = parse_json["votebonus"]
  votema = parse_json["votemax"]
  lastvoted = parse_json["lastvote"]
  firstlogin = parse_json["first_login"]
  derelict = parse_json["derelict_protection"]
  embed = discord.Embed(title = "**" + username1 + "**" , description = "Player Stats" , color = discord.Color.blue())
  if groups == "1":
    embed.add_field(name = "**Group**" , value = "Default" , inline = True)
  elif groups == "2":
      embed.add_field(name = "**Group**" , value = "Iron Supporter" , inline = True)
  elif groups == "3":
        embed.add_field(name = "**Group**" , value = "Gold Supporter" , inline = True)
  elif groups == "4":
          embed.add_field(name = "**Group**" , value = "Diamond Supporter" , inline = True)
  elif groups == "6":
    embed.add_field(name = "**Group**" , value = "Developer" , inline = True)
  elif groups == "7":
    embed.add_field(name = "**Group**" , value = "Moderator" , inline = True)
  elif groups == "8":
    embed.add_field(name = "**Group**" , value = "Senior Staff" , inline = True)
  elif groups == "9":
    embed.add_field(name = "**Group**" , value = "Community Manager" , inline = True)
  elif groups == "10":
    embed.add_field(name = "**Group**" , value = "Owner" , inline = True)
  embed.add_field(name = "**Vote Bonus**" , value = votebon , inline = True)
  embed.add_field(name = "**Max Vote Bonus**" , value = votema , inline = True)
  embed.add_field(name = "\n\u200b" + "**Last Voted**" , value = datetime.datetime.fromtimestamp(int(lastvoted)).strftime('%Y-%m-%d at %H:%M:%S %z %Z') , inline = True) 
  embed.add_field(name = "**First Joined**" , value = datetime.datetime.fromtimestamp(int(firstlogin)).strftime('%Y-%m-%d at %H:%M:%S') , inline = True)
  if derelict == "1" and groups == "2":
    embed.add_field(name = "**Derelict Protection**" , value = "Protected (Supporter)" , inline = True)
  elif derelict == "1" and groups == "3":
    embed.add_field(name = "**Derelict Protection**" , value = "Protected (Supporter)" , inline = True)
  elif derelict == "1" and groups == "4":
    embed.add_field(name = "**Derelict Protection**" , value = "Protected (Supporter)" , inline = True)
  elif derelict == "1" and groups == "6":
    embed.add_field(name = "**Derelict Protection**" , value = "Protected (Staff)" , inline = True)
  elif derelict == "1" and groups == "7":
    embed.add_field(name = "**Derelict Protection**" , value = "Protected (Staff)" , inline = True)
  elif derelict == "1" and groups == "8":
    embed.add_field(name = "**Derelict Protection**" , value = "Protected (Staff)" , inline = True)
  elif derelict == "1" and groups == "9":
    embed.add_field(name = "**Derelict Protection**" , value = "Protected (Staff)" , inline = True) 
  elif derelict == "1" and groups == "10":
    embed.add_field(name = "**Derelict Protection**" , value = "Protected (Staff)" , inline = True) 
  elif derelict == "1" and groups == "1":
    embed.add_field(name = "**Derelict Protection**" , value = "Protected (Permanent)" , inline = True)
  elif derelict == "0":
    embed.add_field(name = "**Derelict Protection**" , value = "Not Protected" , inline = True)
  embed.add_field(name = "\n\u200b" , value = "\n\u200b" , inline = True)
  await ctx.send(embed=embed)

  
#Tells you what server the player is currently on
@client.command()
async def online(ctx , username1 = "Null"):
  url = "https://empireminecraft.com/api/pinfo.php?name=" + username1
  status = requests.get(url)
  data = status.text
  parse_json = json.loads(data)
  current = parse_json["server_id"]
  embed = discord.Embed(title = "**" + username1 + "**" , description = "Online Status" , color = discord.Color.blue())
  if current == "null":
    embed.add_field(name = "**Currently Playing**" , value = "Offline" , inline = True)
  elif current == "1": 
    embed.add_field(name = "**Currently Playing**" , value = "SMP1" , inline = True)
  elif current == "2":
    embed.add_field(name = "**Currently Playing**" , value = "SMP2" , inline = True)
  elif current == "3":
    embed.add_field(name = "**Currently Playing**" , value = "Utopia" , inline = True)
  elif current == "4":
    embed.add_field(name = "**Currently Playing**" , value = "SMP3" , inline = True)
  elif current == "5":
    embed.add_field(name = "**Currently Playing**" , value = "SMP4" , inline = True)
  elif current == "6":
    embed.add_field(name = "**Currently Playing**" , value = "SMP5")
  elif current == "7":
    embed.add_field(name = "**Currently Playing**" , value = "SMP6" , inline = True)
  elif current == "8":
    embed.add_field(name = "**Currently Playing**" , value = "SMP7" , inline = True)
  elif current == "9":
    embed.add_field(name = "**Currently Playing**" , value = "SMP8" , inline = True)
  elif current == "10":
    embed.add_field(name = "**Currently Playing**" , value = "SMP9" , inline = True)
  elif current == "200":
    embed.add_field(name = "**Currently Playing**" , value = "Games Server" , inline = True)
  await ctx.send(embed=embed)

#Invites bot to your server. Link is permanently valid.
@client.command()
async def invite(ctx):
  await ctx.send("https://discord.com/api/oauth2/authorize?client_id=833450592125845574&permissions=382976&scope=bot")

 #This works in conjuction with webserver.py to keep the bot running.
  keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
