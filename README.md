# YADTQ

## client (producer)

create tasks → send to client side support

- create task (using cli)
- query task using task ID
- will include yadtq API which has various functions

## broker (kafka)

- create/update task queue
- is the connector between client and workers
- client sends info here

## worker

fetch task, return result → send to worker side support

1. robust logic for assigning tasks to workers
2. equal distribution
3. fault tolerance
4. tasks executed exactly once
5. worker fails, task incomplete → submit for reprocessing
6. update status of task in result backend
7. send periodic heartbeat to yatdq server
8. logging

- executes task based on task type

## logging

status, heartbeat updates of workers

- connection status
- task events (task receipt, task initiation, success, and failure)
- worker events (worker connections, disconnections, failures)

## result backend

database/in-memory store for result updation

### install redis

https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/linux/

```bash
sudo apt-get install lsb-release curl gpg
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
sudo chmod 644 /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
sudo apt-get update
sudo apt-get install redis-stack-server

# run these commands to start redis
sudo systemctl enable redis-stack-server
sudo systemctl start redis-stack-server
```

## client side support

1. create unique id for each task client sends
2. id stored in result backend with status <queued>
3. client query task status → check result backend, retrieve status
4. store result of task on success in result backend

## dataset structure (tentative) (tasks given by client)

```python
{
	"task-id": "d5750c0e-ed82",
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
