import discord
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
# Replace 'target_member_id' with the ID of the member you want to respond to
target_member_id = 668657392908632074
my_id = 225356670027431936
cabe_id = 676990484123615243

@client.event
async def on_message(message):

    if 'ethan' in message.content.lower() and message.author.id == cabe_id:
        # Replace 'response' with the response message you want to send
        response = 'What an ethangamer!'
        await message.channel.send(response)

    if message.author.id == target_member_id or my_id:
        if message.author == client.user:
            # Ignore messages sent by the bot itself
            return

    if 'mauzymice' in message.content.lower() or 'mauzy' in message.content.lower() or 'boykisser' in message.content.lower():
            # Get the sender's user ID and tag them in the response message
            sender_id = message.author.id
            response = f'<@{sender_id}> NO'
            await message.channel.send(response)

client.run('MTEwMjc2MjU1ODc3NzIwODg4Mw.GP_DdY.ZZ6RltKUufyzoKhIm1LAiH9l1U_gKaXUydg3Vc')
