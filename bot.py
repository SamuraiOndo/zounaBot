import discord
from responses import *
from bitmap_z import *
import time
from discord.ext import commands, tasks
async def send_message(message, user_message,username, is_private=False):
    try:
        response = handle_response(user_message,username)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
    
def run_discord_bot():
    token = ""
    secret_id = 'SECRET_ID'
    bot = commands.Bot(command_prefix='.',intents=discord.Intents.all())
    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Game('Zouna-ing it up'))
        print(f'{bot.user} has connected to Discord!')
    
    bot.remove_command('help')
    @bot.command(aliases=['help'])
    async def help_01(ctx):
        embed=discord.Embed(title="Help", description="Show descriptions of commands", color=0x049383)
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/888489182379511839.webp')
        embed.add_field(name=".crc32", value="Returns the Asobo CRC32 of the given string", inline=False)
        embed.add_field(name=".crc64", value="Returns the Asobo CRC64 of the given string", inline=False)
        embed.add_field(name=".Bitmap_Z", value="Converts the given Bitmap_Z", inline=False)
        embed.add_field(name=".zounasrc", value="Sends the link to the Opal Source Code", inline=False)
        embed.add_field(name=".wiki", value="Sends link to the FMTK wiki", inline=False)
        embed.add_field(name=".tl", value="Sends link to the FMTK wiki timeline", inline=False)
        embed.add_field(name=".source", value="Sends link to bot source code", inline=True)
        embed.set_footer(text="This bot was made by https://github.com/SamuraiOndo/")
        await ctx.send(embed=embed)
    @bot.command()
    async def crc32(ctx, *, message):
        import crc32
        await ctx.send(str(crc32.crc32(message.encode("utf-8"))))
    @bot.command()
    async def crc64(ctx, *, message):
        import crc64
        await ctx.send(str(crc64.crc64(message.encode("utf-8"))))
    @bot.command()
    async def bitmap_z(ctx, *, arg: discord.Attachment):
        attachment = str(arg)
        if attachment is not None and attachment.lower().endswith(".bitmap_z"):
            await ctx.send("Converting...")
            bitmapInfo = extract_bitmap(attachment)
            await ctx.send(file=bitmapInfo[0])
            time.sleep(5)
            os.remove(bitmapInfo[1])
            os.remove(bitmapInfo[2])
        elif attachment is not None:
            await ctx.send("Not a Bitmap_Z file")
        else:
            await ctx.send("No attachment")
    @bot.command()
    async def zounasrc(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/888080380752707627/986683930734374922/ZOUNA.rar")
    @bot.command()
    async def source(ctx):
        await ctx.send("https://github.com/SamuraiOndo/zounaBot")
    @bot.command()
    async def wiki(ctx):
        await ctx.send("https://github.com/widberg/fmtk/wiki")
    @bot.command()
    async def tl(ctx):
        await ctx.send("https://github.com/widberg/fmtk/wiki/TotemTech-ToonTech-Zouna-ACE-BSSTech-Opal-Timeline")
    @bot.command()
    async def trans(ctx,language,*, message):
        destLang = message.split(" ")[0]
        print(destLang)
        text = message
        translation = GoogleTranslator(source='auto', target=language).translate(text)
        if text.lower() == translation.lower(): 
            await ctx.send("Translated text is the same as the original text")
        elif ("http" in text.lower()):
            await ctx.send("There is a link in the message. Please resend without the link.")
        else:
            await ctx.send(translation)
    @bot.listen()
    async def on_message(message):
        if message.author == bot.user:
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
            else:
                await send_message(message, usermessage,username, is_private=False)
                

    bot.run(token)
                # elif usermessage.startswith(".bitmap_z") and attachment is not None:
                # bitmapInfo = extract_bitmap(attachment,channel)
                # await channel.send(file=bitmapInfo[0])
                # time.sleep(5)
                # os.remove(bitmapInfo[1])
                # os.remove(bitmapInfo[2])