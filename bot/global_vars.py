import os
from discord import Intents, app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN", "")
owner_id = int(os.getenv("OWNER_ID", "0"))


def default() -> Intents:
    intents = Intents.default()
    intents.message_content = True

    return intents


bot = commands.Bot(command_prefix="b!", intents=default(), help_command=None)
bot.tree.allowed_installs = app_commands.AppInstallationType(guild=True, user=True)
bot.tree.allowed_contexts = app_commands.AppCommandContext(guild=True, dm_channel=True, private_channel=True)
