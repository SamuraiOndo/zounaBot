import discord
from responses import *
from bitmap_z import *
import time
async def send_message(message, user_message,username, is_private=False):
    try:
        response = handle_response(user_message,username)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
    
def run_discord_bot():
    token = "TOKEN"
    secret_id = "SECRET_ID"
    client = discord.Client(intents=discord.Intents.all())
    @client.event
    async def on_ready():
        await client.change_presence(activity=discord.Game('Zouna-ing it up'))
        print(f'{client.user} has connected to Discord!')
    
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author.display_name)
        usermessage = str(message.content)
        channel = message.channel
        if message.attachments:
            attachment = str(message.attachments[0])
        else:attachment= None
        print(f'{username} says: {usermessage} and has attachment: {attachment}')
        if len(usermessage) > 0:
            if usermessage[0] == '!':
                usermessage = usermessage[1:]
                await send_message(message, usermessage, username, is_private=True)
            elif usermessage.startswith(".bitmap_z") and attachment is not None:
                bitmapInfo = extract_bitmap(attachment,channel)
                await channel.send(file=bitmapInfo[0])
                time.sleep(5)
                os.remove(bitmapInfo[1])
                os.remove(bitmapInfo[2])
            else:
                await send_message(message, usermessage,username, is_private=False)
            
        
    client.run(token)