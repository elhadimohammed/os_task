
# OS Tasks

Menu-based console application for **Operating Systems** coursework.  
Implements three managers with a persistent loop and dedicated manual pages:

- **File Manager** (Task 1)
- **User Manager** (Task 2)
- **Process Manager** (Task 3)

---

## ✨ Features

### Task 1 — File Manager
- List files/directories (with permissions and types)
- Change permissions (`chmod`, numeric e.g., `755`)
- Create/delete files and directories (with confirmation for delete)
- Create symbolic links

### Task 2 — User Manager
- Add/delete users
- Add/delete groups
- Change account info (username, password)
- Assign users to groups

> ⚠️ **Requires sudo/root** for user and group operations.

### Task 3 — Process Manager
- List all processes (independent of terminal)
- List processes by user
- Show PIDs of all processes
- Run a process
- Stop a process (SIGSTOP)
- Send specific signals (e.g., SIGTERM, SIGKILL, SIGCONT)

---

## 🗂️ Project Structure
os_tasks/
├─ main.py               # Entry point: persistent menu
├─ file_manager.py       # Task 1 implementation
├─ user_manager.py       # Task 2 implementation (needs sudo)
├─ process_manager.py    # Task 3 implementation
├─ man_pages/
│   ├─ task1.1           # File Manager manual page
│   ├─ task2.1           # User Manager manual page
│   └─ task3.1           # Process Manager manual page
└─ README.md
