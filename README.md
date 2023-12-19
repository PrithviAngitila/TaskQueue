Run the following commands to start celery application <br>
redis-server <br>
celery -A tasks worker -n simple_worker --loglevel=info <br>
celery -A tasks flower --port=5050 <br>
finally simulae the tasks by running python run_chain_tasks.py 