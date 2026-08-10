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

An advanced, interactive and fixed **TUI (Terminal User Interface)** and unified **CLI (Command Line Interface)** for running, configuring, installing, and diagnosing the **OpenClaw AI Assistant** ecosystem.

---

## 🤖 What is OpenClaw AI Assistant?

An extremely popular, fully autonomous, local-first personal developer AI agent. It operates on your local machine, interacting through your favorite chat apps, executing terminals, running code, and self-learning skills.

**OpenClaw-TUI is the ultimate console interface that allows you to manage, install, configure, and execute this incredible system from a single, unified workspace!**

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
- 📋 **System Diagnostics**:
  - Get a clear health report of your operating system, Node.js state, and AI gateway status.

---

## 📦 Prerequisites

OpenClaw-TUI is entirely self-contained inside Python's robust standard library. It has **zero external python dependencies**, ensuring it runs instantly on any server, container, or computer without installing packages.

- **Python**: 3.8 or newer (3.12+ recommended)
- **Node.js**: required by the underlying OpenClaw AI gateway (v22.22.3+ recommended)
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

# Check diagnostic report
./openclaw-tui status

# Install OpenClaw AI Assistant
./openclaw-tui install

# Modify settings for OpenClaw AI Assistant
./openclaw-tui configure

# Run OpenClaw AI Assistant
./openclaw-tui run
```

---

## 📋 Walkthrough Guide

### Interactive Main Menu

Upon running `./openclaw-tui`, you are greeted by our signature logo and a clean control panel menu:

```text
=== OpenClaw AI Assistant Control Panel ===

1) 📥 Install / Download
2) ⚙️ Configure Onboarding (openclaw onboard)
3) 🚀 Start Gateway Daemon
4) 🛑 Stop Gateway Daemon
5) 🔄 Restart Gateway Daemon
6) 💬 Launch Local Chat (TUI)
7) 📊 Open Browser Dashboard
8) 🩺 Run Doctor Diagnostics
9) 📋 System Diagnostics (OS & AI Status)
10) ❌ Exit
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
5. `test_dynamic_import_helpers`: Dynamically compiles and loads helpers directly from the script to test internal paths and methods.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) - see the file for details.
