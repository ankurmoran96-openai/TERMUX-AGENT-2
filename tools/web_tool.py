import requests
from bs4 import BeautifulSoup
try:
    from googlesearch import search
except ImportError:
    import subprocess
    import sys
    subprocess.run([sys.executable, "-m", "pip", "install", "googlesearch-python"], capture_output=True)
    from googlesearch import search

def google_search(query, num_results=5):
    """Searches Google and returns a list of URLs."""
    try:
        # Pass timeout to prevent hanging, handle empty list
        results = list(search(query, num_results=num_results, sleep_interval=1, timeout=10))
        if not results:
            return "No results found for that query."
        return "\n".join(results)
    except Exception as e:
        return f"Search Error: {str(e)}"

def web_browse(url):
    """Scrapes the text content of a webpage."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.extract()
            
        text = soup.get_text()
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text[:5000] # Return first 5000 chars to avoid token limit
    except Exception as e:
        return f"Browse Error: {str(e)}"
