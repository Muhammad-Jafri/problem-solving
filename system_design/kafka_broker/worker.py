# worker.py
import asyncio
import json
import time
from functools import partial
from concurrent.futures import ThreadPoolExecutor
from system_design.kafka_broker.kafka_handler import KafkaHandler
from system_design.kafka_broker.expression_evaluator import evaluate_expression
from system_design.kafka_broker.schemas import Status

# You would need to import your job_statuses somehow
# In a real app, you'd use a shared database instead of in-memory dictionary
from system_design.kafka_broker.db import job_statuses

# Flag to control the worker loop
running = True

# This function will run in a separate thread
def consume_messages(consumer, loop, process_message_callback):
    """Consume messages from Kafka in a separate thread."""
    try:
        for message in consumer:
            if not running:
                break
                
            # Schedule the message processing in the event loop
            asyncio.run_coroutine_threadsafe(
                process_message_callback(message.value), 
                loop
            )
    except Exception as e:
        print(f"Error in consumer thread: {e}")

async def process_message(data):
    """Process a single message from Kafka."""
    job_id = data.get("id")
    expression = data.get("expression")
    
    # Skip if we don't have this job in our dictionary
    if job_id not in job_statuses:
        print(f"Received unknown job ID: {job_id}")
        return
        
    # Update status to IN_PROGRESS
    job_statuses[job_id].status = Status.IN_PROGRESS
    
    try:
        # Evaluate the expression
        result = await evaluate_expression(expression)
        job_statuses[job_id].result = result
        job_statuses[job_id].status = Status.DONE
        print(f"Job {job_id} completed with result: {result}")
    except Exception as e:
        # Handle errors
        error_message = str(e)
        job_statuses[job_id].error = error_message
        job_statuses[job_id].status = Status.FAILED
        print(f"Job {job_id} failed: {error_message}")

async def run_worker():
    """Main worker function that starts the consumer in a background thread."""
    global running
    running = True
    
    # Get the event loop
    loop = asyncio.get_event_loop()
    
    # Initialize Kafka
    kafka_handler = KafkaHandler()
    consumer = kafka_handler.get_consumer("expression_input")
    
    print("Worker started, waiting for messages...")
    
    # Create a thread pool executor
    executor = ThreadPoolExecutor(max_workers=1)
    
    # Submit the consumer task to the executor
    future = executor.submit(
        consume_messages,
        consumer,
        loop,
        process_message
    )
    
    try:
        # Keep the worker running until cancelled
        while running:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Worker received cancel signal")
        running = False
        consumer.close(autocommit=True)
        executor.shutdown(wait=False)
        raise
    finally:
        # Ensure proper cleanup
        running = False
        consumer.close(autocommit=True)
        executor.shutdown(wait=True)
        print("Worker shut down")