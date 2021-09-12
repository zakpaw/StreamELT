import json
from tweepy.streaming import StreamListener
from pprint import pprint

class KinesisListener(StreamListener):
    """Class inheriting from tweepy StreamListener
    created to modify on_data method to stream data
    to Kenesis Stream.
    """
    def on_data(self, data):
        run = True
        while run:
            tweet = json.loads(data)
            try:
                message = '\t'.join(tweet) + '\n'
                # kinesis_client.put_record(StreamName=)
            except(AttributeError, Exception) as e:
                pprint("***Error***: ", e)
                pass

    def on_error(self, status_code):
        pprint(status_code)
        if status_code == 420:
            return False
