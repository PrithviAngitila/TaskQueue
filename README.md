Run the following commands to start celery
redis-server
celery -A tasks worker -n simple_worker --loglevel=info
celery -A tasks flower --port=5050