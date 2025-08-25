# UmaVer

A tiny Windows/Python utility to quickly switch between the **Global (Steam)** and **Japanese (DMM)** versions of *Uma Musume Pretty Derby*.

UmaVer works by swapping/renaming the game’s config folder at:

```
%LOCALAPPDATA%Low\Cygames\Umamusume
```

This avoids manual backups and lets you jump between **JP** and **Global** profiles in seconds.

---

## ✨ Features
- Fast switch between **JP** and **Global** configs
- Creates a **Start Menu** shortcut during setup
- Optional Windows notifications via **BurntToast**
- Uses **fzf** for a clean, interactive selection
- Simple install (copies files to `C:\UmaVer`)

> **Note**: You should have both game versions installed (JP via DMM, Global via Steam) before using UmaVer.

---

## 📦 Requirements
- **Windows 10/11**
- **Python 3.11+** [Download here](https://www.python.org/downloads/)
- **Both game versions installed** (Global via Steam, JP via DMM)
- **fzf** (required for menu selection)
- **BurntToast** PowerShell module (required for notifications)

### Installing dependencies (Both should also get installed when running the `setup.py`)
- **fzf** (choose one):
  - *winget*: `winget install junegunn.fzf`
  - *scoop*: `scoop install fzf`
  - *choco*: `choco install fzf`
- **BurntToast** (PowerShell):
  - `Install-Module -Name BurntToast -Scope CurrentUser`

---

## ⚙️ Installation
Clone the repository and run the setup script:

```powershell
git clone https://github.com/JOPATE/UmaVer
cd UmaVer
py ./setup.py
```

What the setup does:
- Copies the main script and assets to `C:\UmaVer` (e.g., `C:\UmaVer\UmaVer.py`)
- Adds an app **shortcut** to the **Start Menu**
- Installs/uses the included icon for easier identification

> If you run into permission prompts, approve them so the shortcut can be created.

---

## 🚀 Usage
You can start UmaVer in two ways:

1) **From Start Menu** → search for **UmaVer** and run it
2) **From terminal**:

```powershell
python C:\UmaVer\UmaVer.py
```

Follow the on-screen prompt to choose **Japan** or **Global**. UmaVer will safely swap the config folder and open the correct game version.

https://github.com/user-attachments/assets/85e0d786-e0b8-4d0a-a550-ab929a44be5f

> Make sure to launch both games at least once separately (Steam/DMM) with UmaVer so their folders are created as UmaVer will also start the game for you.

---

## 🔧 Troubleshooting
**`fzf` is not recognized**  
Confirm fzf is installed and on your PATH. Open a new terminal and run `fzf --version`. If it fails, reinstall by running the `setup.py` again, with winget/scoop/choco or restart your shell.

**No Windows notifications**  
Install BurntToast via PowerShell (`Install-Module BurntToast`). Also check Windows *Do Not Disturb / Focus Assist* settings.

**Icon not showing**  
This is cosmetic. Re-run setup, then sign out/in or reboot to refresh icon cache.

---

## 🧹 Uninstall
- Remove the folder `C:\UmaVer`
- Delete the **UmaVer** shortcut from the Start Menu (if present)


> Note: UmaVer only manipulates the *Umamusume* folder names under `%LOCALAPPDATA%Low`. It does **not** delete game content.

> I should make a `uninstall.py` now that i think about it...

---

## 🤝 Contributing
Contributions welcome! If you’d like to help:

1. **Fork** the repo
2. **Create a branch**: `git checkout -b feature/your-idea`
3. **Commit** your changes: `git commit -m "Add your feature"`
4. **Push** the branch: `git push origin feature/your-idea`
5. **Open a Pull Request** and describe your changes

> Just note: I don’t check GitHub very often, so responses might be a bit slow.

---

## 📄 License
This project is licensed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

---

## 🙏 Disclaimer
This project is **not affiliated** with Cygames, DMM, or Steam. Use at your own risk.

---

## 📌 FAQ
**Does UmaVer launch the game automatically?**  
Yep, and it also gives you a small notification, I might add a way to disable it in the future.

**Will switching break updates or downloads?**  
No. UmaVer only renames local config folders, so game files should remain untouched. 

**Can I use it without BurntToast?**  
Yep, Notifications are optional; everything else works normally. (did not test this tho, so it might not work.. but its meant to install by itself by running the `setup.py`)

**Where are the files stored again?**  
`%LOCALAPPDATA%Low\Cygames\Umamusume`
