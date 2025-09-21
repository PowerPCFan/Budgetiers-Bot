from discord import Interaction, app_commands, Embed


@app_commands.user_install()
@app_commands.command(name="gpu", description="View prices for GPUs")
@app_commands.describe(ephemeral="Whether the response should be shown only to you or to everyone")
async def gpu_command(interaction: Interaction, ephemeral: bool = False):
    prices = """
Price Guide by <@1183179981002645524>

## Nvidia
### 10 Series
1060 - $50
1070/1660 Ti/Super - $75
1080/2060 - $90
1080Ti - $100-120
### 20 Series
2060 Super/2070 - $120
2070 Super/2080 - $150
2080 Super - $170
### 30 Series
3050 (6GB) - Please Don't
3050 - $100
3060 12GB- $150-170
3060 Ti - $180-200
3070 - $220
3070 Ti - $250
3080 - $330
3080 12GB  - $350
3080Ti - $450
3090 - $600
3090Ti - $700
### 40 Series
4060 - $200-220
4060Ti - $250
4060Ti 16GB - $280-300
4070 - $400
4070 Super - $450
4070Ti - $500
4070Ti Super - $650
4080/Super - $750
4090 - Sub $1700
### 50 Series
MSRP or lower
## AMD
### 500 Series
580 8GB - $50
### 5000 Series
5700XT - $120 (On Par with 3060 12GB)
### 6000 Series
6600 - $120 (On Par with 3060 12GB)
6600XT - $140
6650XT/7600 - $160 (On Par with 4060)
6700 - $160 (6650XT with 10GB VRAM)
6700XT - $220
6750XT - $240
6800 - $280-300
6800XT - $330 (Faster than 4070)
6900XT - $400 (On Par with 4070 Super
6950XT - $450 (On Par with 3090/4070Ti/5070)
### 7000 Series
7600 - $160
7700XT - $300
7800XT - $350
7900XT - $600 (On Par with 4070 Ti Super)
7900XTX - $800 (Faster than 4080/Super)
### 9000 Series
MSRP or lower
    """

    embed = Embed(
        title="GPU Prices",
        description=prices
    )

    embed.set_footer(text=f"Requested by {interaction.user}", icon_url=interaction.user.display_avatar.url)

    await interaction.response.send_message(embed=embed, ephemeral=ephemeral)
