import discord #dicord.py library - asynch - callback
import os

client = discord.Client()  #creates an instance of a client

@client.event #this is how you register event
async def on_ready(): #when bot ready to start being used
  print('We have logged in as {0.user}'.format(client))  #gets username

@client.event
async def on_message(message): #if msg from bot, don't do anything
  if message.author == client.user:
    return # checks if message from the bot
  if message.content.startswith('$hello'): #command
    await message.channel.send('Hello Sheebers!') #response from bot

client.run(os.getenv('TOKEN'))