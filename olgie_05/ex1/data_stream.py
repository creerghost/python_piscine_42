from abc import ABC, abstractmethod
from typing import Any, List


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
                self.total_processed += 1
            elif type(data) is list:
                for num in data:
                    int(num)
                    self._storage.append(str(num))
                    self._rank.append(len(self._rank))
                    self.total_processed += 1
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
                self.total_processed += 1
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
                self.total_processed += 1

        else:
            raise AttributeError


class DataStream:
    def __init__(self) -> None:
        self.processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: List[Any]) -> None:
        for element in stream:
            is_handled: bool = False
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    is_handled = True
                    break
            if not is_handled:
                print(f"DataStream error - "
                      f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream Statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            total = proc.total_processed
            remaining = len(proc._storage)
            name = name = proc.__class__.__name__.replace("Processor",
                                                          " Processor")
            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")


def main() -> None:
    data = ['Hello world', [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
              'log_message': 'Telnet access! Use ssh instead'},
             {'log_level': 'INFO',
              'log_message': 'User wil is connected'}], 42,
            ['Hi', 'five']]
    d_stream = DataStream()
    d_stream.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    d_stream.register_processor(NumericProcessor())
    print(f"Send first batch of data on stream: {data}")
    try:
        d_stream.process_stream(data)
        d_stream.print_processors_stats()
    except Exception as e:
        print(e)

    print("Registering other data processors")
    d_stream.register_processor(TextProcessor())
    d_stream.register_processor(LogProcessor())
    print("Send the same batch again")
    try:
        d_stream.process_stream(data)
        d_stream.print_processors_stats()
    except Exception as e:
        print(e)

    print("\nConsume some elements from the data processors: Numeric 3,"
          " Text 2, Log 1")
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
