import discord
from discord import Intents

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


async def favo_game(message: discord.Message):
    await message.channel.send("Kies 3 favoriete spellen")
    count = 1
    bericht = str()
    for game in games:
        bericht = bericht + f"{count}\t{game}\n"
        count += 1

    embedVar = discord.Embed(title="Games")
    embedVar.add_field(name="", value=bericht)
    await message.channel.send(embed=embedVar)
    # await message.channel.send(bericht)


# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message: discord.Message):
    if "welke game" in message.content.lower():
        # await message.reply("NiggaVerse Season 2")
        await favo_game(message)


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("MTE0NjAyMzIxNTY3Njc4ODc5Ng.Gxi2ek.0fFiOps-27E77Jboz7kZqeYzBAjiQfHEtW1bQ4")

#mijn bot toke: MTE0NjAyMTc4NTUyODE3MjY1NA.GlCfVc.20Xl1uoAV36b9CQa0X-E8aCticpj1xH1U5CnIo
