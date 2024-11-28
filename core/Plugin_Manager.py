# core/plugin_manager.py

import importlib
import os
import json

class PluginManager:
    def __init__(self, bot, permissions):
        self.bot = bot
        self.permissions = permissions
        self.plugins = {}

    def load_core_commands(self):
        """Loads core commands from the core/corecommands/ folder."""
        core_commands_path = "core/corecommands"
        for filename in os.listdir(core_commands_path):
            if filename.endswith(".py") and not filename.startswith("__"):
                command_name = filename[:-3]
                self.load_plugin(f"core.corecommands.{command_name}")

    def load_enabled_plugins(self):
        """Loads enabled plugins as defined in config/settings.json."""
        with open("config/settings.json") as f:
            config = json.load(f)

        for plugin_name in config["enabled_plugins"]:
            self.load_plugin(f"plugins.{plugin_name}")

    def load_plugin(self, module_path):
        """Dynamically loads a plugin or command."""
        try:
            module = importlib.import_module(module_path)
            plugin_class = getattr(module, "Plugin")
            plugin_instance = plugin_class(self.bot, self.permissions)
            plugin_instance.load()
            self.plugins[module_path] = plugin_instance
            print(f"Loaded plugin: {module_path}")
        except Exception as e:
            print(f"Failed to load plugin {module_path}: {e}")

    def unload_plugin(self, module_path):
        """Dynamically unloads a plugin or command."""
        if module_path in self.plugins:
            self.plugins[module_path].unload()
            del self.plugins[module_path]
            print(f"Unloaded plugin: {module_path}")
        else:
            print(f"Plugin {module_path} not loaded.")
