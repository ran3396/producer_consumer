# Non-Blocking Producer/Consumer Stream Processing Service

## Requirements
- Python >= 3.6
- Flask

## Setup
1. Install Requirements:
    ```
    pip install -r requirements.txt
    ```

2. Run the application:
    ```
    python run.py
    ```

3. Run the tests:
    ```
    python -m unittest discover tests
    ```

## Endpoints
- `GET /events/countByEventType`
  - Returns a JSON map of event types to their counts.

- `GET /events/countWords`
  - Returns a JSON map of words to their counts.

## Improvements
1. **Scalability**: Use a more robust message queue system like RabbitMQ or Kafka for better scalability and durability.
2. **Security**: Add authentication and authorization mechanisms to secure the service.
3. **Monitoring**: Add monitoring and alerting to track the health of the service.
4. **Containerization**: Use Docker for containerization and Kubernetes for orchestration.
5. **Separation of Concerns**: Separate the producer, consumer and the web service into different services for better maintainability.
6. **Data Storage**: Use a database to store the events and words for better data management.
