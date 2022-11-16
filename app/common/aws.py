import json
import uuid
import boto3

from config import JsonConfig


class AwsSQS:
    sqs = boto3.resource('sqs', region_name='ap-northeast-2',
                         aws_access_key_id=JsonConfig.get_data('SQS_ACCESS_KEY'),
                         aws_secret_access_key=JsonConfig.get_data('SQS_SECRET_KEY'))

    def __init__(self, queue_name: str):
        self.queue = self.sqs.get_queue_by_name(QueueName=queue_name)

    def send_message(self, message_body: dict):
        return self.queue.send_message(
            MessageBody=json.dumps(message_body),
            MessageGroupId='default',
            MessageDeduplicationId=str(uuid.uuid4())
        )
