from flask import Flask
import subprocess

from .routes import register_routes
from .logger import logger
from .const import DATA_FILE


class ServiceManager:
    def __init__(self):
        self.consumer_process = None
        self.producer_process = None

    def start_consumer(self, data_file: str) -> subprocess.Popen:
        # Start the consumer process and create a stdin pipe to write to it
        consumer_process = subprocess.Popen(['python', 'app/consumer.py', data_file],
                                            stdin=subprocess.PIPE)
        logger.info("Started consumer process.")
        return consumer_process

    def start_producer(self, consumer_process: subprocess.Popen) -> subprocess.Popen:
        # Start the producer process and get its stdout to write to the consumer process stdin
        producer_process = subprocess.Popen(['python', 'producer.py'],
                                            stdout=consumer_process.stdin)
        logger.info("Started producer process.")
        return producer_process


def create_app(start_consumer_producer_processes: bool = True) -> Flask:
    app = Flask(__name__)

    # Register routes
    register_routes(app, DATA_FILE)

    if start_consumer_producer_processes:
        manager = ServiceManager()
        consumer_process = manager.start_consumer(DATA_FILE)
        manager.start_producer(consumer_process)

    logger.info("Application started.")
    return app
