with open("inputs/day7.txt") as f:
    s = f.read()


def parse_cd(s):
    """Returned the directory name from a cd command"""
    return s.split("cd ")[1].strip()

def parse_ls(s):
    """Returns a list of (name, size) tuples from an ls command"""
    ret_list = []
    for line in s.split("\n")[1:]:
        if line == "": continue
        size, name = line.split(" ")
        if size=="dir":
            ret_list.append((name, None))
        else:
            ret_list.append((name, int(size)))
    return ret_list


class Directory:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.files = {}
        self.dirs = {}
    
    def add_file(self, name, size):
        self.files[name] = size

    
    def add_dir(self, name):
        new_dir = Directory(self, name)
        self.dirs[name] = new_dir
        return new_dir
    
    def size(self):
        return sum(self.files.values()) + sum([d.size() for d in self.dirs.values()])


tree = Directory(None, "/")
current_dir = tree
all_dirs = [current_dir]
for cmd in s.split("$ ")[2:]:
    if cmd.startswith("ls"):
        ls = parse_ls(cmd)
        for name, size in ls:
            if size == None:
                new_dir = current_dir.add_dir(name)
                all_dirs.append(new_dir)
            else:
                current_dir.add_file(name, size)

    elif cmd.startswith("cd"):
        new_dir = parse_cd(cmd)
        if new_dir == "..":
            current_dir = current_dir.parent
        else:
            current_dir = current_dir.dirs[new_dir]

curr_used = 70000000-tree.size()
candidates = []
for dir in all_dirs:
    if curr_used+dir.size()>=30000000:
        candidates.append(dir)
print(min(candidates, key=lambda x: x.size()).size())



