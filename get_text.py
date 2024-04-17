import requests
from bs4 import BeautifulSoup
import subprocess

def get_text_from_css_selectors(url, css_selectors):
    """
    Get text content from specific CSS selectors in a webpage.

    Args:
    - url: String, URL of the webpage to fetch content from.
    - css_selectors: List of CSS selectors used to locate elements for extracting text content.

    Returns:
    - List of tuples, each tuple containing text content corresponding to the CSS selector.
    """
    # Send a GET request to fetch webpage content
    response = requests.get(url)
    if response.status_code == 200:
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        text_contents = []
        # Use given CSS selectors to locate elements and extract text content
        for css_selector in css_selectors:
            elements = soup.select(css_selector)
            text_content = [element.text.strip() for element in elements]
            text_contents.append(text_content)
        return text_contents
    else:
        print(f"Failed to fetch webpage content: {response.status_code}")
        return None

def generate_concatenated_text(url, css_selectors):
    """
    Get text content from a given website and concatenate it into a single string.

    Args:
    - url: String, URL of the webpage to fetch content from.
    - css_selectors: List of CSS selectors used to locate elements for extracting text content.

    Returns:
    - String, concatenated text content.
    """
    text_contents = get_text_from_css_selectors(url, css_selectors)
    if text_contents:
        story_title, story_summary, story_text = text_contents
        concatenated_text = "Title of the news: " + story_title[0] + "Summary of the news: " + story_summary[0] +  "Text of the news: " + story_text[0]
        concatenated_text = concatenated_text.replace("\n", "").replace("\r", "").replace('"', '').replace("'", "\\'")
        return concatenated_text
    else:
        print("Failed to get text content from CSS selectors")
        return None

# Example Call
# url = "https://www.repubblica.it/economia/2024/04/17/news/enrico_letta_mercato_unico_ue-422557638/?ref=RHLF-BG-P1-S1-T1"
# css_selectors = [".story__title", ".story__summary", ".story__text"]
# concatenated_text = generate_concatenated_text(url, css_selectors)
# if concatenated_text:
#     print(concatenated_text)
