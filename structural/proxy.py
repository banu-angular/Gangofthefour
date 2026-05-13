# The Setup: You are building an Image Viewer app that loads high-resolution photos from a remote server.
# The Problem: Loading a 50MB image takes a long time. If you load all images at once when the app starts, it will crash or freeze.
# Your Task: Create an Image interface with a display() method. Create a RealImage class that actually loads the file. Then, create a ProxyImage class. The Proxy should only create/load the RealImage object the moment the user actually clicks display. This is called "Lazy Loading."
class Image:
    def display(self):
        pass
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.loadFromDisk()

    def loadFromDisk(self):
        print(f"Loading {self.filename} from disk...")

    def display(self):
        print(f"Displaying {self.filename}.")
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()
# Usage Example
proxy_image = ProxyImage("high_resolution_photo.jpg")
# Image is not loaded yet
print("Image is ready to be displayed.")
# User clicks display for the first time, image is loaded and displayed
proxy_image.display()
# User clicks display again, image is already loaded, just displayed
proxy_image.display()
# Output:
# Image is ready to be displayed.
# Loading high_resolution_photo.jpg from disk...
# Displaying high_resolution_photo.jpg.
# Displaying high_resolution_photo.jpg.
