import subprocess
import os
import shutil
from rich.console import Console

console = Console()

def run_shell(command, cli_name="BrahMos", cwd="Workspace"):
    """Executes a shell command after user confirmation."""
    console.print(f"\n[bold yellow]\\[!] {cli_name} wants to execute:[/bold yellow] [white]{command}[/white]")
    confirm = console.input("[bold green]Authorize execution? (y/n): [/bold green]").lower()
    
    if confirm == 'y':
        try:
            # Ensure cwd exists
            os.makedirs(cwd, exist_ok=True)
            
            # Dynamically find the best shell (especially for Termux/Android)
            shell_path = shutil.which("bash") or shutil.which("sh") or os.environ.get("SHELL")
            
            # Execute command inside the current working directory
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=120, executable=shell_path, cwd=cwd)
            output = f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
            return output
        except Exception as e:
            return f"Error executing command: {str(e)}"
    
    return "Command execution cancelled by user."
