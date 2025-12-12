
# process_manager.py
import os
import signal
import subprocess

def process_manager_menu():
    while True:
        print("""
--- Process Manager ---
1) List all processes
2) List processes by user
3) Show PIDs of all processes
4) Run a process
5) Stop a process (SIGSTOP)
6) Send a signal to a process
7) Back
""")
        c = input("Choose: ").strip()
        if c == "1":
            list_all_processes()
        elif c == "2":
            user = input("Username: ").strip()
            list_processes_by_user(user)
        elif c == "3":
            show_all_pids()
        elif c == "4":
            cmd = input("Command to run (e.g., sleep 100): ").strip().split()
            run_process(cmd)
        elif c == "5":
            pid = int(input("PID: ").strip())
            stop_process(pid)
        elif c == "6":
            pid = int(input("PID: ").strip())
            print("Signals: 15=SIGTERM, 9=SIGKILL, 19=SIGSTOP, 18=SIGCONT, 1=SIGHUP, 2=SIGINT")
            sig = int(input("Signal number: ").strip())
            send_signal(pid, sig)
        elif c == "7":
            break
        else:
            print("Invalid choice.")

def list_all_processes():
    subprocess.run(["ps", "-e", "-o", "pid,user,comm,stat,etime"])

def list_processes_by_user(user: str):
    subprocess.run(["ps", "-u", user, "-o", "pid,user,comm,stat,etime"])

def show_all_pids():
    subprocess.run(["ps", "-e", "-o", "pid"])

def run_process(cmd_list):
    try:
        p = subprocess.Popen(cmd_list)
        print(f"Started: PID {p.pid}")
    except Exception as e:
        print(f"Start failed: {e}")

def stop_process(pid: int):
    try:
        os.kill(pid, signal.SIGSTOP)
        print(f"Sent SIGSTOP to PID {pid}")
    except PermissionError:
        print("Permission denied.")
    except ProcessLookupError:
        print("PID not found.")
    except Exception as e:
        print(f"Stop failed: {e}")

def send_signal(pid: int, sig_num: int):
    try:
        os.kill(pid, sig_num)
        print(f"Signal {sig_num} sent to PID {pid}")
    except PermissionError:
        print("Permission denied.")
    except ProcessLookupError:
        print("PID not found.")
    except Exception as e:
        print(f"Signal failed: {e}")
