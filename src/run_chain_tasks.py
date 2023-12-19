from celery import chain
from celery.exceptions import ChordError
from celery_app import app
from tasks import add_numbers, multiply_result
import logging
import time
import random

logger = logging.getLogger(__name__)

def run_chain_tasks(n=10):
    # Result accumulator
    final_result = 0

    # Chain tasks sequentially
    try:
        for task_id in range(1, n + 1):
            result = chain(
                add_numbers.s(task_id, random.randint(1, 10), random.randint(1, 10)) |
                multiply_result.s(task_id, z=random.randint(1, 10))
            )()

            # Wait for the result
            final_result += result.get()
            logger.info(f"Task {task_id} Final Result: {final_result}")

    except ChordError as e:
        logger.error(f"Error in chain: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

    # Print the overall final result
    logger.info(f"Overall Final Result (Sum of Individual Results): {final_result}")

if __name__ == "__main__":
    run_chain_tasks()
