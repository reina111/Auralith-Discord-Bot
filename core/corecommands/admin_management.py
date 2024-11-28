import discord
from discord.ext import commands

class Plugin:
    def __init__(self, bot, permissions, server_manager):
        self.bot = bot
        self.permissions = permissions
        self.server_manager = server_manager

    def load(self):
        @self.bot.command()
        async def add_admin(ctx, member: discord.Member):
            """Adds an admin to the server."""
            if self.server_manager.is_admin(ctx.guild.id, ctx.author.id):
                self.server_manager.add_admin(ctx.guild.id, member.id)
                await ctx.send(f"{member.mention} has been added as an admin.")
            else:
                await ctx.send("You do not have permission to add admins.")

        @self.bot.command()
        async def remove_admin(ctx, member: discord.Member):
            """Removes an admin from the server."""
            if self.server_manager.is_admin(ctx.guild.id, ctx.author.id):
                self.server_manager.remove_admin(ctx.guild.id, member.id)
                await ctx.send(f"{member.mention} has been removed as an admin.")
            else:
                await ctx.send("You do not have permission to remove admins.")

        @self.bot.command()
        async def list_admins(ctx):
            """Lists all admins in the server."""
            if self.server_manager.is_admin(ctx.guild.id, ctx.author.id):
                admins = self.server_manager.server_configs.get(str(ctx.guild.id), {}).get("admins", [])
                if admins:
                    admin_mentions = [f"<@{admin_id}>" for admin_id in admins]
                    await ctx.send(f"Admins for this server: {', '.join(admin_mentions)}")
                else:
                    await ctx.send("There are no admins for this server.")
            else:
                await ctx.send("You do not have permission to view the admin list.")

    def unload(self):
        """Unload logic if needed."""
        pass
