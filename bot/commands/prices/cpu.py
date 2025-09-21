from discord import Interaction, app_commands, Embed


@app_commands.user_install()
@app_commands.command(name="cpu", description="View prices for CPUs")
@app_commands.describe(ephemeral="Whether the response should be shown only to you or to everyone")
async def cpu_command(interaction: Interaction, ephemeral: bool = False):
    prices = """
Price Guide by <@584080817698111499>

Don't want to overpay on your AMD CPUs? This guide will help with that!
These prices are what you should be paying for these CPUs

**Ryzen 5**
Ryzen 5 2600 - $35
Ryzen 5 3600  - $50
Ryzen 5 5500 - $55
Ryzen 5 5600 - $70
Ryzen 5 7500f - $115
Ryzen 5 7600 - $135
Ryzen 5 7600x - $145
Ryzen 5 9600x - $150

**Ryzen 7**
Ryzen 7 2700x - $45
Ryzen 7 3700x - $60
Ryzen 7 3800x - $70
Ryzen 7 5700x - $85
Ryzen 7 5800x - $105
Ryzen 7 7700 - $170
Ryzen 7 7700x - $180
Ryzen 7 9700x - $200

**Ryzen 9**
Ryzen 9 3900x - $80
Ryzen 9 5900x - $170
Ryzen 9 5950x - $200
Ryzen 9 7900 - $220
Ryzen 9 7900x - $250
Ryzen 9 7950x - $320
Ryzen 9 9900x - $300
Ryzen 9 9950x - $400

**X3D CPUs**
Ryzen 7 7800x3D - $300
Ryzen 7 9800x3D - $400
Ryzen 9 9950x3D - $600
    """

    embed = Embed(
        title="CPU Prices",
        description=prices
    )

    embed.set_footer(text=f"Requested by {interaction.user}", icon_url=interaction.user.display_avatar.url)

    await interaction.response.send_message(embed=embed, ephemeral=ephemeral)
