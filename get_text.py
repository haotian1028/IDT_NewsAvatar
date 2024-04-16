import requests
from bs4 import BeautifulSoup
import subprocess

# Get content from website and pass it to AI-generation.py to generate a video.

# Put url and css selectors here

url = "https://roma.repubblica.it/cronaca/2024/04/16/news/guerra_israele_manifestazione_sapienza_di_roma-422546836/?ref=RHLF-BG-P1-S1-T1"
css_selectors = [".story__title", ".story__summary", ".story__text"]

def get_text_from_css_selectors(url, css_selectors):
    # Send a GET request to fetch the webpage content
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        text_contents = []
        # Use the given CSS selectors to find the corresponding elements and extract text content
        for css_selector in css_selectors:
            elements = soup.select(css_selector)
            text_content = [element.text.strip() for element in elements]
            text_contents.append(text_content)
        return tuple(text_contents)
    else:
        print(f"Failed to fetch webpage content: {response.status_code}")
        return None

# Call the function and pass URL and CSS selector list



text_contents = get_text_from_css_selectors(url, css_selectors)
if text_contents:
    story_title, story_summary, story_text = text_contents
    # print("story_title:", story_title)
    # print("story_summary:", story_summary)
    # print("story_text:", story_text)



    # Call AI-generation.py

    concatenated_text = "Salve, la seguente notizia per voi: " + story_title[0] + "\r\n" + story_summary[0]

    print(concatenated_text)

    subprocess.run(["python", "AI-generation.py", concatenated_text], shell=True)


else:
    print("Failed to get text content from CSS selectors")
