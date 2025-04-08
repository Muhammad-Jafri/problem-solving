from kafka import KafkaProducer, KafkaConsumer
import json
from typing import Dict, Any


class KafkaHandler:
    def __init__(self, bootstrap_servers: str = "0.0.0.0:9092"):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )

    async def produce_message(self, topic: str, message: Dict[str, Any]) -> None:
        # Kafka producer doesn't have async methods, but we can make our interface async
        # to maintain consistency with the rest of the application
        self.producer.send(topic, message)
        self.producer.flush()
        # Optional: Add producer.flush() for immediate delivery

    def get_consumer(self, topic: str, group_id: str = "expression_group"):
        return KafkaConsumer(
            topic,
            bootstrap_servers="0.0.0.0:9092",
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        )
