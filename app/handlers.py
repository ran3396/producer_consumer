import json
from .logger import logger


class EventHandler:

    @staticmethod
    def get_count_by_event_type(data_file: str) -> dict:
        # Get the event count by type from the data file
        try:
            with open(data_file, 'r') as f:
                data = json.load(f)
                return data.get("statistics", {}).get("event_count", {})
        except (json.JSONDecodeError, FileNotFoundError, KeyError, TypeError):
            logger.error(f"Error getting event count by type from file {data_file}")
            return {}

    @staticmethod
    def get_count_words(data_file: str) -> dict:
        # Get the word count from the data file
        try:
            with open(data_file, 'r') as f:
                data = json.load(f)
                return data.get("statistics", {}).get("word_count", {})
        except (json.JSONDecodeError, FileNotFoundError, KeyError, TypeError):
            logger.error(f"Error getting word count from file {data_file}")
            return {}
