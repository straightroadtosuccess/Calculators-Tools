import discord
import asyncio
import array

TOKEN = "BOT_TOKEN"  # Make sure this is the bot token, not a user token
GUILD_ID = DISCORD_SERVER_ID
CHANNEL_ID = CHANNEL_ID

intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True

client = discord.Client(intents=intents)
voice_client = None

# --- Optimized Silence Source ---
frame = array.array('h', [0] * 1920 * 2).tobytes()

class Silence(discord.AudioSource):
    def read(self):
        return frame
    def is_opus(self):
        return False
# -------------------------------

async def play_silence():
    """Continuously stream silence"""
    global voice_client
    if voice_client and voice_client.is_connected():
        if not voice_client.is_playing():
            voice_client.play(Silence())
            print("Streaming continuous silence")

async def connect_loop():
    global voice_client
    while True:
        try:
            channel = await client.fetch_channel(CHANNEL_ID)
            if not isinstance(channel, discord.VoiceChannel):
                print("Channel is not a voice channel")
                return

            if voice_client is None or not voice_client.is_connected():
                voice_client = await channel.connect()
                print(f"Joined {channel.name}")

            await play_silence()

        except Exception as e:
            print("Failed to connect or play audio:", e)

        await asyncio.sleep(30)  # check every 30s

@client.event
async def on_ready():
    print(f"{client.user} is ready!")
    asyncio.create_task(connect_loop())

client.run(TOKEN)