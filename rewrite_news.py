from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def rewrite_news(content,prompt_selection="IT"):

    """
    This function generates news report content.

    Parameters:
    - content: A string containing the content for generating the news report.
    - prompt_selection: IT(Italian),EN(English)

    Returns:
    - A string representing the generated news report content.
    """

    prompts = {'IT': "Vorrei che tu fossi un conduttore del telegiornale di Repubblica. Dovrai presentare le notizie sulla base dei contenuti che ti fornirò. Dovrai riassumere e riorganizzare il contenuto delle notizie che ti fornirò. La presentazione deve includere un'introduzione, un riassunto delle notizie e un resoconto dettagliato. Deve essere concisa e non superare le 300 parole.Iniziate con Cari telespettatori, benvenuti al notiziario di oggi",
               'EN': "I would like you to be an anchorman for the news of the Republic. You will have to present the news based on the content I will provide. You will have to summarise and reorganise the content of the news I will provide. The presentation must include an introduction, a news summary and a detailed account. It must be concise and not exceed 300 words.Start with Dear viewers, welcome to today's news"}

    prompt = prompts[prompt_selection]

    client = OpenAI(
        api_key=os.getenv("GPT_API_KEY")
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content}
        ]
    )

    return response.choices[0].message.content



def get_points(content,prompt_selection="IT"):

    """
    This function generates news report content.

    Parameters:
    - content: A string containing the content for generating the news report.

    Returns:
    - A string representing the generated news report content.
    """

    prompts = {"IT":"Riassumete le notizie che vi ho fornito in 50 parole o meno sotto forma di titoli, interruzioni di riga, punti elenco (interruzioni di riga per ogni punto elenco).",
               "EN":"Summarise the news I have provided in 50 words or less in the form of headings, line breaks, bullet points (line breaks per bullet point)."}

    prompt=prompts[prompt_selection]

    client = OpenAI(
        api_key=os.getenv("GPT_API_KEY")
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content}
        ]
    )

    return response.choices[0].message.content

# Example call 

# content = "The original news"
# news = rewrite_news(content)
# print(news)
