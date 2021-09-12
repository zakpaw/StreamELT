import boto3
import StdOutListener
import KinesisListener
import time
from tweepy import OAuthHandler
from tweepy import Stream



class TweetsStreamer():
    """Universal Tweets Streamer Class"""
    def __init__(self, consumer_key: str, consumer_secret: str, 
                 access_token: str, access_token_secret: str):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.author = OAuthHandler(consumer_key, consumer_secret)
        self.author.set_access_token(access_token, access_token_secret)

    def to_kenesis_stream(self, stream_name: str, filter_list: list, languages: list=['en']):
        client = boto3.client('kinesis')

        while True:
            try:
                stream = Stream(self.auth, KinesisListener)
                stream.filter(track=filter_list, languages=languages, stall_warnings=True)
            except (AttributeError, Exception) as e:
                print(e)

    def to_stdout(self, stream: Stream, filter_list: list, languages: list=['en']):
        while True:
            try:
                stream = Stream(self.auth, StdOutListener)
                stream.filter(track=filter_list, languages=languages, stall_warnings=True)
                time.sleep(1)
            except (AttributeError, Exception) as e:
                print(e)