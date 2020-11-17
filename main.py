import discord
import requests
import json

token = 'YOUR_DISCORD_BOT_TOKEN_HERE'
client = discord.Client()
command_prefix = 'rb.'
roast_command = command_prefix + 'roast'
api_url = 'https://api.snowflakedev.xyz/roast'

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Roasting The Crap Out Of People'))


@client.event
async def on_message(message):
    if not message.author.bot:
        if message.content == roast_command:
            data = requests.get(api_url).content.decode()
            roast = json.loads(data)['roast']
            await message.delete()
            await message.channel.send(roast)


client.run(token)
