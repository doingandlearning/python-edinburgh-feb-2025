import random


class User:
    """A class to represent a university user with attributes and permissions."""

    def __init__(self, username, role, permissions=None):
        self.username = username
        self.role = role
        self.permissions = permissions if permissions else []

    def grant_permission(self, permission):
        """Grant a new permission to the user."""
        if permission not in self.permissions:
            self.permissions.append(permission)

    def revoke_permission(self, permission):
        """Revoke a permission from the user."""
        if permission in self.permissions:
            self.permissions.remove(permission)

    def is_admin(self):
        """Check if the user is an admin."""
        return self.role == "admin"

    def has_permission(self, permission):
        """Check if the user has a specific permission."""
        return permission in self.permissions


def list_admins(users):
    """Print the usernames of all admin users."""
    admins = [user.username for user in users if user.is_admin()]
    print("Admins:", admins)


# Create user instances
alice = User("alice", "student")
admin_user = User("admin_user", "admin", ["read", "write", "delete"])

# Grant and revoke permissions
alice.grant_permission("read")
print(f"Alice's permissions: {alice.permissions}")

admin_user.revoke_permission("delete")
print(f"Admin's permissions: {admin_user.permissions}")

# Check role-specific behaviors
print(f"Is Alice an admin? {alice.is_admin()}")
print(f"Does Admin have 'write' permission? {admin_user.has_permission('write')}")

# Create a list of users
users = [
    User("alice", "student"),
    User("bob", "faculty", ["read"]),
    User("charlie", "admin", ["read", "write"]),
]

list_admins(users)
