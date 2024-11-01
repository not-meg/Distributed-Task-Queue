import argparse
import logging
from client import Client

def main():
    logging.basicConfig(level=logging.INFO)  # Configure logging
    parser = argparse.ArgumentParser(description='YADTQ Client')
    parser.add_argument('--action', choices=['submit', 'check'], required=True, help='Action to perform: submit or check task status')
    parser.add_argument('--task_type', help='Type of task to process (required for submit action)')
    parser.add_argument('--task_data', help='Data for the task (required for submit action)')
    parser.add_argument('--task_id', help='ID of the task to check status (required for check action)')
    
    args = parser.parse_args()
    client = Client()

    if args.action == 'submit':
        if not args.task_type or not args.task_data:
            print("Error: --task_type and --task_data are required for submitting a task.")
            return
        
        task_id = client.submit_task(args.task_type, args.task_data)
        if task_id:
            print(f"Task submitted successfully. Task ID: {task_id}")
        else:
            print("Failed to submit task.")

    elif args.action == 'check':
        if not args.task_id:
            print("Error: --task_id is required for checking task status.")
            return
        
        status = client.check_status(args.task_id)
        print(f"Status of task {args.task_id}: {status}")

if __name__ == "__main__":
    main()

