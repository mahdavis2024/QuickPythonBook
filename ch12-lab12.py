'''
Lab 12: More file operations
How might you calculate the total size of all files ending with .txt that aren’t symlinks in
a directory? If your first answer was using os.path, also try it with pathlib, and vice versa.
Write some code that builds off your solution to move the same .txt files in the lab
question to a new subdirectory called backup in the same directory.
'''
import os
cur_path = os.path.abspath('.')
size = 0
for text_path in os.listdir(cur_path):
    if text_path.endswith('.txt') and not os.path.islink(os.path.join(cur_path, text_path)):
        size += os.path.getsize(os.path.join(cur_path, text_path))
        backup_dir = os.path.join(cur_path, 'backup')
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        backup_path = os.path.join(backup_dir, text_path)
        os.rename(os.path.join(cur_path, text_path), backup_path)
print(size)


import pathlib
cur_path = pathlib.Path(".")
size = 0
moved_files = []
for text_path in cur_path.glob("*.txt"):
    if not text_path.is_symlink():
        size += text_path.stat().st_size
        backup_dir = cur_path / "backup"
        if not backup_dir.exists():
            backup_dir.mkdir()
        backup_path = backup_dir / text_path.name
        text_path.replace(backup_path)
        moved_files.append(text_path.name)
print(size)
print(moved_files)