import subprocess
from get_text import generate_concatenated_text
from rewrite_news import rewrite_news
from rewrite_news import get_points
from generate_avatar import process_synthesis

"""
url example: 
https://roma.repubblica.it/sport/2024/04/17/news/tifoso_roma_telefonata_radio_eutanasia_europa_league-422557771/?ref=RHLF-BG-P17-S1-T1
https://torino.repubblica.it/cronaca/2024/04/17/news/agente_penitenziaria_test_omosessualita_tar_condanna-422559123/?ref=RHLF-BG-P2-S1-T1
"""


def NewsAvatar(URL,website,language="IT"):

    result=dict()

    # Get URL input from command line
    url = URL

    # Get concatenated text from the webpage using CSS selectors
    text_contents = generate_concatenated_text(url,website)

    # print(text_contents+"\n")

    if text_contents:

        # Rewrite the news based on concatenated text
        news = rewrite_news(text_contents,language)
        summery=get_points(text_contents,language)
        result['news_script']=news
        result['news_summery']=summery
        # generate_text_image(summery)

        if news:
            # Process synthesis to generate avatar video and get the video URL
            avatar = process_synthesis(news,language)
            result['avatar']=avatar
            return result

        else:
            print("Failed to rewrite the news.")
            return "error: Failed to rewrite the news."
    else:
        print("Failed to get text content from the webpage.")
        return "error: Failed to get text content from the webpage."

# if __name__ == "__main__":
#     url="https://roma.repubblica.it/sport/2024/04/17/news/tifoso_roma_telefonata_radio_eutanasia_europa_league-422557771/?ref=RHLF-BG-P17-S1-T1"
#     NewsAvatar(utl,"LR","IT")
