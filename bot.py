# bot.py

import discord
from discord.ext import commands
from core.Plugin_Manager import PluginManager
from core.permissions import Permissions
from core.server_manager import ServerManager

# Load configuration
import json
with open('config/settings.json') as f:
    config = json.load(f)

OWNER_ID = config["owner_id"]

# Initialize bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

# Initialize plugin manager, permissions, and server manager
permissions = Permissions()
server_manager = ServerManager(OWNER_ID)
plugin_manager = PluginManager(bot, permissions, server_manager)

# Register events
@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")
    plugin_manager.load_core_commands()
    plugin_manager.load_enabled_plugins()

# Run the bot
bot.run(config["token"])