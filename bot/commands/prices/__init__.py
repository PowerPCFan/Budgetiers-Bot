from discord import Interaction, Embed, app_commands
from discord.ext import commands


class Prices(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.prices_group = app_commands.Group(
            name="prices",
            description="Prices commands"
        )

        self.prices_group = app_commands.user_install()(self.prices_group)

        @self.prices_group.command(name="cpu", description="View prices for CPUs")
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

        @self.prices_group.command(name="gpu", description="View prices for GPUs")
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

        @self.prices_group.command(name="psu", description="View prices for PSUs")
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

    async def cog_load(self):
        self.bot.tree.add_command(self.prices_group)
        print("Prices commands added to tree")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Prices(bot))
