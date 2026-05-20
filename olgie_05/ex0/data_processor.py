from abc import ABC, abstractmethod
from typing import Any, List, Tuple


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[str] = []
        self._rank: List[int] = []
        self.total_processed = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> Tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available")
        storage_res = self._storage.pop(0)
        rank_res = self._rank.pop(0)
        return (rank_res, storage_res)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (float, int)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (float, int)) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if isinstance(data, (float, int)):
            values = [data]
        elif isinstance(data, list):
            if not all(isinstance(x, (float, int)) for x in data):
                raise ValueError("Invalid numeric data")
            values = data
        else:
            raise ValueError("Invalid numeric data")

        for v in values:
            self._storage.append(str(v))
            self._rank.append(len(self._rank))
            self.total_processed += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is str:
            return True
        if type(data) is list and all(type(x) is str for x in data):
            return True
        return False

    def ingest(self, data: Any) -> None:
        if type(data) is str:
            values = [data]
        elif type(data) is list:
            if not all(type(x) is str for x in data):
                raise TypeError("Invalid text data")
            values = data
        else:
            raise TypeError("Invalid text data")

        for v in values:
            self._storage.append(v)
            self._rank.append(len(self._rank))
            self.total_processed += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        log_keys = {"log_level", "log_message"}

        if type(data) is dict:
            if set(data.keys()) != log_keys:
                return False
            return all(type(v) is str for v in data.values())

        if type(data) is list:
            for d in data:
                if set(d.keys()) != log_keys:
                    return False
                if not all(type(v) is str for v in d.values()):
                    return False
            return True

        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Invalid log data")

        if type(data) is dict:
            for v in data.values():
                self._storage.append(v)
                self._rank.append(len(self._rank))
                self.total_processed += 1

        elif type(data) is list:
            for d in data:
                self._storage.append(": ".join(d.values()))
                self._rank.append(len(self._rank))
                self.total_processed += 1

        else:
            raise ValueError("Invalid log data")


def main() -> None:
    print("=== Code Nexus- Data Processor ===\n")

    numeric = NumericProcessor()
    print("Testing Numeric processor...")
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without"
          " prior validation:")
    try:
        numeric.ingest("a")
    except ValueError as e:
        print(f"Got exception: {e}")
    data_num: list[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_num}")
    print("Extracting 3 values...")
    numeric.ingest(data_num)
    for _ in range(3):
        res = numeric.output()
        print(f"Numeric value {res[0]}: {res[1]}")

    text = TextProcessor()
    print("\nTesting Text Processor...")
    print(f"Trying to validate input '42': {text.validate(42)}")
    data_str: list[str] = ["Hello", "Nexus", "World"]
    print(f"Processing data: {data_str}")
    print("Extracting 1 value...")
    text.ingest(data_str)
    res = text.output()
    print(f"Text output {res[0]}: {res[1]}")

    log = LogProcessor()
    print("\nTesting Log Processor...")
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    data_dict: list[dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {data_dict}")
    print("Extracting 2 values...")
    log.ingest(data_dict)
    for _ in range(2):
        res = log.output()
        print(f"Log entry {res[0]}: {res[1]}")


if __name__ == "__main__":
    main()