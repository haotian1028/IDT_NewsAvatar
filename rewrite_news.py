from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def rewrite_news(content):

    """
    This function generates news report content.

    Parameters:
    - content: A string containing the content for generating the news report.

    Returns:
    - A string representing the generated news report content.
    """

    prompt = "Vorrei che tu fossi un conduttore del telegiornale di Repubblica. Dovrai presentare le notizie sulla base dei contenuti che ti fornirò. Dovrai riassumere e riorganizzare il contenuto delle notizie che ti fornirò. La presentazione deve includere un'introduzione, un riassunto delle notizie e un resoconto dettagliato. Deve essere concisa e non superare le 300 parole.Iniziate con Cari telespettatori, benvenuti al notiziario di oggi"

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
