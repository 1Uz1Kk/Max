# Discord Import's #
import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View, Select

# Other Import's #
import asyncio
import json
import random
import os
import time

# Discord Bot #
intents = discord.Intents.all()
TOKEN = "MTE4NDIyMzIyMzM3MDQ4MTY3NA.GSRo3t.Bi3fUcCEzJ_Wr3MpZrhuJYq-rrWLyvZcmgPask"
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f"{bot.user} Is Online!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} Command('s)")
    except Exception as e:
        print(e)

# Overall Menu #
@bot.tree.command(name="balance", description="Shows Overall Statistics")
async def balance(interaction : discord.Interaction):
    await open_account(interaction.user)
    user = interaction.user
    users = await get_bank_data()
    name = user.display_name
    thumbnail = user.display_avatar

    coins = users[str(user.id)]["coins"]
    diamonds = users[str(user.id)]["diamonds"]
    level = users[str(user.id)]["level"]
    progress = users[str(user.id)]["progress"]
    progress2 = users[str(user.id)]["progress2"]

    em = discord.Embed(title=f"**~~ {name}'s Balance **")
    em.set_thumbnail(url=f"{thumbnail}")

    if level < 5:
        rank = "<:bronze:1172309117302472725>"
    elif level > 5 and level < 10:
        rank = "<:silver:1172309123958841365>"
    elif level > 10 and level < 20:
        rank = "<:gold:1172309131361792044>"
    elif level > 20 and level < 30:
        rank = "<:emerald:1172309208637640755>"
    elif level > 30 and level < 50:
        rank = "<:ruby:1172309180871360532>"
    elif level > 50 and level < 75:
        rank = "<:diamond:1171942980756701226>"
    else:
        rank = "<:diamond:1172309139670696017>"

    em.add_field(name="**~~ Currency :**", value=f"> **<:coin:1171943088529358970> | Coins : {coins}**\n"
                                                f"> **<:diamond:1171942980756701226> | Diamonds : {diamonds}**", inline=True)

    lr = "<:lr:1166486907178459177>"
    mr = "<:mr:1166486964325851186>"
    rr = "<:rr:1166487001638371459>"
    lg = "<:lg:1166487046077030581>"
    mg = "<:mg:1166487077270081656>"
    rg = "<:rg:1166487102138089472>"

    if progress == 0:
        bar = f"{lr}{mr}{mr}{mr}{mr}{mr}{mr}{mr}{mr}{rr}"
    elif progress == 1:
        bar = f"{lg}{mr}{mr}{mr}{mr}{mr}{mr}{mr}{mr}{rr}"
    elif progress == 2:
        bar = f"{lg}{mg}{mr}{mr}{mr}{mr}{mr}{mr}{mr}{rr}"
    elif progress == 3:
        bar = f"{lg}{mg}{mg}{mr}{mr}{mr}{mr}{mr}{mr}{rr}"
    elif progress == 4:
        bar = f"{lg}{mg}{mg}{mg}{mr}{mr}{mr}{mr}{mr}{rr}"
    elif progress == 5:
        bar = f"{lg}{mg}{mg}{mg}{mg}{mr}{mr}{mr}{mr}{rr}"
    elif progress == 6:
        bar = f"{lg}{mg}{mg}{mg}{mg}{mg}{mr}{mr}{mr}{rr}"
    elif progress == 7:
        bar = f"{lg}{mg}{mg}{mg}{mg}{mg}{mg}{mr}{mr}{rr}"
    elif progress == 8:
        bar = f"{lg}{mg}{mg}{mg}{mg}{mg}{mg}{mg}{mr}{rr}"
    elif progress == 9:
        bar = f"{lg}{mg}{mg}{mg}{mg}{mg}{mg}{mg}{mg}{rr}"
    else:
        bar = f"{lg}{mg}{mg}{mg}{mg}{mg}{mg}{mg}{mg}{rg}"
    em.add_field(name="**~~ Progress :**", value=f"> **{rank} | Level : {level}**\n"
                                                f"> **<:target:1171946146931933314> | Progress :**\n"
                                                f"{bar}", inline=False)

    em.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
    em.set_footer(text="~~ Use The Menu To Go To Specific Pages")

    await interaction.response.send_message(f"<@"+str(user.id)+">", embed=em)

# Blackjack #
@bot.tree.command(name="blackjack", description="Gambling Gamemode")
async def blackjack(interaction : discord.Interaction):
    await open_account(interaction.user)
    user = interaction.user
    users = await get_bank_data()
    name = user.display_name
    thumbnail = user.display_avatar

    coins = users[str(user.id)]["coins"]
    diamonds = users[str(user.id)]["diamonds"]
    level = users[str(user.id)]["level"]
    progress = users[str(user.id)]["progress"]
    progress2 = users[str(user.id)]["progress2"]

    em = discord.Embed(title=f"**~~ {name}'s Balance **")
    em.set_thumbnail(url=f"{thumbnail}")

    betamount = 0
    dealerscard = "❔"
    playerscard = "❔"

    em.add_field(name="**~~ Currency :**", value=f"> **<:coin:1171943088529358970> | Coins : {coins}**", inline=True)
    em.add_field(name="**~~ Blackjack :**", value=f"> **<:coin:1171943088529358970> | Bet Amount : {betamount}**\n"
                                                  f"> **<:blackjack:1181706782243033179> | Player : {playerscard}**\n"
                                                  f"> **<:dealer:1184226507053346916> <:blackjack:1181706782243033179> | Dealer : {dealerscard}**\n", inline=False)

    em.set_image(url="https://i.ibb.co/tsDpw62/auto-faqw.png")
    em.set_footer(text="~~ Use The Menu To Go To Specific Pages")

    button1 = Button(label="Bet Amount", style=discord.ButtonStyle.secondary)
    button2 = Button(label="Start", style=discord.ButtonStyle.green)
    button3 = Button(label="Cancel", style=discord.ButtonStyle.red)
    async def button_callback1(interaction):
        if interaction.user != user:
            return False
        else:
            await interaction.response.edit_message(view=None)
    async def button_callback2(interaction):
        if interaction.user != user:
            return False
        else:
            await interaction.response.edit_message(view=None)
    async def button_callback3(interaction):
        if interaction.user != user:
            return False
        else:
            await interaction.response.edit_message(view=None)

    button1.callback = button_callback1
    button2.callback = button_callback2
    button3.callback = button_callback3
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    await interaction.response.send_message(f"<@"+str(user.id)+">", embed=em, view=view)

# Function - Open Account #
async def open_account(user):
  users = await get_bank_data()
  if str(user.id) in users:
      return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["coins"] = 0
    users[str(user.id)]["diamonds"] = 0
    users[str(user.id)]["level"] = 0
    users[str(user.id)]["progress"] = 0
    users[str(user.id)]["progress2"] = 0


  with open("bank.json","w") as f:
    json.dump(users,f)
  return True

# Function - Get_Bank_Data #
async def get_bank_data():
    with open("bank.json", "r") as f:
      users = json.load(f)
    return users

# Discord Bot Output #
bot.run(TOKEN)
