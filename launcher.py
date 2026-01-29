import os
import subprocess
import sys

def install_package(package):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    except subprocess.CalledProcessError:
        print(f'Failed to install {package}. Please install it manually.')
        sys.exit(1)

def main():
    # List of required packages
    required_packages = ['flask', 'requests', 'pandas']

    # Install required packages
    for pkg in required_packages:
        install_package(pkg)

    # Launch the Moodle Calendar Dashboard
    print('Launching Moodle Calendar Dashboard...')
    os.system('python moodle_calendar_dashboard.py')  # Replace with the actual entry point of your app

if __name__ == '__main__':
    main()