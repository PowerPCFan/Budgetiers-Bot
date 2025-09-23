from discord import Embed, Interaction
from datetime import datetime, timezone


def make_embed_footer(embed: Embed, interaction: Interaction) -> Embed:
    now = f"{datetime.now(tz=timezone.utc).strftime('%H:%M').lstrip('0')} UTC"
    embed.set_footer(
        text=f"Requested by @{interaction.user} | Today at {now}",
        icon_url=interaction.user.display_avatar.url
    )

    return embed
