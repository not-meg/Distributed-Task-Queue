# YADTQ

## client

- can be many clients
- uses APIs to create tasks
- can query the status and result of a task
- is the ![producer](https://img.shields.io/badge/producer-green?style=flat-square&color=228b22) for sending tasks
<br> <br>

![Task Topic](https://img.shields.io/badge/task%20topic-green?style=flat-square&color=228b22)

- create a topic called 'TASKS'
- task scheduler subscribes to 'TASKS'

## task scheduler

- schedules the tasks to the workers
- is the ![consumer](https://img.shields.io/badge/consumer-green?style=flat-square&color=228b22) for receiving tasks from the clients
- needs a table for (task_id, worker_id) pair
- must keep track of which worker doing which task, as well as a count of how many current tasks and pending tasks for each worker (worker load)
- is the ![producer](https://img.shields.io/badge/producer-orange?style=flat-square&color=f25e35) for assigning tasks to workers.
<br> <br>


![Worker Topic](https://img.shields.io/badge/worker%20topic-orange?style=flat-square&color=f25e35)

- create topics 'W1' 'W2' … 'Wn'
- worker1 subscribes to 'W1', worker2 subscribes to 'W2' etc.

## worker

- works on the tasks assigned to it by the task scheduler
- is the ![consumer](https://img.shields.io/badge/consumer-orange?style=flat-square&color=f25e35) for the assigned tasks
- stores the result of the task in the result backend (redis)
- sends periodic heartbeat to task scheduler
- sends status of the task to task scheduler (on completion, task scheduler must delete entry from worker load table) → can be done by being producer of topic called <status> and sending to task scheduler

## dataset structure (tentative) (tasks given by client)

```json
{
	"task-id":"d5750c0e-ed82",
	"task":"add",
	"args":[1,2]
}
```

## structure of result backend data (tentative)

```json
{
	"<unique-task-id>": 
	{
		"status":"success",
		"result":"3"
	}
}
```
