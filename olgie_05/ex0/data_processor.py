from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[str] = []
        self._rank: List[int] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        storage_res = self._storage.pop(0)
        rank_res = self._rank.pop(0)
        return (rank_res, storage_res)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            if type(data) is int or type(data) is float \
                    or type(data) is str:
                int(data)
            elif type(data) is list:
                [int(num) for num in data]
            else:
                raise ValueError
            return True
        except ValueError:
            return False
        except TypeError:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        try:
            if type(data) is int or type(data) is float \
                    or type(data) is str:
                int(data)
                self._storage.append(str(data))
                self._rank.append(len(self._rank))
            elif type(data) is list:
                for num in data:
                    int(num)
                    self._storage.append(str(num))
                    self._rank.append(len(self._rank))
            else:
                print("hi")
        except ValueError:
            raise ValueError("Improper numeric data")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is str:
            return True
        if type(data) is list and all(type(s) is str for s in data):
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if type(data) is str:
            self._storage.append(data)
            self._rank.append(len(self._rank))
            self.total_processed += 1
        elif type(data) is list and all(type(s) is str for s in data):
            for s in data:
                self._storage.append(s)
                self._rank.append(len(self._rank))
                self.total_processed += 1
        else:
            raise TypeError("Improper text data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            log_keys = ["log_level", "log_message"]
            if type(data) is dict:
                key, val = zip(*data.items())
                # key = data.keys()
                # val = data.values()
                if [k for k in key if k not in log_keys]:
                    raise AttributeError
                if [v for v in val if type(v) is not str]:
                    raise AttributeError
                return True
            elif type(data) is list:
                for d in data:
                    key, val = zip(*d.items())
                    if [k for k in key if k not in log_keys]:
                        raise AttributeError
                    if [v for v in val if type(v) is not str]:
                        raise AttributeError
                    return True
            else:
                return False
        except AttributeError:
            return False

    def ingest(
        self,
        data: dict[str, str] | list[dict[str, str]],
    ) -> None:
        log_keys = ["log_level", "log_message"]
        if type(data) is dict:
            key, val = zip(*data.items())
            # key = data.keys()
            # val = data.values()
            if [k for k in key if k not in log_keys]:
                raise AttributeError
            if [v for v in val if type(v) is not str]:
                raise AttributeError
            for v in val:
                self._storage.append(v)
                self._rank.append(len(self._rank))
        elif type(data) is list:
            val_list = []
            for d in data:
                key, val = zip(*d.items())
                if [k for k in key if k not in log_keys]:
                    raise AttributeError
                if [v for v in val if type(v) is not str]:
                    raise AttributeError
                val_list.append(val)

            for v in val_list:
                self._storage.append(": ".join(v))
                self._rank.append(len(self._rank))

        else:
            raise AttributeError


def main() -> None:
    print("=== Code Nexus- Data Processor ===\n")

    numeric = NumericProcessor()
    print("Testing Numeric processor...")
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate("Hello")}")
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
    print(f"Trying to validate input 'Hello': {log.validate("Hello")}")
    data_dict: list[dict[str, str]] = [{'log_level': 'NOTICE',
                                        'log_message': 'Connection to server'},
                                       {'log_level': 'ERROR',
                                        'log_message':
                                        'Unauthorized access!!'}]
    print(f"Processing data: {data_dict}")
    print("Extracting 2 values...")
    log.ingest(data_dict)
    for _ in range(2):
        res = log.output()
        print(f"Log entry {res[0]}: {res[1]}")


if __name__ == "__main__":
    main()
