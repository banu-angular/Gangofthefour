# Singleton Pattern Implementation in Python
class SettingsManager :
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(SettingsManager, cls).__new__(cls)
            # Initialize your settings here
            cls.__instance.api_base_url = "https://api.example.com"
            cls.__instance.current_theme = "Light Mode"
            cls.__instance.user_permissions = []
        return cls.__instance

    def update_theme(self, theme):
        self.current_theme = theme

    def add_permission(self, permission):
        self.user_permissions.append(permission)

    def remove_permission(self, permission):
        self.user_permissions.remove(permission)
# Example usage:
if __name__ == "__main__":  
    settings1 = SettingsManager()
    settings2 = SettingsManager()
    print(settings1 is settings2)  # True, both variables point to the same instance
    settings1.update_theme("Dark Mode")
    print(settings2.current_theme)  # Dark Mode, changes are reflected across all references
    settings1.add_permission("admin")
    print(settings2.user_permissions)  # ['admin'], permissions are shared across all references
    settings2.remove_permission("admin")
    print(settings1.user_permissions)  # [], permissions are shared across all references
    settings2.add_permission("admin")
    print(settings1.user_permissions)  # ['admin'], permissions are shared across all references
