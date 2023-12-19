Run the following commands to start celery application \n
redis-server \n
celery -A tasks worker -n simple_worker --loglevel=info \n
celery -A tasks flower --port=5050 \n
finally simulae the tasks by running python run_chain_tasks.py