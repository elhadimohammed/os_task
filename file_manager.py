
# file_manager.py
import os
import stat
import shutil
from pathlib import Path

def file_manager_menu():
    while True:
        print("""
--- File Manager ---
1) List files/directories
2) Change permissions (chmod)
3) Create file/directory
4) Delete file/directory
5) Create symbolic link
6) Back
""")
        c = input("Choose: ").strip()
        if c == "1":
            path = input("Path (default .): ").strip() or "."
            list_entries(path)
        elif c == "2":
            path = input("File/Dir path: ").strip()
            mode = input("New permission (e.g., 755): ").strip()
            change_permissions(path, mode)
        elif c == "3":
            name = input("Name (path): ").strip()
            t = input("Type (f=file, d=dir): ").strip().lower()
            create_entry(name, t)
        elif c == "4":
            name = input("Name (path): ").strip()
            delete_entry(name)
        elif c == "5":
            target = input("Target path (existing file/dir): ").strip()
            link = input("Link name (path to create): ").strip()
            create_symlink(target, link)
        elif c == "6":
            break
        else:
            print("Invalid choice.")

def list_entries(path: str):
    try:
        p = Path(path).resolve()
        if not p.exists():
            print(f"Path not found: {p}")
            return
        print(f"\nListing: {p}\n")
        for entry in sorted(p.iterdir(), key=lambda e: e.name.lower()):
            try:
                s = entry.stat(follow_symlinks=False)
                kind = "DIR" if entry.is_dir() else ("LINK" if entry.is_symlink() else "FILE")
                perms = stat.filemode(s.st_mode)
                print(f"{perms}  {kind:4}  {s.st_size:10}  {entry.name}")
            except Exception as e:
                print(f"??    ERR   ----------  {entry.name} ({e})")
        print()
    except Exception as e:
        print(f"Error: {e}")

def change_permissions(path: str, mode_str: str):
    try:
        mode = int(mode_str, 8)
        os.chmod(path, mode)
        print(f"Permissions changed: {path} -> {mode_str}")
    except Exception as e:
        print(f"chmod failed: {e}")

def create_entry(name: str, t: str):
    try:
        p = Path(name)
        if t == "f":
            p.touch(exist_ok=False)
            print(f"File created: {p}")
        elif t == "d":
            p.mkdir(parents=False, exist_ok=False)
            print(f"Directory created: {p}")
        else:
            print("Type must be 'f' or 'd'")
    except FileExistsError:
        print("Already exists.")
    except Exception as e:
        print(f"Create failed: {e}")

def delete_entry(name: str):
    try:
        p = Path(name)
        if not p.exists() and not p.is_symlink():
            print("Path not found.")
            return
        confirm = input(f"Are you sure you want to delete '{p}'? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("Cancelled.")
            return
        if p.is_dir() and not p.is_symlink():
            # remove dir recursively
            shutil.rmtree(p)
            print(f"Directory deleted: {p}")
        else:
            p.unlink()
            print(f"Deleted: {p}")
    except Exception as e:
        print(f"Delete failed: {e}")

def create_symlink(target: str, link_name: str):
    try:
        t = Path(target).resolve()
        if not t.exists():
            print(f"Target does not exist: {t}")
            return
        link = Path(link_name)
        if link.exists() or link.is_symlink():
            print("Link path already exists.")
            return
        os.symlink(str(t), str(link))
        print(f"Symlink created: {link} -> {t}")
    except Exception as e:
        print(f"Symlink failed: {e}")
