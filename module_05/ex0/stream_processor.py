from typing import Any, List, Dict, Optional, Union
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    metadata: Optional[Dict[str, Any]] = None

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            _ = data + []
            for x in data:
                _ = x + 0.0
                return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Data must be a list of numbers.")
            total: Union[int, float] = 0
            count: int = 0
            for x in data:
                total += x
                count += 1
            avg: float = total / count if count else 0.0
            result: str = f"Processed {count} numeric values, sum={
                total}, avg={avg}"
            return self.format_output(result)
        except Exception as e:
            return self.format_output(f"Error processing numeric data: {e}")


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            _ = data + ""
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Data must be a string type.")
            chars: int = 0
            for _ in data:
                chars += 1
            words: int = 0
            for _ in data.split():
                words += 1
            result: str = f"Processed text: {chars} characters, {words} words"
            return self.format_output(result)
        except Exception as e:
            return self.format_output(f"Error processing text data: {e}")


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            _ = data + ""
            return ":" in data
        except Exception:
            return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Data must be a valid log string"
                                 "containing a colon.")
            parts: List[str] = data.split(":", 1)
            level: str = parts[0].strip().upper()
            msg: str = parts[1].strip()
            tag: str = "ALERT" if level == "ERROR" else level
            result: str = f"[{tag}] {level} level detected: {msg}"
            return self.format_output(result)
        except Exception as e:
            return self.format_output(f"Error processing log data: {e}")


def stream_processor() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    num_data: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    num_proc = NumericProcessor()
    if num_proc.validate(num_data):
        print("Validation: Numeric data verified")
    print(f"Output: {num_proc.process(num_data)}")

    print("Initializing Text Processor...\n")
    text_data: str = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')
    text_proc = TextProcessor()
    if text_proc.validate(text_data):
        print("Validation: Text data verified")
    print(f"Output: {text_proc.process(text_data)}")

    print("Initializing Log Processor...\n")
    log_data: str = "ERROR: Connection timeout"
    print(f'Processing data: "{log_data}"')
    log_proc = LogProcessor()
    if log_proc.validate(log_data):
        print("Validation: Log entry verified")
    print(f"Output: {log_proc.process(log_data)}")

    print("\n=== Polymorphic Processing Demo ===")

    print("Processing multiple data types through same interface...")
    processors: List[DataProcessor] = [NumericProcessor(),
                                       TextProcessor(), LogProcessor()]
    demo_data: List[Any] = [[1, 2, 3], "Nexus Stream", "INFO: System ready"]
    for i, (proc, data) in enumerate(zip(processors, demo_data), 1):
        print(f"Result {i}: {proc.process(data)}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    stream_processor()
