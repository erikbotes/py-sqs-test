import boto3
import os
from settings import QUEUE_URL, AWS_REGION

sqs = boto3.client(
    'sqs',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    region_name=AWS_REGION
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

    if 'Messages' in response and len(response['Messages']) > 0:
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']

        
        print('📩  Received message: %s' % message['Body'])
        print('📭  receipt handle: %s' % receipt_handle)

        return message['Body'], receipt_handle
    else:
        print("No messages :'(")

def delete(rx_handle):
    # Delete received message from queue
    sqs.delete_message(
        QueueUrl=QUEUE_URL,
        ReceiptHandle=rx_handle
    )
    print('☠️  Deleted!')