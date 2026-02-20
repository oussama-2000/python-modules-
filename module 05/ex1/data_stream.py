from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0
        self.show = True

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
            "processed_items": self.processed_count
        }


class SensorStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        if self.show:
            print("Initializing Sensor Stream...")
            print(f"Stream ID: {self.stream_id}, Type: Environmental Data")
            print(f"Processing sensor batch: {data_batch}")
        if not isinstance(data_batch, list):
            print("Error: Invalid data batch")
            return "invalid"

        try:
            for i in data_batch:
                if len(i.split(":")) != 2:
                    raise ValueError
                name, value = i.split(":")
                if not name or not value:
                    raise ValueError
                if name.isspace() or value.isspace():
                    raise ValueError

            temps = [
                float(item.split(":")[1])
                for item in data_batch
                if isinstance(item, str) and "temp" in item
            ]

            self.processed_count = len(data_batch)

            avg_temp = sum(temps) / len(temps) if temps else 0
            if self.show:
                print(f"Sensor analysis: {len(data_batch)} readings processed,"
                      f" avg temp: {avg_temp}°C")

            return (f"Sensor analysis: {len(data_batch)} readings processed, "
                    f"avg temp: {avg_temp}°C")

        except Exception:
            print("Error: Sensor processing failed")
            return "invalid"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "type": "Sensor",
            "processed": f"{self.processed_count} readings processed"
        }


class TransactionStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        if self.show:
            print("Initializing Transaction Stream...")
            print(f"Stream ID: {self.stream_id}, Type: Financial Data")
            print(f"Processing transaction batch: {data_batch}")
        if not isinstance(data_batch, list):
            print("Error: Invalid data batch")
            return "invalid"

        try:
            for i in data_batch:
                if len(i.split(":")) != 2:
                    raise ValueError
                name, value = i.split(":")
                if not name or not value:
                    raise ValueError
                if name.isspace() or value.isspace():
                    raise ValueError
            bought = 0
            sold = 0
            for item in data_batch:
                if isinstance(item, str) and ":" in item:
                    action, value = item.split(":")
                    bought += int(value) if action == "buy" else 0
                    sold += int(value) if action == "sell" else 0

            self.processed_count = len(data_batch)

            net_flow = bought - sold

            sign = "+" if net_flow >= 0 else ""
            if self.show:
                print(f"Transaction analysis: {len(data_batch)} operations, "
                      f"net flow: {sign}{net_flow} units")

            return (f"Transaction analysis: {len(data_batch)} operations, "
                    f"net flow: {sign}{net_flow} units")

        except Exception:
            print("Error: Transaction processing failed")
            return "invalid"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "type": "Transaction",
            "processed": f"{self.processed_count} operations processed"
        }


class EventStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        if self.show:
            print("Initializing Event Stream...")
            print(f"Stream ID: {self.stream_id}, Type: System Events")
            print(f"Processing event batch: {data_batch}")
        if not isinstance(data_batch, list):
            print("Error: Invalid data batch")
            return "invalid"

        try:
            for event in data_batch:
                if not isinstance(event, str):
                    raise ValueError
                if not event or event.isspace():
                    raise ValueError
            errors = [
                event for event in data_batch
                if isinstance(event, str) and "error" in event.lower()
            ]

            self.processed_count = len(data_batch)
            if self.show:
                print(f"Event analysis: {len(data_batch)} events,"
                      f" {len(errors)} error detected")

            return (f"Event analysis: {len(data_batch)} events,"
                    f" {len(errors)} error detected")

        except Exception:
            print("Error: Event processing failed")
            return "invalid"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "type": "Event",
            "processed": f"{self.processed_count} events processed"
        }


class StreamProcessor:

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        print("Processing mixed stream types through unified interface...\n")

        print("Batch 1 Results:")
        for stream, batch in zip(self.streams, batches):
            stream.show = False
            validation = stream.process_batch(batch)
            if validation == "invalid":
                print("Error: cannot process invalid data")
                continue
            stats = stream.get_stats()
            print(f"- {stats['type']} data: {stats['processed']}")
        try:
            print("\nStream filtering active: High-priority data only")
            filtered_sensor = self.streams[0].filter_data(
                batches[0], "temp"
            )
            filtered_transaction = self.streams[1].filter_data(
                batches[1], "buy"
            )

            print(
                f"Filtered results: "
                f"{len(filtered_sensor)} critical sensor alerts, "
                f"{len(filtered_transaction)} large transaction"
            )
        except TypeError:
            print("Error: filtering failed")
            return

        print("\nAll streams processed successfully. "
              "Nexus throughput optimal.")


if __name__ == "__main__":

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor = SensorStream("SENSOR_001")
    sensor.process_batch(["temp:22.5", "humidity:65", "pressure:1013"])

    print()
    transaction = TransactionStream("TRANS_001")
    transaction.process_batch(["buy:100", "sell:150", "buy:75"])

    print()
    event = EventStream("EVENT_001")
    event.process_batch(["login", "error", "logout"])

    print("\n=== Polymorphic Stream Processing ===")

    processor = StreamProcessor()

    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    batches = [
        ["temp:25", "temp:1"],
        ["buy:100", "sell:150", "sell:10", "sell:40"],
        ["login", "error", "logout"]
    ]

    processor.process_all(batches)
