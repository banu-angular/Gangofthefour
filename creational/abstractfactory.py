
# 🎨 Scenario: Cross-Platform UI Toolkit
# Imagine you are building a UI library that needs to look native on both Windows and Mac.

# If the user is on Windows, the app must show a Windows Button and a Windows Checkbox.

# If the user is on Mac, the app must show a Mac Button and a Mac Checkbox.

# The danger is accidentally mixing them (e.g., a Mac button appearing on a Windows screen). The Abstract Factory ensures that you always get a "family" of components that belong together.

# Abstract Factory Pattern Implementation in Python


class UIFactory:
    def create_button(self):
        raise NotImplementedError

    def create_checkbox(self):
        raise NotImplementedError

class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacFactory(UIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()    

class WindowsButton:
    def render(self):
        return "Rendering a Windows Button"

class WindowsCheckbox:
    def render(self):
        return "Rendering a Windows Checkbox"    

class MacButton:
    def render(self):
        return "Rendering a Mac Button"  
        
class MacCheckbox:
    def render(self):
        return "Rendering a Mac Checkbox"

# Example usage:
if __name__ == "__main__":  
    import platform 
    if platform.system() == "Windows":
        factory = WindowsFactory()
    else:
        factory = MacFactory()
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())  # Rendering a Windows Button or Rendering a Mac Button
    print(checkbox.render())  # Rendering a Windows Checkbox or Rendering a Mac Checkbox
