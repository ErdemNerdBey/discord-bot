import discord
from discord import Intents

intents = Intents.default()
intents.message_content = True
intents.guilds = True
intents.reactions = True
intents.guild_reactions = True
intents.messages = True
intents.guild_messages = True
bot = discord.Client(intents=intents)


# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("SampleDiscordBot is in " + str(guild_count) + " guilds.")


nummers = {
    1: '\u0031\u20E3',  # :one:
    2: '\u0032\u20E3',  # :two:
    3: '\u0033\u20E3',  # :three:
    4: '\u0034\u20E3',  # :four:
    5: '\u0035\u20E3',  # :five:
    6: '\u0036\u20E3',  # :six:
    7: '\u0037\u20E3',  # :seven:
    8: '\u0038\u20E3',  # :eight:
    9: '\u0039\u20E3',  # :nine:
    10: '\uD83D\uDD1F'  # :keycap_ten:
}

games = {
    "Fortnite": 0,
    "Call of Duty": 0,
    "Fifa 23": 0,
    "CS:GO": 0,
    "BTD 6": 0,
    "Minecraft": 0,
    "Valorant": 0,
    "Roblox": 0,
}


async def on_reaction_add(reaction, user):
    if user != bot.user:  # Check if the reaction is not from the bot itself
        emoji = reaction.emoji
        if emoji in emoji_to_number:
            number = emoji_to_number[emoji]
            await reaction.message.channel.send(f'You chose number {number}')


async def favo_game(message: discord.Message):
    await message.channel.send("Kies 3 favoriete spellen")
    count = 1
    bericht = str()
    for game in games:
        bericht = bericht + f"{count}\t{game}\n"
        count += 1

    embedVar = discord.Embed(title="Games")
    embedVar.add_field(name="", value=bericht)
    sent_message = await message.channel.send(embed=embedVar)
    for i in range(len(games)):
        await sent_message.add_reaction(f'{nummers[i + 1]}')
    # await message.channel.send(bericht)


# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message: discord.Message):
    if "welke game" in message.content.lower():
        # await message.reply("NiggaVerse Season 2")
        await favo_game(message)


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("MTE0NjAyMTc4NTUyODE3MjY1NA.GHVCni.zL8sSgJq9ZQLjla2o340UGJWMjt39SZTVNLY_0")
