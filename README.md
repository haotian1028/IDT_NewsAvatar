# IDT_NewsAvatar

News Avatar Generator is a Python script that generates an avatar video based on the news content from a given webpage and provide API interfaces. It extracts text from the webpage, rewrites the news, and then synthesizes an avatar video to present the news in a dynamic format.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.8.x
- Required Python packages: `subprocess`, `dotenv`, `pathlib`, `requests`, `bs4` (BeautifulSoup), `OpenAI`

- An .env file should be created containing the following information:

    ```
    GPT_API_KEY = Your ChatGPT key
    Azure_SUBSCRIPTION_KEY = Your Azure Speech Lab subscription
    Azure_SERVICE_REGION = Your Azure Speech Lab  service region
    ```

## Usage

1. Run the `Routers.py` script to start the server

    ```bash
    python Routers.py
    ```

2. Call the APIs, example:

```javascript
    const data = {
        URL: "https://www.repubblica.it/......",
        website: "LR",
        language: "EN"
    };

    fetch('http://127.0.0.1:5000/api/getAvatar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
```

## API reference

### Endpoint: /api/getAvatar

Method: POST

Description: This API endpoint retrieves the avatar, news script, and news summary for a given URL from a specific website.

#### Request Body:

    URL (string, required): The URL of the news article.
    website (string, required(LR for La Repubblica)): The website code indicating where the news article is from.
    language (string, optional(IT or EN)): The desired language for the news script and summary. Defaults to "IT" if not provided.

Example:

```json
{
    "URL": "https://www.repubblica.it/politica/2024/05/10/news/salvini_dimissioni_toti_musumeci_magistratura-422900882/?ref=RHLF-BG-P5-S1-T1",
    "website": "LR",
    "language": "EN"
}
```

#### Response Body

    avatar (string): The URL of the avatar associated with the news article.
    news_script (string): The script of the news article in the desired language.
    news_summary (string): A summary of the news article in the desired language.

Example:

```json

{
    "result": {
        "avatar": "https://cvoiceprodwus2.blob.core.windows.net......",
        "news_script": "Dear viewers, welcome to today's news. In the latest development of the Toti case, government ministers have expressed criticism towards the judiciary. Vice Premier Matteo Salvini commented on the house arrest of Liguria Governor Giovanni Toti, stating that if every accused individual resigned, Italy would come to a standstill. Meanwhile, Minister Nello Musumeci questioned the timing of the investigation, stating concerns with the judiciary's advancement into areas outside their jurisdiction for the past 30 years. Other ministers, including Guido Crosetto and Daniela Santanchè, have also raised doubts about the timing of the investigation, particularly with the European elections approaching. Minister Adolfo Urso expressed solidarity with Toti, while Minister Carlo Nordio emphasized the importance of presumption of innocence and respecting due process. The Toti case continues to spark debate and calls for reforms in the judicial system to ensure fairness and justice. Stay tuned for more updates on this ongoing story.",
        "news_summary": "- Salvini and other ministers criticize magistrates over Toti's house arrest\n- Salvini: \"Italy stops if every accused resigns\"\n- Crosetto and Musumeci raise doubts about the timing of the investigation\n- Ministry of Defense and Civil Protection express perplexity\n- Musumeci defends Toti, criticizes the judiciary, and emphasizes the importance of politics\n- Other ministers, such as Santanchè and Urso, express solidarity with Toti and demand respect for the presumption of innocence"
    }
}
```


## Reference

[OpenAI](https://openai.com)

[Avatar Synthesis API](https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/yulin/batch-avatar/samples/batch-avatar/python)