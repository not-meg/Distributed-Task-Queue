import time
import random
import yadtq

random.seed(int(time.time()))

# Initialize the YADTQClient
client = yadtq.YADTQClient()

def generate_task():
    task_names = ['add','subtract', 'multiply','divide', 'pow']
    task_name = random.choice(task_names)
    nargs = random.randint(2, 5)
    args = [random.randint(1, 100) + random.random() for _ in range(nargs)]
    return task_name, args

try:
    while True:
        task_ids = []
        num_tasks = 10  # Define how many tasks to generate in each loop

        # Generate and send tasks
        for i in range(num_tasks):
            task_name, args = generate_task()
            task_id = client.send_task(task_name, args)
            task_ids.append(task_id)
            print(f"Sent task {task_id}: {task_name} with args {args}")
            time.sleep(0.5)

        # Sleep for 5 seconds before querying tasks
        time.sleep(5)

        # Query tasks until they are completed
        for task_id in task_ids:
            attempt = 0
            while attempt < 10:  # Limit the number of attempts to avoid infinite loops
                status,task_id,result = client.query_task(task_id)
                if status == 'success':
                    print(f"Task {task_id} completed successfully with result: {result}")
                    break
                elif status == 'failed':
                    print(f"Task {task_id} failed with error: {result}")
                    break
                else:
                    print(f"Task {task_id} still processing. Current status: {status}")
                attempt += 1
                time.sleep(3)  # Sleep for 1 second before querying again

            if attempt == 10:
                print(f"Task {task_id} did not complete in time.")

except KeyboardInterrupt:
    print("Shutting down gracefully...")
finally:
    client.close()
