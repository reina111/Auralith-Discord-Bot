# core/server_manager.py

import json

class ServerManager:
    def __init__(self, owner_id):
        self.owner_id = owner_id
        self.server_config_path = "config/server_config.json"
        self.load_server_configs()

    def load_server_configs(self):
        """Loads server configurations from a JSON file."""
        try:
            with open(self.server_config_path) as f:
                self.server_configs = json.load(f)
        except FileNotFoundError:
            self.server_configs = {}
            self.save_server_configs()

    def save_server_configs(self):
        """Saves server configurations to a JSON file."""
        with open(self.server_config_path, "w") as f:
            json.dump(self.server_configs, f, indent=4)

    def is_owner(self, user_id):
        """Checks if the user is the bot owner."""
        return str(user_id) == str(self.owner_id)

    def is_admin(self, server_id, user_id):
        """Checks if the user is an admin for a specific server."""
        server_id = str(server_id)
        user_id = str(user_id)
        if self.is_owner(user_id):
            return True  # Owner always has admin rights
        return user_id in self.server_configs.get(server_id, {}).get("admins", [])

    def add_admin(self, server_id, user_id):
        """Adds a user as an admin for the server."""
        server_id = str(server_id)
        user_id = str(user_id)
        if server_id not in self.server_configs:
            self.server_configs[server_id] = {"admins": []}
        if user_id not in self.server_configs[server_id]["admins"]:
            self.server_configs[server_id]["admins"].append(user_id)
            self.save_server_configs()

    def remove_admin(self, server_id, user_id):
        """Removes a user as an admin for the server."""
        server_id = str(server_id)
        user_id = str(user_id)
        if server_id in self.server_configs and user_id in self.server_configs[server_id]["admins"]:
            self.server_configs[server_id]["admins"].remove(user_id)
            self.save_server_configs()
