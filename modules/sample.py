import os
import asyncio
from datetime import datetime

import colorama
from termcolor import colored
colorama.init()

try:
    import discord
    from discord.ext import commands
except ImportError:
    os.system("python -m pip install discord")
    import discord
    from discord.ext import commands

token = "{bottoken}"
prefix = "{cmdprefix}"
guildid = "{gid}"
userid = []
with open('modules\whitelists.txt', 'r') as file:
    for line in file:
        userid.append(line.strip())


client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
client.remove_command("help")


def command_validation(ctx):
    ids = []
    for id in userid:
        if ctx.author.id == int(id):
            ids.append(id)
    if len(ids) > 0:
        return True
    else:
        return False

help_menu = f"""
Commandes disponibles pour le bot Prodige DmAll :

**{prefix}help** - afficher ce message.

:green_circle: Activations

**{prefix}massdm (message)** - Envoyez un seul message DM à tous les utilisateurs du serveur.

"""


@client.event
async def on_ready():
    os.system("cls")
    print(colored(f"Prodige initialized as: {client.user}",'blue'))
    print("")

# commands

@client.command()
async def help(ctx):
    validation = command_validation(ctx)
    if validation:
        print(colored("Prodige - MENU D’AIDE REÇU",'magenta'))
        if ctx.guild:
            await ctx.message.delete()
        try:
            await ctx.author.send(help_menu)
        except:
            await ctx.send(help_menu)



@client.command()
async def massdm(ctx, *, message: str):
    validation = command_validation(ctx)
    if not validation:
        return
    
    if ctx.guild:
        await ctx.message.delete()
    
    members_contacted = 0

    for member in ctx.guild.members:
        if str(member.id) in userid or member.id == client.user.id or member.bot:
            continue

        try:
            await member.send(message)
            print(colored(f"{datetime.now().strftime('%H:%M:%S')}", 'white'), colored(f"Messaged {member}: {message}", 'green'))
            members_contacted += 1

            if members_contacted % 2 == 0:
                print(colored("Cooldown 6 seconds", 'yellow'))
                await asyncio.sleep(6)

        except discord.errors.Forbidden:
            print(colored(f"{datetime.now().strftime('%H:%M:%S')}", 'white'), colored(f"Couldn't message {member}, leurs DM sont désactivés ou le bot a été bloqué", 'red'))

    print(colored("Prodige - DmAll TERMINER", 'magenta'))



os.system("title Prodige DmAll")
client.run(token)