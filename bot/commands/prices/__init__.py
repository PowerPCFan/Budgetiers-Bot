from discord import app_commands
from discord.ext import commands

from .gpu import gpu_command
from .cpu import cpu_command
from .psu import psu_command

cmds = [
    gpu_command,
    cpu_command,
    psu_command
]


class Prices(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.prices_group = app_commands.Group(
            name="prices", description="Prices commands"
        )

        for cmd in cmds:
            self.prices_group.add_command(cmd)  # noqa: E116

    async def cog_load(self):
        self.bot.tree.add_command(self.prices_group)
        print("Prices commands added to tree")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Prices(bot))
