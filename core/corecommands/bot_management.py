# core/corecommands/bot_management.py

class Plugin:
    def __init__(self, bot, permissions):
        self.bot = bot
        self.permissions = permissions

    def load(self):
        @self.bot.command()
        async def restart(ctx):
            """Restarts the bot."""
            if self.permissions.has_permission(str(ctx.author.id), "Admin", "restart_bot"):
                await ctx.send("Restarting bot...")
                await self.bot.close()
            else:
                await ctx.send("You don't have permission to restart the bot.")

        @self.bot.command()
        async def shutdown(ctx):
            """Shuts down the bot."""
            if self.permissions.has_permission(str(ctx.author.id), "Admin", "shutdown_bot"):
                await ctx.send("Shutting down bot...")
                await self.bot.close()
            else:
                await ctx.send("You don't have permission to shut down the bot.")

        @self.bot.command()
        async def start(ctx):
            """Starts the bot (simulated for command structure)."""
            if self.permissions.has_permission(str(ctx.author.id), "Admin", "start_bot"):
                await ctx.send("Bot is already running!")
            else:
                await ctx.send("You don't have permission to start the bot.")

    def unload(self):
        """Unload logic if needed (currently unused)."""
        pass
