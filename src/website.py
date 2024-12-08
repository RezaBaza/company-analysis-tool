import requests
from bs4 import BeautifulSoup

class Website:
    def __init__(self, url):
        self.url = url
        self.body = self.scrape_website()

    def scrape_website(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract relevant content from the webpage, removing irrelevant elements
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()

        return soup

    def get_contents(self):
        title = self.scrape_website().title.string if self.scrape_website().title else "No title found"
        text = self.scrape_website().body.get_text(separator="\n", strip=True)
        return f"Webpage Title:\n{title}\nWebpage Contents:\n{text}\n\n"
