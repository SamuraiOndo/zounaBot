import discord
from responses import *
async def send_message(message, user_message,username, is_private=False):
    try:
        response = handle_response(user_message,username)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
    
def run_discord_bot():
    token = "TOKEN"
    client = discord.Client(intents=discord.Intents.all())
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
    
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author.display_name)
        usermessage = str(message.content)
        channel = str(message.channel)
        print(f'{username} says: {usermessage}')
        
        if usermessage[0] == '!':
            usermessage = usermessage[1:]
            await send_message(message, usermessage, username, is_private=True)
        else:
            await send_message(message, usermessage,username, is_private=False)
            
        
    client.run(token)