from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    metadata: Optional[Dict[str, Any]] = None

    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return the result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Provide a default output format that can be overridden if needed."""
        return result


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        return all(isinstance(x, (int, float)) for x in data)

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Data must be a list of numbers.")
            num_list: List[Union[int, float]] = data
            total = sum(num_list)
            avg = total / len(num_list) if num_list else 0.0
            result = f"Processed {len(num_list)} numeric values,"
            f"sum={total}, avg={avg}"
            return self.format_output(result)
        except Exception as e:
            return self.format_output(f"Error processing numeric data: {e}")


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Data must be a string type.")
            chars = len(data)
            words = len(data.split())
            result = f"Processed text: {chars} characters, {words} words"
            return self.format_output(result)
        except Exception as e:
            return self.format_output(f"Error processing text data: {e}")


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Data must be a valid log string"
                                 "containing a colon.")
            level, msg = data.split(":", 1)
            level = level.strip().upper()
            msg = msg.strip()
            tag = "ALERT" if level == "ERROR" else level
            result = f"[{tag}] {level} level detected: {msg}"
            return self.format_output(result)
        except Exception as e:
            return self.format_output(f"Error processing log data: {e}")


def stream_processor() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("Initializing Numeric Processor...")
    num_data: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    num_proc = NumericProcessor()
    if num_proc.validate(num_data):
        print("Validation: Numeric data verified")
    print(f"Output: {num_proc.process(num_data)}")

    print("Initializing Text Processor...")
    text_data: str = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')
    text_proc = TextProcessor()
    if text_proc.validate(text_data):
        print("Validation: Text data verified")
    print(f"Output: {text_proc.process(text_data)}")
    print("Initializing Log Processor...")

    log_data: str = "ERROR: Connection timeout"
    print(f'Processing data: "{log_data}"')
    log_proc = LogProcessor()
    if log_proc.validate(log_data):
        print("Validation: Log entry verified")
    print(f"Output: {log_proc.process(log_data)}")

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors: List[DataProcessor] = [NumericProcessor(),
                                       TextProcessor(), LogProcessor()]
    demo_data: List[Any] = [[1, 2, 3], "Nexus Stream", "INFO: System ready"]
    for i, (proc, data) in enumerate(zip(processors, demo_data), 1):
        print(f"Result {i}: {proc.process(data)}")
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    stream_processor()
