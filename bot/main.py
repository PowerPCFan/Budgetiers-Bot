import global_vars as gv
import sys


async def setup_bot():
    extensions = [
        "commands.prices"
    ]

    for extension in extensions:
        try:
            await gv.bot.load_extension(extension)
            print(f"Loaded extension {extension}")
        except Exception as e:
            print(f"Failed to load extension {extension}: {e}")

    try:
        # sync commands
        for guild in gv.bot.guilds:
            await gv.bot.tree.sync(guild=guild)
            print(f"Command tree synced for guild {guild.name} ({guild.id})")
        await gv.bot.tree.sync()
        print("Command tree synced successfully!")
    except Exception as e:
        print(f"Failed to sync command tree: {e}")


def main():
    @gv.bot.event
    async def on_ready():
        print(f"Logged in as {gv.bot.user}")
        await setup_bot()

    gv.bot.run(gv.token)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Bot is shutting down.")
        sys.exit(0)
    except Exception as e:
        print(f"Error occurred: {e}")
