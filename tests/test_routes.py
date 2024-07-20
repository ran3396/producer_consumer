import unittest
from unittest.mock import patch
from flask import Flask

from app.routes import register_routes


class TestRoutes(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        register_routes(app, 'dummy_data_file.json')
        self.client = app.test_client()
        self.app = app

    @patch('app.handlers.EventHandler.get_count_by_event_type')
    def test_get_event_count(self, mock_get_count_by_event_type):
        mock_get_count_by_event_type.return_value = {"foo": 1, "bar": 2}

        response = self.client.get('/events/countByEventType')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)
        self.assertEqual(response.json, {"foo": 1, "bar": 2})
        mock_get_count_by_event_type.assert_called_once_with('dummy_data_file.json')

    @patch('app.handlers.EventHandler.get_count_words')
    def test_get_word_count(self, mock_get_count_words):
        mock_get_count_words.return_value = {"test": 3, "data": 4}

        response = self.client.get('/events/countWords')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)
        self.assertEqual(response.json, {"test": 3, "data": 4})
        mock_get_count_words.assert_called_once_with('dummy_data_file.json')


if __name__ == '__main__':
    unittest.main()
