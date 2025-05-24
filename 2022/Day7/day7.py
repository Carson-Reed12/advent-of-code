####### SETUP
with open("day7_input.txt", "r") as file:
    lines = file.readlines()

TOTAL_SPACE = 70000000
NECESSARY_SPACE = 30000000
####### PART 1
class Directory():
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.sub_dirs = {}
        self.files = {}
        self.size = 0

    def addDir(self, dir):
        self.sub_dirs[dir.name] = dir
    
    def addFile(self, file):
        self.files[file.name] = file

    def calculateSize(self):
        self.size = sum([file.size for file in self.files.values()]) + sum([directory.calculateSize() for directory in self.sub_dirs.values()])
        return self.size

class File():
    def __init__(self, size, name):
        self.name = name
        self.size = size

def getLimitedSize(directory, limit):
    global total
    if directory.size <= limit:
        total += directory.size

    for sub_dir in directory.sub_dirs.values():
        getLimitedSize(sub_dir, limit)

def dirStats(directory):
    print(f"Dir Name: {directory.name}")
    print(f"File Names: {', '.join([file.name for file in directory.files.values()])}")
    print(f"SubDir Names: {', '.join([sub_dir.name for sub_dir in directory.sub_dirs.values()])}")

root_dir = Directory("/")
root_dir.parent = root_dir
current_dir = None
for line in lines:
    if line.startswith("$"):
        if "cd /" in line:
            current_dir = root_dir
        elif "cd .." in line:
            current_dir = current_dir.parent
        elif "cd" in line:
            dir_name = line.split()[-1]
            current_dir = current_dir.sub_dirs[dir_name]
    else:
        if "dir" in line:
            dir_name = line.split()[-1]
            if dir_name not in current_dir.sub_dirs:
                current_dir.addDir(Directory(dir_name, current_dir))
        else:
            file_size = int(line.split()[0])
            file_name = line.split()[-1]
            if file_name not in current_dir.files:
                current_dir.addFile(File(file_size, file_name))

root_dir.calculateSize()

total = 0
getLimitedSize(root_dir, 100000)
print(f"PART 1 LIMITED SIZE: {total}")

####### PART 2
def getSmallestSize(directory, root_size):
    global smallest_size
    if root_size - directory.size <= TOTAL_SPACE - NECESSARY_SPACE and directory.size < smallest_size:
        smallest_size = directory.size

    for sub_dir in directory.sub_dirs.values():
        getSmallestSize(sub_dir, root_size)

smallest_size = float('inf')
getSmallestSize(root_dir, root_dir.size)
print(f"PART 2 SMALLEST DIR: {smallest_size}")