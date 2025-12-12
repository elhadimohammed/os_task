
#!/usr/bin/env python3
# main.py
from file_manager import file_manager_menu
from user_manager import user_manager_menu
from process_manager import process_manager_menu

def main():
    while True:
        print("""
================= OS TASKS =================
1) File Manager
2) User Manager (requires sudo)
3) Process Manager
4) Exit
============================================
""")
        choice = input("Select option: ").strip()
        if choice == "1":
            file_manager_menu()
        elif choice == "2":
            user_manager_menu()
        elif choice == "3":
            process_manager_menu()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
