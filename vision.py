
import os
import subprocess
from get_text import generate_concatenated_text
from rewrite_news import rewrite_news
from openai import OpenAI
from get_image import get_img_from_css_selectors

client = OpenAI(
    api_key=os.getenv("GPT_API_KEY")

)


# Get URL 
url = "https://genova.repubblica.it/cronaca/2024/04/29/news/incidente_sullautofiori_tir_si_ribalta_si_viaggia_su_una_sola_corsia-422771681/?ref=RHLF-BG-P18-S1-T1"

# Define default CSS selectors
css_selectors = [".story__title", ".story__summary", ".story__text"]
css_selector_image = ".story__media > picture:nth-child(1) > img:nth-child(4)"

# Get concatenated text from the webpage using CSS selectors
text_contents = generate_concatenated_text(url,css_selectors)

css_selector_image=".story__media > picture:nth-child(1) > img:nth-child(4)"


image=get_img_from_css_selectors(url,css_selector_image)

# print(text_contents+"\n")

if text_contents:

    # Rewrite the news based on concatenated text
    news = rewrite_news(text_contents)
    print(news)

# prompt= "Base on the news content:" + news +  "descirbe the image. And you're a news reporter, combine the image, report the news for me in 300 words"
prompt= "Base on the news content:" + news +  "descirbe the image."


response = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": prompt},
        {
          "type": "image_url",
          "image_url": {
            "url":image[0],
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print("\n"+response.choices[0].message.content)