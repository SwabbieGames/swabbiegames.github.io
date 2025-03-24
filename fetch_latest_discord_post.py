import discord
import asyncio
import os

BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN']

# Channel name -> Channel ID mapping
CHANNELS = {
    'roadmap': 1350097483270852630,
    'updates': 1352060123463417926,
    'patch_notes': 1344543229831413831
}

class DiscordClient(discord.Client):
    async def on_ready(self):
        print(f'✅ Logged in as {self.user} (ID: {self.user.id})')

        for name, channel_id in CHANNELS.items():
            channel = self.get_channel(channel_id)

            if not channel:
                print(f"❌ Channel '{name}' (ID {channel_id}) not found.")
                continue

            try:
                messages = [msg async for msg in channel.history(limit=1)]
                message = messages[0]  # get the first message object
                filename = name

                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(message.content)

            except Exception as e:
                print(f"❌ Error reading from '{name}': {e}")

        await self.close()

intents = discord.Intents.default()
intents.message_content = True

client = DiscordClient(intents=intents)
client.run(BOT_TOKEN)
