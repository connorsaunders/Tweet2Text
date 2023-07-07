# Tweet2Text

**This script can be thought of as an automated Tweet to text bot.**

Tweet2Text (Tweet to Text) is a Python script that utilizes Tweepy to connect to Twitter's API and scrape tweets from a user(s) containing images or text. The script uses OCR technology to read text from images and sends the scraped text to a specified phone number through the macOS Messages app.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a macOS machine (must have iMessage enabled)
- Python 3.x installed.
- You have a Twitter Developer account with access to API keys and Bearer Token.
- You have the following Python libraries installed:
    - `tweepy`
    - `pytesseract`
    - `PIL`
- [jq](https://stedolan.github.io/jq/) installed on your system.
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed on your system.
- Ensure that you have permission for sending messages through the macOS Messages app (you should be asked when running the script)

## Installation

1. Clone the GitHub repository.
2. Install the required Python libraries:

`pip install tweepy pytesseract Pillow`


## Configuration

1. Open the script and set your Twitter API credentials (`api_key`, `api_key_secret`, `access_token`, `access_token_secret`, and `bearer_token`).
2. Set the phone number (`phoneNumber`) where you want to send the scraped text.

The script is configured to extract text that follows the word "text" (case insensitive).
You can modify the regular expression pattern within the script to fit your requirements.
The [stream](https://docs.tweepy.org/en/stable/streaming.html) the script listens to can be configured to your liking by adding more stream rules.

## Usage

Run the script using Python:

```bash
python main.py
```

This script can be utilized for fast response times in code word giveaways.

The script listens to a Twitter stream. When it detects a tweet containing an image, the image is downloaded, then the script uses OCR technology to read text from the image. It also scans the text within tweets. If the text matches a specific pattern, it sends the text to the specified phone number through the macOS Messages app. The script also plays a notification sound.

## Acknowledgements
Tweepy, for providing a Python wrapper for the Twitter API.
Tesseract OCR, for providing OCR technology.

## Disclaimer

The script is provided for educational purposes only. It is the responsibility of the user to ensure that the script is used in compliance with Twitter’s terms of service and applicable laws. The author of this script is not responsible for any misuse or any damages resulting from the use of this script.

