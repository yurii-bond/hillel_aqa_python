from pathlib import Path


path = Path('lecture_12')

files = [file for file in path.iterdir() if file.is_file()]

print(files)

print("Files: ")
for file in files:
    print(file)


folder_path = Path('lecture_11')

directories = [dir for dir in folder_path.iterdir() if dir.is_dir()]

print('Directories: ')
for directory in directories:
    print(directory)


def show_dir(path: Path, indentation=2):
    print(f"> {path.name}")
    _files = []
    _dirs = []
    for item in path.iterdir():
        if item.is_dir():
            _dirs.append(item)
        else:
            _files.append(item)
    for _dir in _dirs:
        # print(f"  > {_dir.name}")
        show_dir(_dir)
    for _file in _files:
        print(f"    {_file.name}")


show_dir(folder_path)

