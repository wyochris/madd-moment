import discord
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')
madd_id = os.getenv('MADD_ID')
my_id = os.getenv('MY_ID')
cabe_id = os.getenv('CABE_ID')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
# Replace 'target_member_id' with the ID of the member you want to respond to

@client.event
async def on_message(message):

    if 'ethan' in message.content.lower() and message.author.id == cabe_id:
        # Replace 'response' with the response message you want to send
        response = 'What an ethangamer!'
        await message.channel.send(response)

    if message.author.id == madd_id or my_id:
        if message.author == client.user:
            # Ignore messages sent by the bot itself
            return

    if 'mauzymice' in message.content.lower() or 'mauzy' in message.content.lower() or 'boykisser' in message.content.lower():
            # Get the sender's user ID and tag them in the response message
            sender_id = message.author.id
            response = f'<@{sender_id}> NO'
            await message.channel.send(response)

client.run('discord_token')
