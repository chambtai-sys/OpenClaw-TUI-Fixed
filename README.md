# OpenClaw-TUI-Fixed

```text
 ██████╗ ██████╗ ███████╗███╗   ██╗ ██████╗██╗      █████╗ ██╗█╗  ██╗
██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██║     ██╔══██╗██║╚█╗██╔╝
██║   ██║██████╔╝█████╗  ██╔██╗ ██║██║     ██║     ███████║██║ ╚███╔╝
██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║██║     ██║     ██╔══██║██║ ██╔██╗
╚██████╔╝██║     ███████╗██║ ╚████║╚██████╗███████╗██║  ██║██║██╔╝ ██╗
 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
                       ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
                       ───█▒▒░░░░░░░░░▒▒█───
                       ────█░░█░░░░█░░█────
                       ─▄▄▄█░░░░▀▀░░░░█▄▄▄─
                       ─█░░░▀▄░░░░░░▄▀░░░█─
                               TUI Tool v1.0.0
```

An advanced, interactive and fixed **TUI (Terminal User Interface)** and unified **CLI (Command Line Interface)** for running, configuring, installing, and diagnosing the **OpenClaw** ecosystem.

---

## 🌟 The Naming Collision Mystery Solved!

In the software development and retro-gaming worlds, **OpenClaw** has two vastly different but equally famous identities:

1. **🤖 The AI Assistant (`openclaw/openclaw`)**:
   An extremely popular, fully autonomous, local-first personal developer AI agent. It operates on your local machine, interacting through your favorite chat apps, executing terminals, running code, and self-learning skills.
2. **🏴‍☠️ The Game Engine (`pjasicek/OpenClaw`)**:
   A modern open-source C++ and SDL2 recreation of Monolith's beloved 1997 2D side-scrolling platformer, **"Captain Claw"** (featuring the legendary pirate cat Nathaniel J. Claw). It allows gamers to play the game natively on modern operating systems at high resolutions.

**OpenClaw-TUI is the ultimate bridge that allows you to manage, install, configure, and execute BOTH incredible systems from a single, unified console workspace!**

---

## ✨ Features

- 🎨 **Gorgeous ANSI UI Branding**: Highlights terminal output with distinct colors for successes, alerts, inputs, and system information.
- 🚀 **Two Ways to Run**:
  - **Interactive TUI Mode**: A guided terminal selection menu perfect for humans.
  - **Automated CLI Mode**: Straightforward command line arguments perfect for scripts, aliases, and automation.
- 🤖 **AI Assistant Integration**:
  - Install standard, globally packed, or localized source-built OpenClaw gateway servers.
  - Guided wizard configuration, onboarding, and API provider setups.
  - Direct background daemon control: Start, Stop, and Restart gateways.
  - Run the interactive chat terminal (`tui`) or launch the web dashboard.
- 🏴‍☠️ **Captain Claw Game Engine Integration**:
  - Verify system prerequisites (SDL2, SDL2_image, SDL2_ttf, SDL2_mixer, CMake) across Ubuntu/Debian, macOS (Homebrew), and Windows.
  - Clone, fetch, and compile the latest Game Engine repository from source.
  - Check, locate, or copy required asset files like `CLAW.REZ`.
  - **Interactive XML Config Editor**: Modify game screen resolution, toggle fullscreen mode, and control audio volume without touching manual text documents.
- 📋 **Unified System Diagnostics**:
  - Get a single clear health report of your operating system, Node.js state, AI gateway status, and Game Engine directories.

---

## 📦 Prerequisites

OpenClaw-TUI is entirely self-contained inside Python's robust standard library. It has **zero external python dependencies**, ensuring it runs instantly on any server, container, or computer without installing packages.

- **Python**: 3.8 or newer (3.12+ recommended)
- **Git**: Required for cloning source repositories

---

## 🚀 Quick Start

### 1. Download & Make Executable

Clone this repository and mark the main script as executable:

```bash
chmod +x openclaw-tui
```

### 2. Launch Interactive TUI

Simply run the tool without any command-line arguments to access the interactive menus:

```bash
./openclaw-tui
```

### 3. Non-Interactive CLI Commands

Use single-line CLI commands for speed and scripting automation:

```bash
# View help & documentation
./openclaw-tui --help

# Check unified system diagnostic report
./openclaw-tui status

# Install target component (ai / game)
./openclaw-tui install ai
./openclaw-tui install game

# Modify settings for specified component
./openclaw-tui configure ai
./openclaw-tui configure game

# Start/Run specified component
./openclaw-tui run ai
./openclaw-tui run game
```

---

## 📋 Walkthrough Guide

### Interactive Main Menu

Upon running `./openclaw-tui`, you are greeted by our signature Captain Claw ASCII logo and a main directory choice:

```text
Welcome to the ultimate OpenClaw TUI Suite! Choose a service to configure/run:

  1) 🤖 OpenClaw AI Assistant  (Personal Autonomous Developer Agent)
  2) 🏴‍☠️ OpenClaw Game Engine  (Captain Claw 1997 HD Reimplementation)
  3) 📋 Unified Diagnostics  (Combined System Check)
  4) ℹ️ Learn More          (About the OpenClaw Name Ecosystem)
  5) ❌ Exit
```

### Interactive XML Editor (Game Engine)

When configuring the Captain Claw Game Engine, you don't need to manually parse XML nodes. The tool displays your current parameters and lets you modify them through elegant prompts:

```text
[*] Current Video Resolution: 1024x768
[*] Fullscreen: false
[*] Sound Volume: 100 / Music Volume: 100

Select parameters to change:
1) Edit Resolution (Width & Height)
2) Toggle Fullscreen Mode
3) Edit Audio Settings
4) View config.xml Raw File
5) Back to main menu
```

---

## 🧪 Developer & Quality Assurance

To guarantee code reliability and prevent regression, OpenClaw-TUI comes with a comprehensive suite of unit and integration smoke tests.

Run the test suite using Python's standard unittest library:

```bash
python3 test_openclaw_tui.py
```

### Verified Test Cases:
1. `test_executable_exists`: Assures permissions and executable bits are correctly set.
2. `test_help_command`: Confirms `--help` displays standard logo, descriptions, and exits with code 0.
3. `test_status_command`: Confirms `status` command parses environment info and runs non-interactively.
4. `test_invalid_command`: Ensures unknown commands output to stderr and exit with code 1.
5. `test_dynamic_import_helpers`: Dynamically compiles and loads helpers directly from the script (even without a `.py` extension) to test internal paths, config builders, and asset locators.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) - see the file for details.
