from discord import Interaction, app_commands, Embed


@app_commands.user_install()
@app_commands.command(name="psu", description="View prices for PSUs")
@app_commands.describe(ephemeral="Whether the response should be shown only to you or to everyone")
async def psu_command(interaction: Interaction, ephemeral: bool = False):
    prices = """
Price Guide by <@769940582985367572>

- 450W - $30-35
- 500W - $35
- 550W - $35-40
- 600W - $40
- 650W - $40-45
- 700W - $45
- 750W - $50-55
- 800W - $55
- 850W - $60-65
- 1000W - $70-75
- 1000W+ - $80

**Notes**
- Do not spend above ~$80 for a used/open box PSU, even if it's an SFX PSU
- Give or take $5 depending on tier.

**PSU Tierlists**
[SPL Tierlist](https://docs.google.com/spreadsheets/d/1akCHL7Vhzk_EhrpIGkz8zTEvYfLDcaSpZRB6Xt6JWkc/edit?pli=1&gid=1973454078#gid=1973454078)
[Cultists Tierlist](https://docs.google.com/spreadsheets/d/1eL0893Ramlwk6E3s3uSvH1_juom7SMG5SCNzP2Uov8w/edit?gid=1529225916#gid=1529225916)
    """  # noqa: E501

    embed = Embed(
        title="PSU Prices",
        description=prices
    )

    embed.set_footer(text=f"Requested by {interaction.user}", icon_url=interaction.user.display_avatar.url)

    await interaction.response.send_message(embed=embed, ephemeral=ephemeral)
