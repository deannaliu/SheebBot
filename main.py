import discord #dicord.py library - asynch - callback
import os
import requests #allows code to make http req to get data from API - returns JSON
import json


client = discord.Client()  #creates an instance of a client

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event #this is how you register event
async def on_ready(): #when bot ready to start being used
  print('We have logged in as {0.user}'.format(client))  #gets username

@client.event
async def on_message(message): #if msg from bot, don't do anything
  if message.author == client.user:
    return # checks if message from the bot
  if message.content.startswith('$hello'): #command
    await message.channel.send('Hello Sheebers!') #response from bot
  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

client.run(os.getenv('TOKEN'))