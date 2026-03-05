from rich.console import Console
from rich.prompt import Prompt
import getpass

console = Console()

def ask_user_input(prompt_message, is_secret=False):
    """
    Prompts the user for input directly in the terminal.
    If is_secret is True, the input is hidden (useful for passwords, API keys, tokens).
    """
    console.print()
    if is_secret:
        # getpass hides the input while typing
        console.print(f"[bold magenta]│ 🔐 AI REQUEST:[/bold magenta] [white]{prompt_message}[/white]")
        user_response = getpass.getpass(prompt="╰─❯ ")
    else:
        console.print(f"[bold magenta]│ 📝 AI REQUEST:[/bold magenta] [white]{prompt_message}[/white]")
        user_response = console.input("[bold magenta]╰─❯ [/bold magenta]")
    
    return user_response
