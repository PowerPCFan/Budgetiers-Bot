from discord.ext import commands
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


class BudgetiersBot(commands.Bot):
    async def setup_hook(self):
        print(f"Logged in as {self.user}")
        await setup_bot()


def main():
    bot = gv.bot
    bot.__class__ = BudgetiersBot
    bot.run(gv.token)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Bot is shutting down.")
        sys.exit(0)
    except Exception as e:
        print(f"Error occurred: {e}")
