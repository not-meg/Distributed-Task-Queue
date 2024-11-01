import kafka
import redis
import uuid
import json

class YADTQ:
    def __init__(self, kafka_broker, redis_host, redis_port):
        self.producer = kafka.KafkaProducer(bootstrap_servers=kafka_broker)
        self.redis_client = redis.Redis(host=redis_host, port=redis_port, db=0)

    def submit_task(self, task_type, args):
        task_id = str(uuid.uuid4())

        # prepare task data

        task = {
            "task_id": task_id,
            "task": task_type,
            "args": args
        }

       # send task to Kafka

        self.producer.send('tasks', value=json.dumps(task).encode('utf-8'))

        # store task status in Redis

        self.redis_client.set(task_id, json.dumps({
            "status": "queued",
            "result": None
        }))

        return task_id

    # check task status

    def check_status(self, task_id):
        task_data = self.redis_client.get(task_id)
        if task_data:
            return json.loads(task_data)
        else:
            return {"status": "unknown", "result": None}

