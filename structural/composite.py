# The Setup: You are building a File System Simulator.
# The Problem: You have individual Files and Folders. A Folder can contain both Files and other Folders (Sub-folders). You want to treat both a single File and a Folder the same way when calculating total size.
# Your Task: Create a common interface called FileSystemComponent with a getSize() method. Implement it in a File class and a Folder class. The Folder should hold a list of FileSystemComponent objects and sum up their sizes recursively.
class FileSystemComponent:
    def getSize(self):
        pass
class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getSize(self):
        return self.size
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def getSize(self):
        total_size = 0
        for child in self.children:
            total_size += child.getSize()
        return total_size
# Usage Example
file1 = File("file1.txt", 100)
file2 = File("file2.txt", 200)
sub_folder = Folder("sub_folder")   
sub_folder.add(file2)
main_folder = Folder("main_folder")
main_folder.add(file1)
main_folder.add(sub_folder)
print(f"Total size of main_folder: {main_folder.getSize()} bytes")
# Output: Total size of main_folder: 300 bytes
