#!/usr/bin/env python3
import os
import sys
import subprocess
import urllib.request
from pathlib import Path

def main():
    print("\n" + "="*60)
    print("  📚 MOODLE CALENDAR DASHBOARD - SETUP")
    print("="*60 + "\n")
    
    # Create directory
    dashboard_dir = Path.home() / "Moodle-Dashboard"
    dashboard_dir.mkdir(exist_ok=True)
    os.chdir(dashboard_dir)
    
    # Step 1: Upgrade pip
    print("[1/4] 📦 Upgrading pip to 25.3...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip==25.3"], 
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("      ✅ Done\n")
    
    # Step 2: Install dependencies
    print("[2/4] 📦 Installing dependencies...")
    deps = ["requests", "google-auth-oauthlib", "google-auth-httplib2", 
            "google-api-python-client", "PyQt6", "pillow", "python-dotenv"]
    subprocess.run([sys.executable, "-m", "pip", "install"] + deps,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("      ✅ Done\n")
    
    # Step 3: Download install.py
    print("[3/4] 📥 Downloading dashboard application...")
    try:
        urllib.request.urlretrieve(
            "https://raw.githubusercontent.com/mcmillenmelvin000/Moodle-Calendar-Dashboard/main/install.py",
            "install.py"
        )
        print("      ✅ Done\n")
    except Exception as e:
        print(f"      ❌ Error: {e}\n")
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Step 4: Launch
    print("[4/4] 🚀 Launching dashboard...\n")
    subprocess.Popen([sys.executable, "install.py"])

if __name__ == "__main__":
    main()