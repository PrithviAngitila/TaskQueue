import logging
import time
from celery_app import app

logger = logging.getLogger(__name__)

@app.task(bind=True, name='add_numbers')
def add_numbers(self, task_id, x, y):
    try:
        logger.info(f"Task {task_id} started. Adding numbers: {x} + {y}")

        # Simulate some processing
        time.sleep(3)

        result = x + y
        logger.info(f"Task {task_id} completed. Result: {result}")
        return result
    except Exception as e:
        logger.error(f"Task {task_id} failed with exception: {e}")
        raise

@app.task(bind=True, name = 'multiply')
def multiply_result(self, task_id, result, z):
    try:
        logger.info(f"Task {task_id} started. Multiplying result {result} by {z}")

        # Simulate some processing
        time.sleep(3)

        final_result = result * z
        logger.info(f"Task {task_id} completed. Final result: {final_result}")
        return final_result
    except Exception as e:
        logger.error(f"Task {task_id} failed with exception: {e}")
        raise
