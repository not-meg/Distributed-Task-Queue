import yadtq

class Client:
    def __init__(self):
        # Initialize the YADTQ API
        self.yadtq = yadtq.YADTQ(kafka_broker='localhost:9092', redis_host='localhost', redis_port=6379)

    def submit_task(self, task_type, args):
        # Submit task via YADTQ API and return the task ID
        return self.yadtq.submit_task(task_type, args)

    def check_status(self, task_id):
        # Check task status via YADTQ API
        return self.yadtq.check_status(task_id)

