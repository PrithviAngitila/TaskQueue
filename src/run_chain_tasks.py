from celery import chain
from celery.result import AsyncResult
from celery_app import app
from tasks import add_numbers, multiply_result
import logging
import random
import time

logger = logging.getLogger(__name__)

def run_chain_tasks(n=10):
    # List to store AsyncResult objects
    task_results = []

    # Chain tasks to trigger them
    for task_id in range(1, n + 1):
        result = chain(
            add_numbers.s(task_id, random.randint(1, 10), random.randint(1, 10)) |
            multiply_result.s(task_id, z=random.randint(1, 10))
        )()

        task_results.append(result)

    return task_results

def display_completed_results(task_results):
    # Check the status of each task periodically and display completed results
    while any(result.state in ['PENDING', 'STARTED'] for result in task_results):
        completed_results = []

        for task_id, result in enumerate(task_results, start=1):
            if result.ready():
                task_status = result.status
                task_result = result.result
                logger.info(f"Task {task_id} Status: {task_status}")
                logger.info(f"Task {task_id} Result: {task_result}")
                completed_results.append(result)

        # Remove completed tasks from the list
        for completed_result in completed_results:
            task_results.remove(completed_result)

        # Sleep for a short duration before checking again
        time.sleep(2)

if __name__ == "__main__":
    task_results = run_chain_tasks()
    display_completed_results(task_results)
