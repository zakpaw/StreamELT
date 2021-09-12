import TweetsStreamer

if __name__ == "__main__":
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''
    streamer = TweetsStreamer(consumer_key, consumer_secret, \
                            access_token, access_token_secret)
    streamer.to_stdout()
    # to_kenesis_stream(stream_name="ExampleInputStream", kinesis_client=boto3.client('kinesis'))