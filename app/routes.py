from flask import jsonify, Response, Flask

from .handlers import EventHandler
from .logger import logger


def register_routes(app: Flask, data_file: str):

    @app.route('/events/countByEventType', methods=['GET'])
    def get_event_count() -> Response:
        logger.debug("Fetching event count by type.")
        return jsonify(EventHandler.get_count_by_event_type(data_file))

    @app.route('/events/countWords', methods=['GET'])
    def get_word_count() -> Response:
        logger.debug("Fetching word count.")
        return jsonify(EventHandler.get_count_words(data_file))
