from discord import Interaction, Embed, app_commands, Color
from discord.ext import commands
import tools


class PCResourceDocument(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.user_install()
    @app_commands.command(name="pc-resource-document", description="Retrieve the link to the PC Resource Document.")
    async def pcrd(self, interaction: Interaction) -> None:
        await interaction.response.send_message(
            embed=tools.make_embed_footer(interaction=interaction, embed=Embed(
                color=Color.blue(),
                title="PC Resource Document",
                description=(
                    "Check out my PC Resource Document: "
                    "https://www.powerpcfan.xyz/resources/pc-resource-document"
                ),
            ))
        )

    async def cog_load(self):
        print("/pc-resource-document command added to tree")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PCResourceDocument(bot))
