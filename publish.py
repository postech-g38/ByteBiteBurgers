import json

import boto3


if __name__ == '__main__':
    client = boto3.client(
        'sqs', 
        region_name='us-west-2', 
        endpoint_url='http://localhost:4566',
        aws_access_key_id='localstack',
        aws_secret_access_key='localstack'
        )
    
    message = {
        'pedido_id': 123,
        'usuario_id': 123,
        'valor': 44.00,
        'metodo': 'dinheiro'
    }

    queue_publish = client.send_message(
            MessageGroupId='OrderService',
            QueueUrl='http://sqs.us-west-2.localstack:4566/000000000000/tst.fifo',
            MessageBody=json.dumps(message)
        )
