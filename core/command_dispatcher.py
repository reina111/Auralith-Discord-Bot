class CommandDispatcher:
    def __init__(self, bot, permissions):
        self.bot = bot
        self.permissions = permissions
        self.commands ={}

    def register_command(self, command_name, command_handler):
        """Registers a new command with the dispatcher."""
        self.commands[command_name] = command_handler

    async def handle_message(self, message):
        """Handles incoming messages and dispatches commands."""
        if message.content.startswith(self.bot.command_prefix):
            command_name = message.content[len(self.bot.command_perfix):].split()[0]
            if command_name in self.commands:
                command_handler = self.commands[command_name]
                await command_handler(self.bot, message)

    async def execute_command(self, command_name, message):
        """Executes a registered command."""
        if command_name in self.commands:
            await self.commands[command_name](self.bot, message)
        else:
            await message.channel.send(f"Unknown command: {command_name}")