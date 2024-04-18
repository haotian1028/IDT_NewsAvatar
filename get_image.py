import requests
from bs4 import BeautifulSoup
import subprocess

# url="https://www.repubblica.it/politica/2024/04/18/news/aborto_governo_lega_pro_life_consultori-422575453/?ref=RHLF-BG-P1-S2-F"
# css_selectors=".story__media > picture:nth-child(1) > img:nth-child(4)"

def get_img_from_css_selectors(url, css_selectors):

    # Send a GET request to fetch webpage content
    response = requests.get(url)
    if response.status_code == 200:
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        image_elements = soup.select(css_selectors)
        image_links = [element['src'] for element in image_elements]
        # Use given CSS selectors to locate elements and extract text content
        return image_links
    else:
        print(f"Failed to fetch webpage content: {response.status_code}")
        return None



