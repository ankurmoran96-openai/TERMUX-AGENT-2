import requests
import json
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()

def discuss_and_plan(topic=""):
    """Enters an interactive discussion mode with the user using gpt-4o to brainstorm and finalize a project plan. Returns the final plan."""
    # Local import to avoid circular dependencies
    from config import MODEL_API_URL, MODEL_API_KEY
    
    title = "[bold magenta]🏛️ ARCHITECT MODE (GPT-4o)[/bold magenta]"
    subtitle = "[white]Type 'done' to finalize plan or 'cancel' to abort.[/white]"
    
    panel = Panel(
        f"{title}\n{subtitle}",
        border_style="magenta",
        expand=False,
        padding=(1, 2)
    )
    console.print()
    console.print(panel)
    console.print()
    
    messages = [
        {
            "role": "system", 
            "content": "You are an elite software architect. Discuss with the user to figure out what they want to build. Ask clarifying questions one at a time. Help them design the architecture, choose tech stacks, and structure the project. Keep your responses conversational but focused."
        }
    ]
    
    if topic:
        messages.append({"role": "user", "content": f"I want to build: {topic}. Let's discuss."})
        console.print(f" [magenta]├─[/magenta] [white]Initial Topic:[/white] {topic}")
    else:
        messages.append({"role": "user", "content": "What should we build? Help me come up with an idea or guide me."})

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MODEL_API_KEY}"
    }

    while True:
        payload = {
            "model": "gpt-4o",
            "messages": messages,
            "temperature": 0.7
        }

        try:
            with console.status("[bold magenta]...architect is typing...[/bold magenta]", spinner="dots"):
                resp = requests.post(MODEL_API_URL, headers=headers, json=payload, timeout=30)
                resp.raise_for_status()
                reply = resp.json()["choices"][0]["message"]["content"]
                messages.append({"role": "assistant", "content": reply})

            md = Markdown(reply)
            msg_panel = Panel(md, title="[bold magenta]Architect[/bold magenta]", title_align="left", border_style="magenta", expand=False)
            console.print()
            console.print(msg_panel)
            console.print()

        except Exception as e:
            console.print(f"[bold red]│ ✖ Error connecting to Architect:[/bold red] [white]{str(e)}[/white]")
            return "Discussion failed due to error."

        user_input = console.input(f"[bold magenta]╭─ You[/bold magenta]\n[bold magenta]╰─❯ [/bold magenta]")

        if user_input.lower() == 'cancel':
            console.print(f"[bold red]│ ✖ Discussion cancelled.[/bold red]")
            return "User cancelled the discussion."

        if user_input.lower() == 'done':
            messages.append({
                "role": "user", 
                "content": "Summarize our discussion into a highly detailed, step-by-step technical execution plan. This plan will be passed directly to an autonomous God Mode AI (BrahMos) to build. Include file structures, exact tech stacks, and step-by-step instructions. Do NOT include pleasantries, just the plan."
            })
            payload["messages"] = messages

            try:
                with console.status("[bold purple]...generating final blueprint...[/bold purple]", spinner="bouncingBar"):
                    resp = requests.post(MODEL_API_URL, headers=headers, json=payload, timeout=60)
                    resp.raise_for_status()
                    final_plan = resp.json()["choices"][0]["message"]["content"]
                
                final_title = "[bold magenta]🚀 FINAL BLUEPRINT SECURED[/bold magenta]"
                final_panel = Panel(final_title, border_style="magenta", expand=False, padding=(1, 2))
                console.print()
                console.print(final_panel)
                console.print(Markdown(final_plan))
                console.print()
                
                return f"FINAL PROJECT BLUEPRINT:\n\n{final_plan}\n\nProceed to execute this plan."
            except Exception as e:
                return f"Failed to generate final plan: {str(e)}"
        
        messages.append({"role": "user", "content": user_input})
