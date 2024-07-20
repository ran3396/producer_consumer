import unittest

from app.consumer import Consumer
from app.const import DATA_FILE


class TestConsumer(unittest.TestCase):

    def test_process_event_valid_json(self):
        consumer = Consumer(DATA_FILE, persistent=False)
        valid_event = '{"event_type": "foo", "data": "test", "timestamp": 1629475200}'
        consumer.process_event(valid_event)
        self.assertEqual(consumer.event_count["foo"], 1)
        self.assertEqual(consumer.word_count["test"], 1)

    def test_process_event_invalid_json(self):
        consumer = Consumer(DATA_FILE, persistent=False)
        invalid_event = 'invalid json'
        consumer.process_event(invalid_event)
        self.assertEqual(len(consumer.event_count), 0)
        self.assertEqual(len(consumer.word_count), 0)


if __name__ == '__main__':
    unittest.main()
