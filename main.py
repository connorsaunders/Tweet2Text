###########################################################################################
#                                       Imports
###########################################################################################
import tweepy
import re
import subprocess
import pytesseract
from PIL import Image

###########################################################################################
#                       vvv Add API Keys + bearer token below vvv
###########################################################################################
api_key = ""
api_key_secret = ""
access_token = ""
access_token_secret = ""
bearer_token = ""

client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

###########################################################################################
#                          vvv Add number to text below vvv
###########################################################################################
phoneNumber = ""

###########################################################################################
#                                Client connection
###########################################################################################

class MyStream(tweepy.StreamingClient):
    def on_connect(self):
        print("~ Connected ~")
        
###########################################################################################
#                                Image detection
###########################################################################################
    def on_tweet(self, tweet):
        if 'attachments' in tweet and 'media_keys' in tweet['attachments']:

            id = tweet['id']

            custom_filename = "ChipImage.jpg" 
            curl_command = f'curl --request GET \'https://api.twitter.com/2/tweets?ids={id}&tweet.fields=attachments&expansions=attachments.media_keys&media.fields=url\' --header \'Authorization: Bearer {bearer_token}\' | jq -r \'.includes.media[].url\' | xargs wget -P ~/Desktop/ChipScrape -O {custom_filename}'
            output = subprocess.check_output(curl_command, shell=True)

            image_path = "ChipImage.jpg"
            imageText = pytesseract.image_to_string(image_path)

            match = re.search(r'[tT]ext\s(.+?)\s', imageText)
            print(imageText)
            print("#####################")
            if match:
                captured_word = match.group(1)
                send_message(phoneNumber, captured_word)
                print(captured_word)
                subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])

            else:
                print("No match found")
###########################################################################################
#                                Text detection
###########################################################################################
        else:
            text = tweet.text
            match = re.search(r'[tT]ext\s(.+?)\s', text)
            if match:
                captured_word = match.group(1)
                send_message(phoneNumber, captured_word)
                subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])
                print(captured_word)
                print("#############################################################")

###########################################################################################
#                                     Send message
###########################################################################################

def send_message(recipient, message):
    script = f'tell application "Messages" to send "{message}" to buddy "{recipient}" of service 2'
    subprocess.run(['osascript', '-e', script])

###########################################################################################
#                                Print tweet details
###########################################################################################

def print_object(self, obj):
    print("\n".join(["%s: %s" % (attr, getattr(obj, attr)) for attr in dir(obj) if not attr.startswith('_')]))

###########################################################################################
#                                Get current stream rules
###########################################################################################

def get_current_rules(stream):
    rules = stream.get_rules()
    if rules.data:
        print("Current stream rules:")
        for rule in rules.data:
            print(rule)
    else:
        print("No stream rules found.")

###########################################################################################
#                                     Delete rules
###########################################################################################

def delete_all_rules(stream):
    rules = stream.get_rules()
    ids = [rule.id for rule in rules.data]
    if not ids:
        return stream.delete_rules(ids=ids)

###########################################################################################
#                                   Enable stream
###########################################################################################
stream = MyStream(bearer_token=bearer_token)

try:
    stream.filter(tweet_fields=['context_annotations', 'created_at'],
                    media_fields=['preview_image_url'], expansions='attachments.media_keys')

except KeyboardInterrupt:
    print("Streaming stopped by the user")
finally:
    stream.disconnect()
