from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Tuple


class DataStream(ABC):
    def __init__(self, str_id: str) -> None:
        self.str_id = str_id
        self.count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria:
            return [val for val in data_batch if criteria in str(val)]
        return [val for val in data_batch if val is not None]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.str_id,
            "count": self.count
        }


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.str_id}, Type: Environmental Data")
        print(f"Processing sensor batch: {data_batch}")
        temps: List[Union[float, int]] = []
        humidities: List[Union[float, int]] = []
        pressures: List[Union[float, int]] = []
        readings_count: int = 0
        for data in data_batch:
            try:
                if isinstance(data, dict):
                    self.count += 1
                    readings_count += 1
                    if 'temperature' in data and isinstance(
                            data['temperature'], (int, float)):
                        temps.append(data['temperature'])
                    if 'humidity' in data and isinstance(
                            data['humidity'], (int, float)):
                        humidities.append(data['humidity'])
                    if 'pressure' in data and isinstance(
                            data['pressure'], (int, float)):
                        pressures.append(data['pressure'])
            except Exception:
                print("\nError: something went wrong")
        temp_str: str = f", avg temperature: {
                    sum(temps) / len(temps)} °C" if temps else ""
        hum_str: str = f", avg humidity: {
                    sum(humidities) / len(humidities)} %" if humidities else ""

        pres_str: str = f", avg pressure: {
                    sum(pressures) / len(pressures)} hPa" if pressures else ""

        return f"Sensor analysis: {
                    readings_count} readings processed{
                    temp_str}{hum_str}{pres_str}"


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.str_id}, Type: Financial Data")
        print(f"Processing transaction batch: {data_batch}")
        transaction_count: int = 0
        net_flow: int = 0
        buy: int = 0
        sell: int = 0
        for data in data_batch:
            try:
                if isinstance(data, dict):
                    if 'buy' in data or 'sell' in data:
                        self.count += 1
                        transaction_count += 1
                    if 'buy' in data and isinstance(data['buy'], (int)):
                        buy += data['buy']
                    if 'sell' in data and isinstance(data['sell'], (int)):
                        sell += data['sell']
            except Exception:
                print("Error: something went wrong")
        net_flow = buy - sell
        return f"Transaction analysis: {
                    transaction_count} operations processed, net flow {
                    net_flow:+} units"


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.str_id}, Type: System Events")
        print(f"Processing event batch: {data_batch}")
        errors: int = 0
        events_count: int = 0
        for data in data_batch:
            try:
                if isinstance(data, str):
                    events_count += 1
                    self.count += 1
                    if 'error' in data.lower():
                        errors += 1
            except Exception:
                print("Error: something went wrong")
        return f"Event analysis: {events_count} events processed, {
                errors} errors detected"


class StreamProcessor():
    def __init__(self):
        self.streams: List[DataStream] = []
        self.count: int = 0

    def add_stream(self, stream: DataStream):
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]):
        print("Processing mixed stream types through unified interface...\n")
        self.count += 1
        print(f"Batch {self.count} Results:")
        for i, stream in enumerate(self.streams):
            if i < len(batches):
                try:
                    if isinstance(stream, SensorStream):
                        print(f"- Sensor data: {
                            len(batches[i])} readings processed")
                    elif isinstance(stream, TransactionStream):
                        print(f"- Transaction data: {
                            len(batches[i])} operations processed")
                    elif isinstance(stream, EventStream):
                        print(f"- Event data: {
                            len(batches[i])} events processed")
                except Exception:
                    print("Stream processing failed")


def data_stream() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    test_sensor_batch: List[Tuple[Any]] = [
        {"date": "2026-03-13 12:00", "temperatuare": 22.5, "humidity": 45.0, "pressure": 1012.5},  # noqa
    {"date": "2026-03-13 12:05", "temperatuare": 23.0, "humidity": 46.2}, # noqa
    {"date": "2026-03-13 12:10", "temperataure": "SENSOR_ERROR", "pressure": 1011.0},  # noqa
    "CONNECTION_LOST_RETRYING...",  # noqa
    {"date": "2026-03-13 12:15", "temperataure": -15.5, "humidity": 80.5, "pressure": 990.0},  # noqa
    {},  # noqa
    {"date": "2026-03-13 12:20", "temperatuare": 24.1, "battery_level": 15, "status": "low_power", "humidity": 40.0}]  # noqa
    sensor = SensorStream("STREAM_123")
    print(sensor.process_batch(test_sensor_batch))
    print()

    test_transaction_batch: List[Dict] = [{"buy": 25}, {"sell": 30}, {"buy": 30}]  # noqa
    transaction = TransactionStream("TRANS_123")
    print(transaction.process_batch(test_transaction_batch))
    print()

    test_event_batch: List[str] = ["login", "error", "logout", "error"]
    event = EventStream("EVENT_123")
    print(event.process_batch(test_event_batch))
    print()

    print("===Polymorphic stream processing ===")
    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)
    batches: List[Any] = [[
        {"date": "2026-03-13 12:00", "temperatuare": 22.5, "humidity": 45.0, "pressure": 1012.5},  # noqa
        {"date": "2026-03-13 12:05", "temperatuare": 23.0, "humidity": 46.2} # noqa
    ], [{"buy": 25}, {"sell": 30}, {"buy": 30}], ["startup", "login", "warning", "error"]]  # noqa
    processor.process_all(batches)

    print("\nSelf filtering active: High-priority data only")
    mixed_data = [
        "normal_log",
        "CRITICAL: core overheating",
        {"amount": 5},
        "CRITICAL: pressure drop",
        {"amount": 10000, "type": "large_transaction"}
    ]
    critical_alerts = sensor.filter_data(mixed_data, criteria="CRITICAL")
    large_transactions = transaction.filter_data(mixed_data, criteria="large")
    print(f"Filtered results: {len(critical_alerts)} critical sensor alerts, {
        len(large_transactions)} large transaction")
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
