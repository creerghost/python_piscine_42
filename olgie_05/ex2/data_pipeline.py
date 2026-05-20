from abc import ABC, abstractmethod
from typing import Any, List, Protocol, Tuple


class ExportPlugin(Protocol):
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        ...


class CSVPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        res = []
        for d in data:
            res.append(d[1])
        res_str = ",".join(res)
        print(f"CSV Output:\n{res_str}")


class JSONPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        items = []
        for rank, value in data:
            key = f"item_{rank}"
            items.append(f'"{key}": "{value}"')
        json = "{" + ", ".join(items) + "}"
        print(f"JSON Output:\n{json}")


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
        return (self._rank.pop(0), self._storage.pop(0))


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")

        values = [data] if isinstance(data, (int, float)) else data

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
        if not self.validate(data):
            raise TypeError("Invalid text data")

        values = [data] if type(data) is str else data

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


class DataStream:
    def __init__(self) -> None:
        self.processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: List[Any]) -> None:
        for element in stream:
            handled = False

            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break

            if not handled:
                print(f"DataStream error - Can't process element: {element}")

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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            outputs = []

            for _ in range(nb):
                try:
                    outputs.append(proc.output())
                except IndexError:
                    break

            if outputs:
                plugin.process_output(outputs)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initializing Data Stream...")

    data = ['Hello world', [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
              'log_message': 'Telnet access! Use ssh instead'},
             {'log_level': 'INFO',
              'log_message': 'User wil is connected'}], 42,
            ['Hi', 'five']]

    d_stream = DataStream()

    d_stream.print_processors_stats()

    print("\nRegistering Processors\n")

    d_stream.register_processor(NumericProcessor())
    d_stream.register_processor(TextProcessor())
    d_stream.register_processor(LogProcessor())

    print(f"Send first batch of data on stream: {data}\n")

    try:
        d_stream.process_stream(data)
        d_stream.print_processors_stats()
    except Exception as e:
        print(e)

    print("Send 3 processed data from each processor to a CSV plugin:")

    d_stream.output_pipeline(3, CSVPlugin())

    data_2 = [21,
              ['I love AI',
               'LLMs are wonderful',
               'Stay healthy'],
              [{'log_level': 'ERROR',
                'log_message': '500 server crash'},
               {'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'}],
              [32, 42, 64, 84, 128, 168], 'World hello']

    try:
        d_stream.process_stream(data_2)
        d_stream.print_processors_stats()
    except Exception as e:
        print(e)

    print("Send 5 processed data from each processor to a JSON plugin:")

    d_stream.output_pipeline(5, JSONPlugin())
    d_stream.print_processors_stats()

if __name__ == "__main__":
    main()