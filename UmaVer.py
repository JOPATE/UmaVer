import os
import subprocess
import time
import threading

# --- CONFIG --- #
BASE_PATH = os.path.expandvars(r"%LOCALAPPDATA%Low\Cygames")
ACTIVE = os.path.join(BASE_PATH, "Umamusume")
JP = os.path.join(BASE_PATH, "Umamusume_DMM")
GLOBAL = os.path.join(BASE_PATH, "Umamusume_Global")

DMM_EXE = r"C:\Program Files\DMMGamePlayer\DMMGamePlayer.exe"  # <- update path
STEAM_EXE = r"C:\Program Files (x86)\Steam\steam.exe"
STEAM_GAME_ID = "3224770"  # <- replace with correct Uma Global Steam AppID

# --- HELPERS --- #
def detect_last_version():
    """Detects which version was last run based on folder layout."""
    if os.path.exists(ACTIVE) and os.path.exists(GLOBAL) and not os.path.exists(JP):
        return "jp"
    elif os.path.exists(ACTIVE) and os.path.exists(JP) and not os.path.exists(GLOBAL):
        return "global"
    return None

def switch_to(version):
    """Switch folder layout to requested version."""
    last = detect_last_version()

    if version == "jp" and last != "jp":
        if os.path.exists(ACTIVE):
            os.rename(ACTIVE, GLOBAL)  # push Global aside
        if os.path.exists(JP):
            os.rename(JP, ACTIVE)

    elif version == "global" and last != "global":
        if os.path.exists(ACTIVE):
            os.rename(ACTIVE, JP)  # push JP aside
        if os.path.exists(GLOBAL):
            os.rename(GLOBAL, ACTIVE)

def vpn_connect_jp():
    print("🔗 Connecting NordVPN to Japan...")
    subprocess.run(r'start "" /D "C:\Program Files\NordVPN" nordvpn -c -g japan', shell=True)

def vpn_disconnect():
    print("🔌 Disconnecting NordVPN...")
    subprocess.run(r'start "" /D "C:\Program Files\NordVPN" nordvpn -d', shell=True)

def auto_disconnect(delay=60):
    time.sleep(delay)
    vpn_disconnect()

def launch_jp():
    switch_to("jp")
    #vpn_connect_jp()
    #threading.Thread(target=auto_disconnect, args=(45,)).start()  # disconnect after 1 minute
    print("🚀 Launching Uma Musume Global via DMM...")
    send_toast("Japanese Server", "Launching Uma Musume JP via DMM", r"C:/UmaVer/matikanetannhauser.png")
    subprocess.Popen([DMM_EXE, "dmmgameplayer://play/GCL/umamusume/cl/win"])

def launch_global():
    switch_to("global")
    print("🚀 Launching Uma Musume Global via Steam...")
    send_toast("Global Server", "Launching Uma Musume Global via Steam", r"C:/UmaVer/teio.png")
    subprocess.Popen([STEAM_EXE, f"steam://rungameid/{STEAM_GAME_ID}"])

def send_toast(title: str, message: str, icon_path: str = None):
    # Escape strings for PowerShell
    title = title.replace('"', '`"')
    message = message.replace('"', '`"')

    if icon_path and os.path.exists(icon_path):
        ps_command = f'New-BurntToastNotification -Text "{title}", "{message}" -AppLogo "{icon_path}"'
    else:
        ps_command = f'New-BurntToastNotification -Text "{title}", "{message}"'

    # Run PowerShell with BurntToast
    subprocess.run([
        "powershell",
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-Command", ps_command
    ])

# --- MAIN --- #
def main():
    try:
        # Build the fzf menu
        result = subprocess.run(
            ["fzf", "--prompt=Select version: ", "--height=5", "--reverse"],
            input="Japan\nGlobal\n",
            text=True,
            capture_output=True,
            check=True
        )
        choice = result.stdout.strip().lower()
    except subprocess.CalledProcessError:
        print("No selection made.")
        return

    if choice == "japan":
        launch_jp()
    elif choice == "global":
        launch_global()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
