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
import pytz
import dateutil.tz

#Commands Handler- DO NOT TOUCH
client = commands.Bot(command_prefix=">")
member = discord.Member

#Matrixes
playingwith = ["with Aikar | >accinfo" , "with MoreMoople | >accinfo" , "with Krysyy | >accinfo" , "with Chickeneer | >accinfo"]
#Removes the default help command.
client.remove_command('help')

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name= random.choice(playingwith)))
  print('Bot is ready child')


@client.command()
async def help(ctx):
  embed = discord.Embed(title = "**Help Menu**" , description = "*EMC Discord Bot*" , color = discord.Color.blue())
  embed.add_field(name = "**accinfo [playername]**" , value = "Gives general information about the player." , inline = False)
  embed.add_field(name = "**online [playername]**" , value = "Displays the online status of the named player." , inline = False)
  embed.add_field(name = "**banstatus [playername]**" , value = "Checks whether the named player is banned, and if so, who banned them." , inline = False)
  embed.add_field(name = "**vote [playername]**" , value = "Creates a link to TopG to vote for the specified player." , inline = False)
  embed.add_field(name = "**invite**" , value = "Sends a link for the user to add the bot to their server!" , inline = False)
  embed.add_field(name = "**sourcecode**" , value = "Sends a link to the Github Page for this bot!" , inline = False)
  embed.set_footer(text = "Made by fighter_Ethan!")
  await ctx.send(embed=embed)
  
  
  
@client.command()
async def accinfo(ctx , * , username1 = "Null"):
  url = "https://empireminecraft.com/api/pinfo.php?name=" + username1
  timezone = pytz.timezone('America/New_York')  # Setting timezone
  utc_now = pytz.utc.localize(datetime.datetime.utcnow()) # UTC
  tz_now = utc_now.astimezone(timezone)
  tzinfo = pytz.timezone("America/New_York")
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

@client.command()
async def online(ctx , username1 = "Nulled"):
  url = "https://empireminecraft.com/api/pinfo.php?name=" + username1
  status = requests.get(url)
  data = status.text
  parse_json = json.loads(data)
  current = parse_json["server_id"]
  lastseen = parse_json["last_seen"]
  embed = discord.Embed(title = "**" + username1 + "**" , description = "Online Status" , color = discord.Color.blue())
  if username1 == "Nulled":
    await ctx.send("You forgot to put i")
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
  else:
    embed.add_field(name = "**Currently Playing**" , value = "Offline" , inline = True)
    embed.add_field(name = "**Last Seen**" , value =
 datetime.datetime.fromtimestamp(int(lastseen)).strftime('%Y-%m-%d at %H:%M:%S %z %Z'), inline = True)
  await ctx.send(embed=embed)

@client.command()
async def banstatus(ctx , username1 = "Null"):
  url = "https://empireminecraft.com/api/pinfo.php?name=" + username1
  status = requests.get(url)
  data = status.text
  parse_json = json.loads(data)
  currently = parse_json["banned"]
  status2 = requests.get(url)
  data2 = status2.text
  parse_json2 = json.loads(data2)
  so = parse_json2["banned_by"]
  embed = discord.Embed(title = "**" + username1 + "**", description = "Ban Status" , color = discord.Color.red())
  if currently == "0":
    embed.add_field(name = "**Is Banned**" , value = "No" , inline = True)
  elif currently == "1":
    embed.add_field(name = "**Is Bannned**" , value = "Yes" , inline = True)
    embed.add_field(name = "**Banned By**" , value = so , inline = True)
  await ctx.send(embed=embed)

@client.command()
async def vote(ctx , * , username = "Null"):
  if username == "Null":
    await ctx.send(f"{ctx.author.mention}, please enter a valid username!")
  else:
    await ctx.send("Here is your voting link:")
    await asyncio.sleep(1)
    await ctx.send("https://topg.org/minecraft-servers/server-355353-" + username)
  

@client.command()
async def invite(ctx):
  await ctx.send("https://discord.com/api/oauth2/authorize?client_id=833450592125845574&permissions=382976&scope=bot")

@client.command()
async def sourcecode(ctx):
  await ctx.send("https://github.com/fighter-Ethan/EMC-Query-Bot")

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
