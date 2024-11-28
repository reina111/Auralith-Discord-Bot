# core/permissions.py

import json

class Permissions:
    def __init__(self):
        self.load_permissions()

    def load_permissions(self):
        with open("config/permissions.json") as f:
            self.permissions = json.load(f)

    def save_permissions(self):
        with open("config/permissions.json", "w") as f:
            json.dump(self.permissions, f, indent=4)

    def has_permission(self, user_id, role, permission):
        """Checks if a user or role has the required permission."""
        # Check user-specific permissions
        if user_id in self.permissions["users"] and permission in self.permissions["users"][user_id]:
            return True

        # Check role-based permissions
        return permission in self.permissions["roles"].get(role, [])

    def add_permission(self, entity, permission, entity_type="user"):
        """Adds a permission to a user or role."""
        key = "users" if entity_type == "user" else "roles"
        if entity not in self.permissions[key]:
            self.permissions[key][entity] = []
        self.permissions[key][entity].append(permission)
        self.save_permissions()

    def remove_permission(self, entity, permission, entity_type="user"):
        """Removes a permission from a user or role."""
        key = "users" if entity_type == "user" else "roles"
        if entity in self.permissions[key] and permission in self.permissions[key][entity]:
            self.permissions[key][entity].remove(permission)
            self.save_permissions()
