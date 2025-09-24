from discord import Interaction, Embed, app_commands, Color
from discord.ext import commands
import textwrap
import tools


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.user_install()
    @app_commands.command(name="help", description="Get help with the bot's commands.")
    async def help(self, interaction: Interaction) -> None:
        # TODO: improve this

        embed = Embed(
            color=Color.blue(),
            title="Bot Help",
            description=textwrap.dedent("""\
                **Available Commands:**
                - `/prices` - Price-related commands:
                  - `/prices cpu` - View prices for CPUs
                  - `/prices amd-gpu` - View prices for AMD GPUs
                  - `/prices nvidia-gpu` - View prices for NVIDIA GPUs
                  - `/prices psu` - View prices for PSUs
                - `/help` - Display this help message
            """)
        )

        embed = tools.make_embed_footer(embed, interaction)

        await interaction.response.send_message(embed=embed)

    async def cog_load(self):
        print("/help command added to tree")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Help(bot))
