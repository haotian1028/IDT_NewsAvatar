# IDT_NewsAvatar

News Avatar Generator is a Python script that generates an avatar video based on the news content from a given webpage. It extracts text from the webpage, rewrites the news, and then synthesizes an avatar video to present the news in a dynamic format.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.8.x
- Required Python packages: `subprocess`, `json`, `logging`, `os`, `sys`, `time`, `dotenv`, `pathlib`, `requests`, `bs4` (BeautifulSoup), `subprocess`, `OpenAI`

- An .env file should be created containing the following information:

    ```
    GPT_API_KEY = Your ChatGPT key
    Azure_SUBSCRIPTION_KEY = Your Azure Speech Lab subscription
    Azure_SERVICE_REGION = Your Azure Speech Lab  service region
    ```

## Usage

1. Request the relevant services (if they don't exist), create the .env file

2. Navigate to the project directory:

    ```bash
    cd news-avatar-generator
    ```

3. Run the `NewsAvatar.py` script:

    ```bash
    python NewsAvatar.py
    ```

3. Enter the URL of the webpage containing the news content when prompted.

4. View the generated avatar video.

## Example

Here's an example of how to use the News Avatar Generator:

```bash
python NewsAvatar.py
Enter the URL of the webpage: https://roma.repubblica.it/sport/2024/04/17/news/tifoso_roma_telefonata_radio_eutanasia_europa_league-422557771/?ref=RHLF-BG-P17-S1-T1
```

## Reference

[OpenAI](https://openai.com)

[Avatar Synthesis API](https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/yulin/batch-avatar/samples/batch-avatar/python)