import time
import boto3


def generate(stream_name, kinesis_client):
    while True:
        records = "Test Message"
        kinesis_client.put_records(StreamName=stream_name, Records=records)
        time.sleep(0.1)


if __name__ == "__main__":
    generate(stream_name="ExampleInputStream", kinesis_client=boto3.client('kinesis'))