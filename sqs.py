import boto3
import os

QUEUE_URL = 'https://sqs.eu-west-1.amazonaws.com/282415712953/erik'
sqs = boto3.client(
    'sqs',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    region_name='eu-west-1'
)

def send(message):
    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        DelaySeconds=10,
        MessageBody=(message)
    )
    print('✉️ 💨  ' + response['MessageId'])

def receive():
    response = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=1,
        VisibilityTimeout=120,
        WaitTimeSeconds=0
    )

    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']

    
    print('📩 Received message: %s' % message)
    print('📭 receipt handle: %s' % receipt_handle)

def delete(rx_handle):
    # Delete received message from queue
    sqs.delete_message(
        QueueUrl=QUEUE_URL,
        ReceiptHandle=rx_handle
    )
    print('☠️ Deleted!')