import subprocess
import sys

def create_requirements_txt():
    """
    Create a requirements.txt file based on installed packages.
    """
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install','gunicorn'], shell=True)
        subprocess.check_call([sys.executable, '-m', 'pip', 'freeze', '>', 'requirements.txt'], shell=True)
        print("requirements.txt file created successfully.")
    except subprocess.CalledProcessError:
        print("Failed to create requirements.txt file.")

def run_server():
    """
    Run Django server using Gunicorn.
    """
    try:
        subprocess.check_call(['gunicorn', 'Monthly_Expenses.wsgi:application'])
    except subprocess.CalledProcessError:
        print("Failed to run the server.")

if __name__ == "__main__":
    create_requirements_txt()
    run_server()
