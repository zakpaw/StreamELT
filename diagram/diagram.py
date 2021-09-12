from diagrams import Diagram, Cluster
from diagrams.aws.analytics import KinesisDataStreams, KinesisDataFirehose
from diagrams.aws.storage import S3, SimpleStorageServiceS3Bucket, SimpleStorageServiceS3Bucket
from diagrams.aws.compute import ECS
from diagrams.aws.ml import Sagemaker
from diagrams.saas.analytics import Snowflake
from diagrams.onprem.container import Docker
from diagrams.programming.language import Python


with Diagram(""):
    with Cluster("COVID19 Tweets Source"):
        with Cluster(""):
            ecs = ECS("")
            with Cluster(""):
                docker = Docker("containarized")
                get_tweets = Python("Stream COVID19 Tweets from Twitter API")
        # elb_tweets = aws.network.ELB("Load Balance streaming data")
        tweets_stream = KinesisDataStreams("Stream tweets")
    with Cluster("Data Lake"):
        tweets_firehose = KinesisDataFirehose("Transform to JSON's")
        with Cluster(""):
            s3staging = S3("S3")
            raw_bucket = SimpleStorageServiceS3Bucket("Raw Tweets")
            raw_to_standardzied = KinesisDataFirehose("Standardize")
            standardized_bucket = SimpleStorageServiceS3Bucket("Standardized Tweets")
            standardized_to_cleansed = KinesisDataFirehose("Cleanse")
            cleansed_bucket = SimpleStorageServiceS3Bucket("Cleansed Tweets")
    with Cluster("Warehousing"):
        snowflake = Snowflake("DW")
    sagemaker = Sagemaker("Sentiment analysis")

    get_tweets >> tweets_stream >> tweets_firehose >> raw_bucket
    raw_bucket >> raw_to_standardzied >> standardized_bucket >> standardized_to_cleansed >> cleansed_bucket
    standardized_bucket >> sagemaker
    cleansed_bucket >> snowflake