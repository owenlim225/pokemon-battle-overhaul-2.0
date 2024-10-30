import subprocess
import sys

# =======================================
# List of dependencies to install
# Add your dependencies here
# =======================================
dependencies = [
    "rich",
    "numpy",
    "pandas",
]

def install_package(package):
    """Install a package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"Successfully installed {package}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package}: {e}")

def check_and_install_pip():
    """Check if pip is installed, and install it if not."""
    try:
        import pip
        print("pip is already installed.")
    except ImportError:
        print("pip is not installed. Installing pip...")
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--default-pip"])

def initialize_packages():
    """Check pip and install all dependencies."""
    check_and_install_pip()

    for package in dependencies:
        install_package(package)

    print("\033c", end="")  # Clear console output (Unix and Windows compatible)

if __name__ == "__main__":
    initialize_packages()
