import discord
import random
import os
from discord.ext import commands
bot = commands.Bot(command_prefix='!', description='Simple roll bot')

@bot.event
async def on_ready():
        print('Logged in as')
        print(bot.user.name)

@bot.command()
async def hello():
 await bot.say('Hello!')

@bot.command()
async def roll20():
  await bot.say('Rolling d20')
  await bot.say(random.randint(1, 20))
@bot.command()
async def roll6():
  await bot.say('Rolling d6')
  roll = random.randint(1, 6)
  if roll == 1:
      await bot.say('Ha! You rolled a 1!')
  else:
      await bot.say(roll)
@bot.command()
async def roll8():
  await bot.say('Rolling d8')
  roll = random.randint(1, 8)
  if roll == 1:
    await bot.say('Ha! You rolled a 1!')
  else:
    await bot.say(roll)
@bot.command()
async def roll4():
  await bot.say('Rolling d4')
  roll = random.randint(1, 4)
  if roll == 1:
    await bot.say('Ha! You rolled a 1!')
  else:
    await bot.say(roll)
@bot.command()
async def roll100():
  await bot.say('Rolling d100')
  roll = random.randint(1, 100)
  if roll == 1:
    await bot.say('Ha! You rolled a 1!')
  else:
    await bot.say(roll)

@bot.command()
async def OWO():
  await bot.say('OWO')

@bot.command()
async def roll(dice, number):
  await bot.say("Rolling " + number + " d" + dice)
  total = []
  num = int(number)
  die = int(dice)
  roll = 0
  i = 1
  while i <= num:  
    if number != '0' and die != 0:
      a = random.randint(1, die)
      total.append(a)
      roll += a
    i += 1
  await bot.say(roll)
  await bot.say(total)
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)
