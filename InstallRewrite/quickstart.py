import discord

TOKEN = "Your Token Here"

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$greetings'):
        # new method for sending messages
        await message.channel.send('Greetings and salutations!')
        # old method is below
        # await client.send_message(message.channel,content='Greetings and salutations')

client.run(TOKEN)
