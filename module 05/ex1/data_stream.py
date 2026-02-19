from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self._processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:

        if criteria is None:
            return data_batch

        return [item for item in data_batch
                if criteria.lower() in str(item).lower()]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed_items": self._processed_count
        }


class SensorStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:

        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Environmental Data")
        print(f"Processing sensor batch: {data_batch}")

        try:
            temps = [
                float(item.split(":")[1])
                for item in data_batch
                if isinstance(item, str) and "temp" in item
            ]

            self._processed_count = len(data_batch)

            avg_temp = sum(temps) / len(temps) if temps else 0

            print(f"Sensor analysis: {len(data_batch)} readings processed, "
                  f"avg temp: {avg_temp}°C")

            return (f"Sensor analysis: {len(data_batch)} readings processed, "
                    f"avg temp: {avg_temp}°C")

        except Exception:
            return "Sensor processing failed"


class TransactionStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Financial Data")
        print(f"Processing transaction batch: {data_batch}")

        try:
            bought = 0
            sold = 0
            for item in data_batch:
                if isinstance(item, str) and ":" in item:
                    action, value = item.split(":")
                    bought += int(value) if action == "buy" else 0
                    sold += int(value) if action == "sell" else 0

            self._processed_count = len(data_batch)

            net_flow = bought - sold

            sign = "+" if net_flow >= 0 else ""

            print(f"Transaction analysis: {len(data_batch)} operations, "
                  f"net flow: {sign}{net_flow} units")

            return (f"Transaction analysis: {len(data_batch)} operations, "
                    f"net flow: {sign}{net_flow} units")

        except Exception:
            return "Transaction processing failed"


class EventStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: System Events")
        print(f"Processing event batch: {data_batch}")

        try:
            errors = [
                event for event in data_batch
                if isinstance(event, str) and "error" in event.lower()
            ]

            self._processed_count = len(data_batch)

            print(f"Event analysis: {len(data_batch)} events,"
                  f" {len(errors)} error detected")

            return (f"Event analysis: {len(data_batch)} events,"
                    f" {len(errors)} error detected")

        except Exception:
            return "Event processing failed"


class StreamProcessor:

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")

        for stream, batch in zip(self.streams, batches):
            result = stream.process_batch(batch)
            print(result)

        print("\nAll streams processed successfully. Nexus throughput optimal.")


sensor = SensorStream("SENSOR_001")
sensor.process_batch(["temp:22.5", "humidity:65", "pressure:1013"])

print()
transaction = TransactionStream("TRANS_001")
transaction.process_batch(["buy:100", "sell:150", "buy:75"])

print()
event = EventStream(" EVENT_001")
event.process_batch(["login", "error", "logout"])
