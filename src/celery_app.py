from celery import Celery

app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/1',
    include=['tasks']
)

# Configuration, e.g., task result expires after 10 seconds
app.conf.update(
    result_expires=10,
)
