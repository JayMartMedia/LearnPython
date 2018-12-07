# import libraries
import discord
from discord.ext.commands import Bot

# your bot token
TOKEN = "Add your token here"

# create bot/client object
client = Bot(command_prefix="!")

# define a function that is run on the on_ready event
@client.event
async def on_ready():
    print("The bot is ready!")
    
# define a function that is called on the on_message event
@client.event
async def on_message(message):
    print(message.author.name+" said, '"+message.content+"'")
    if not message.author.id == "insert your bots id here":
        if "!greeting" in message.content.lower():
            await client.send_message(message.channel, content = "Greetings and Salutations!")
        elif "!goodbye" in message.content.lower():
            await client.send_message(message.channel, content = "I hope to see you return soon!")
            
# start the bot            
client.run(TOKEN)

# this is the format for sending messages
# await client.send_message(message.channel, content = "I can now send messages!")
