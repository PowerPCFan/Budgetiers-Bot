import os
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN", "")


def default() -> Intents:
    intents = Intents.default()
    intents.message_content = True

    return intents


bot = commands.Bot(command_prefix="b!", intents=default())
