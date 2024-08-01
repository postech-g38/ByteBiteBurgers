import boto3


if __name__ == '__main__':
    client = boto3.client(
        'sqs', 
        region_name='us-west-2', 
        endpoint_url='http://localhost:4566',
        aws_access_key_id='localstack',
        aws_secret_access_key='localstack'
        )

    queue_create = client.create_queue(
        QueueName='tst.fifo',
        Attributes={
            'FifoQueue': 'true',
            'ContentBasedDeduplication': 'true'
        }

    )
    print(f"AWS_SIMPLE_QUEUE_SERVICE_URL: {queue_create['QueueUrl']}")
