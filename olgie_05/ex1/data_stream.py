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
        elif isinstance(data, list):
            return all(isinstance(element, (float, int)) for element in data)
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if isinstance(data, (float, int)):
            self._storage.append(str(data))
            self._rank.append(len(self._rank))
            self.total_processed += 1
        elif isinstance(data, list):
            for element in data:
                if isinstance(element, (float, int)):
                    self._storage.append(str(element))
                    self._rank.append(len(self._rank))
                    self.total_processed += 1
                else:
                    raise ValueError("Improper numeric data")
        else:
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
        log_keys = {"log_level", "log_message"}

        if type(data) is dict:
            if set(data.keys()) != log_keys:
                return False
            return all(type(v) is str for v in data.values())

        elif type(data) is list:
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


class DataStream:
    def __init__(self) -> None:
        self.processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: List[Any]) -> None:
        for element in stream:
            is_handled = False

            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    is_handled = True
                    break

            if not is_handled:
                print(f"DataStream error - Can't "
                      f"process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream Statistics ==")

        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(
                f"{name}: total {proc.total_processed} items processed, "
                f"remaining {len(proc._storage)} on processor"
            )


def main() -> None:
    data = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]

    d_stream = DataStream()

    print("Registering Numeric Processor\n")
    d_stream.register_processor(NumericProcessor())

    print(f"Send first batch of data on stream: {data}")

    d_stream.process_stream(data)
    d_stream.print_processors_stats()

    print("\nRegistering other data processors")
    d_stream.register_processor(TextProcessor())
    d_stream.register_processor(LogProcessor())

    print("Send the same batch again")

    d_stream.process_stream(data)
    d_stream.print_processors_stats()

    print("\nConsume some elements from the data processor:"
          " Numeric 3, Text 2, Log 1")
    for proc in d_stream.processors:
        if isinstance(proc, NumericProcessor):
            for _ in range(3):
                proc.output()
        elif isinstance(proc, TextProcessor):
            for _ in range(2):
                proc.output()
        elif isinstance(proc, LogProcessor):
            for _ in range(1):
                proc.output()

    d_stream.print_processors_stats()


if __name__ == "__main__":
    main()
