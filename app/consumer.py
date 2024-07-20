import json
import sys


class Consumer:
    def __init__(self, data_file_path: str, persistent: bool = True):
        self.event_count = {}
        self.word_count = {}
        self.data_file = data_file_path
        self.persistent = persistent

    def process_event(self, event_str: str) -> None:
        # Process the event. Update the event count and word count and write to a file if persistent is True
        # If the event is not a valid JSON, ignore it
        try:
            event = json.loads(event_str)
            # Update event count
            event_type = event.get("event_type")
            if event_type:
                if event_type in self.event_count:
                    self.event_count[event_type] += 1
                else:
                    self.event_count[event_type] = 1

            # Update word count
            word = event.get("data")
            if word:
                if word in self.word_count:
                    self.word_count[word] += 1
                else:
                    self.word_count[word] = 1
            if self.persistent:
                # Write the data to a file
                json_to_write = {"statistics": {"event_count": self.event_count, "word_count": self.word_count}}
                with open(self.data_file, 'w') as f:
                    json.dump(json_to_write, f)

        except json.JSONDecodeError:
            # Handle corrupted JSON
            pass

    def start(self) -> None:
        for line in sys.stdin:
            self.process_event(line.strip())


if __name__ == "__main__":
    # get the datafile from the command line arguments
    if len(sys.argv) > 1:
        data_file = sys.argv[1]
    else:
        data_file = 'data.json'
    consumer = Consumer(data_file)
    consumer.start()
