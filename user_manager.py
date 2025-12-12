
# user_manager.py
import subprocess
import shutil

def _run(cmd):
    """Run a command and show its output; raise if fails."""
    print(f"$ {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed (exit {e.returncode}).")

def _ensure(cmd_name):
    if shutil.which(cmd_name) is None:
        print(f"Missing system tool: {cmd_name}. Install it or run on a full Linux system.")

def user_manager_menu():
    while True:
        print("""
--- User Manager (requires sudo/root) ---
1) Add user
2) Delete user
3) Add group
4) Delete group
5) Change username
6) Change password
7) Assign user to group
8) Back
""")
        c = input("Choose: ").strip()
        if c == "1":
            _ensure("useradd")
            u = input("Username: ").strip()
            _run(["sudo", "useradd", "-m", u])  # create home
        elif c == "2":
            _ensure("userdel")
            u = input("Username: ").strip()
            print("This will remove the user; with -r it also removes home directory.")
            remove_home = input("Remove home directory? (y/n): ").strip().lower() == "y"
            cmd = ["sudo", "userdel"] + (["-r"] if remove_home else []) + [u]
            _run(cmd)
        elif c == "3":
            _ensure("groupadd")
            g = input("Group name: ").strip()
            _run(["sudo", "groupadd", g])
        elif c == "4":
            _ensure("groupdel")
            g = input("Group name: ").strip()
            _run(["sudo", "groupdel", g])
        elif c == "5":
            _ensure("usermod")
            old = input("Old username: ").strip()
            new = input("New username: ").strip()
            _run(["sudo", "usermod", "-l", new, old])
        elif c == "6":
            _ensure("passwd")
            u = input("Username: ").strip()
            _run(["sudo", "passwd", u])
        elif c == "7":
            _ensure("usermod")
            u = input("Username: ").strip()
            g = input("Group: ").strip()
            _run(["sudo", "usermod", "-aG", g, u])
        elif c == "8":
            break
        else:
            print("Invalid choice.")
