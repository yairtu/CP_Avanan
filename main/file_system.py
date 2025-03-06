class Entry:
    def __init__(self, name, is_file=False, parent=None):
        self.name = name
        self.is_file = is_file
        self.parent = parent
        if not is_file:
            self.sub_directory = {}
        else:
            self.sub_directory = None


class FileSystem:
    def __init__(self):
        self.root = Entry("/")  # Root
        self.current_dir = self.root

    def ls(self):
        """List whats inside the current directory"""
        print(f"\nInside '{self.current_dir.name}':")

        for item in self.current_dir.sub_directory:
            if not self.current_dir.sub_directory[item].is_file:
                print(item + "/")
            else:
                print(item)

        if not self.current_dir.sub_directory:
            print("empty.")

    def mkdir(self, folder_name):
        """Make a new folder"""
        if folder_name in self.current_dir.sub_directory:
            print(f"mkdir: '{folder_name}' error - cannot create duplicate")
            return

        self.current_dir.sub_directory[folder_name] = Entry(folder_name, parent=self.current_dir)

    def touch(self, file_name):
        """Make a new file"""
        if file_name in self.current_dir.sub_directory:
            print(f"touch: '{file_name}' error - cannot create duplicate")
            return

        self.current_dir.sub_directory[file_name] = Entry(file_name, is_file=True, parent=self.current_dir)

    def cd(self, path):
        """Move into a different directory"""
        if path == "/":
            self.current_dir = self.root
            return

        parts = path.split("/")
        temp_dir = self.current_dir

        for part in parts:
            if part == "..":
                temp_dir = temp_dir.parent
            elif part and part in temp_dir.sub_directory:
                temp_dir = temp_dir.sub_directory[part]
            else:
                print(f"cd: Can't go to '{path}', doesn't exist.")
                return

        self.current_dir = temp_dir

if __name__ == "__main__":
    fs = FileSystem()

    print("\nMaking a folder")
    fs.mkdir("docs")
    fs.cd("docs")

    print("\nMaking a file")
    fs.touch("readme.txt")

    print("\nWhat's inside the directory:")
    fs.ls()

    print("\nHeading back to root")
    fs.cd("/")