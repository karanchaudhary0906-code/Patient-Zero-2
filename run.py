import os
import sys
import subprocess

def main():
    print("=" * 60)
    print("PATIENT ZERO: THE MISSING CONTEXT")
    print("Longitudinal Patient Timeline & Sourced Insights Platform")
    print("=" * 60)
    
    # Path to virtual env python
    venv_python = os.path.join(os.path.dirname(__file__), ".venv", "Scripts", "python.exe")
    if not os.path.exists(venv_python):
        venv_python = sys.executable

    print("\n[+] Starting server at:")
    print("    • Local:   http://127.0.0.1:8000")
    print("    • Network: http://0.0.0.0:8000 (accessible on phone via your laptop IP)")
    print("[+] Press Ctrl+C to stop.\n")
    
    cmd = [venv_python, "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n[!] Server stopped by user.")

if __name__ == "__main__":
    main()