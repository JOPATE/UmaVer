import os
import shutil
import subprocess
import time

# --- CONFIG --- #
INSTALL_DIR = r"C:\UmaVer"
START_MENU_DIR = os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs")
START_MENU_SHORTCUT = os.path.join(START_MENU_DIR, "UmaVer.lnk")

FILES_TO_COPY = [
    "UmaVer.py",
    "matikanetannhauser.ico",
    "matikanetannhauser.png",
    "teio.png",
]

# Resolve source folder relative to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_install_dir():
    os.makedirs(INSTALL_DIR, exist_ok=True)
    for f in FILES_TO_COPY:
        src = os.path.join(BASE_DIR, f)
        dst = os.path.join(INSTALL_DIR, os.path.basename(f))
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"✔ Copied {f} -> {dst}")
        else:
            print(f"⚠ Missing {src}, skipping...")

def install_shortcut():
    src_shortcut = os.path.join(BASE_DIR, "UmaVer.lnk")
    if os.path.exists(src_shortcut):
        shutil.copy2(src_shortcut, START_MENU_SHORTCUT)
        print(f"✔ Shortcut installed to Start Menu: {START_MENU_SHORTCUT}")
    else:
        print(f"⚠ Missing UmaVer.lnk in setup folder, skipping shortcut install.")

def ensure_burnttoast():
    ps_script = r"""
$ErrorActionPreference = 'SilentlyContinue'
if (-not (Get-Module -ListAvailable -Name BurntToast)) {
    try {
        [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
        if (-not (Get-PackageProvider -Name NuGet -ListAvailable)) {
            Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force -Scope CurrentUser
        }
        if ((Get-PSRepository -Name 'PSGallery').InstallationPolicy -ne 'Trusted') {
            Set-PSRepository -Name 'PSGallery' -InstallationPolicy Trusted
        }
        Install-Module -Name BurntToast -Force -Scope CurrentUser -AllowClobber
    } catch {
        Write-Host '⚠ Failed to install BurntToast'
        exit 1
    }
}
"""
    subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps_script],
        capture_output=True
    )
    print("✔ BurntToast ready")

def ensure_fzf():
    try:
        # Try to run fzf to see if it's installed
        subprocess.run(["powershell", "fzf", "--version"], capture_output=True, check=True)
        print("✔ fzf is already installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠ fzf not found, installing with winget...")
        try:
            subprocess.run(
                ["winget", "install", "-e", "--id", "junegunn.fzf"],
                check=True
            )
            print("✔ fzf installed successfully")
        except Exception as e:
            print(f"❌ Failed to install fzf: {e}")

def main():
    create_install_dir()
    install_shortcut()
    ensure_burnttoast()
    ensure_fzf()
    print("✅ Setup complete! UmaVer is installed at C:\\UmaVer and in Start Menu.")
    time.sleep(5)

if __name__ == "__main__":
    main()
