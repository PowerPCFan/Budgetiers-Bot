from discord import Interaction, Embed, app_commands, Color
from discord.ext import commands
import tools
import global_vars as gv


class ReloadCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.user_install()
    @app_commands.command(name="reload-command", description="[OWNER ONLY] Reload a command")
    @app_commands.describe(command_or_command_group="The command or command group to reload")
    async def reload_command(self, interaction: Interaction, command_or_command_group: str) -> None:
        if interaction.user.id != gv.owner_id:
            embed = Embed(
                color=Color.red(),
                title="Permission Denied",
                description="You do not have permission to use this command."
            )

            embed = tools.make_embed_footer(embed, interaction)

            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

        try:
            await self.bot.unload_extension(f"commands.{command_or_command_group}")
            await self.bot.load_extension(f"commands.{command_or_command_group}")

            embed = Embed(
                color=Color.blue(),
                title="Command Reloaded",
                description="Command reloaded successfully."
            )
        except Exception as e:
            embed = Embed(
                color=Color.red(),
                title="Error Reloading Command",
                description=f"An error occurred while reloading the command:\n```\n{e}\n```"
            )

        await interaction.response.send_message(embed=tools.make_embed_footer(embed, interaction), ephemeral=True)

    async def cog_load(self):
        print("/reload-command command added to tree")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ReloadCommand(bot))
