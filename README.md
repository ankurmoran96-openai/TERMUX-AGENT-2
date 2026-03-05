# ⚡ BrahMos Core (God Mode AI CLI)

BrahMos is an autonomous, terminal-based AI orchestrator capable of reading, writing, planning, and executing complex software engineering tasks directly on your machine.

## ✨ Features
* **Modern Rich UI**: Fully animated terminal interface with Markdown parsing and syntax highlighting.
* **Autonomous Workspace**: Automatically creates and safely isolates all generated code into a local `Workspace` directory.
* **Interactive Architect Mode**: Uses GPT-4o to brainstorm and map out project blueprints before executing them.
* **Dynamic Navigation**: Move the AI seamlessly through your file system using `/cd path/to/folder`.
* **Sub-Shell Drop-in**: Use the `/shell` command to instantly drop into an interactive terminal in your active workspace without breaking context.
* **GitHub Integration**: Ask the AI to push your projects straight to GitHub! Just provide a token and an empty repo, and it handles the git commands.
* **Auto-dependency Resolution**: Never worry about missing packages; the system installs what it needs dynamically.

## 🚀 Installation

You can install BrahMos directly from GitHub. This will automatically download the code, install dependencies, and register the global `brahmos` command on your system.

**Run this single command in your terminal:**
```bash
pip install git+https://github.com/ankurmoran96-openai/TERMUX-AGENT-2.git
```

## 💻 Usage

Once the installation finishes, you can launch the AI from anywhere in your terminal by simply typing:

```bash
brahmos
```

*(Note: The API key is currently built-in for immediate use. You do not need to configure any `.env` files right now!)*

### Commands
* `/cd <path>` - Change the directory the AI is actively working in.
* `/shell` - Drop into an interactive terminal inside the current working directory.
* `clear` - Clear the terminal screen.
* `exit` or `quit` - Shutdown BrahMos.

## 🛡️ Architecture & Safety
By default, the AI is sandboxed into a `./Workspace` directory that is created wherever you run the `brahmos` command. It will write files, start servers, and execute code within this directory unless you explicitly tell it to navigate elsewhere using the `/cd` command.
