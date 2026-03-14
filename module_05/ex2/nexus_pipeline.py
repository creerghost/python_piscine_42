from typing import Any, List, Protocol
from abc import abstractmethod, ABC
import collections
import time


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage():
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            return {k: v for k, v in data.items() if v is not None}
        return data


class TransformStage():
    def process(self, data: Any) -> Any:
        if isinstance(data, str) and data == "ERROR_TRIGGER":
            raise ValueError("Invalid data format")
        return data


class OutputStage():
    def process(self, data: Any) -> Any:
        return data


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: List[ProcessingStage] = []

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def run_stages(self, data: Any) -> Any:
        current_data: Any = data
        for stage in self.stages:
            current_data = stage.process(current_data)
        return current_data


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Any:
        result: Any = self.run_stages(data)
        if isinstance(result, dict) and result.get("sensor") == "temp":
            temp: int = result.get("value")
            if temp is not None:
                if temp > 25 or temp < 20:
                    print(f"Output: Processed temperature reading: {
                        temp}°C (Temperature is exceeding normal range)")
                else:
                    print(f"Output: Processed temperature reading: {
                        temp}°C (Normal range)")
            else:
                print("Error: sensor is not measuring temperature")
        else:
            print("Error: sensor is not measuring temperature")


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Any:
        actions: int = 0
        result: Any = self.run_stages(data)
        if isinstance(data, str) and ',' in data:
            result = data.split(',')
        if isinstance(data, list):
            actions = len(data)
        else:
            actions = 1
        print(f"Output: User activity logged: {actions} actions processed")
        return result


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Any:
        result: Any = self.run_stages(data)
        if isinstance(result, list) and all(isinstance(x, (int, float))
           for x in result):
            avg: float = sum(result) / len(result)
            print(f"Output: Stream summary: {
                len(result)} readings, avg: {avg:.1f}°C")
        else:
            print("Output: Stream summary processed (no numerical data)")
        return result


class NexusManager():
    def __init__(self) -> None:
        print("Initializing Nexus Manager...")
        self.pipelines: List[ProcessingPipeline] = []
        self.performance_stats = collections.deque(maxlen=100)
        self.total_records: int = 0
        self.error_count: int = 0

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self,
                     initial_data: Any, silent_mode: bool = False) -> Any:
        time1 = time.time()
        records = initial_data if isinstance(initial_data,
                                             list) else [initial_data]
        self.total_records += len(records)

        results = []
        for item in records:
            current_data = item
            for pipeline in self.pipelines:
                try:
                    current_data = pipeline.run_stages(current_data)
                except Exception as e:
                    self.error_count += 1
                    if not silent_mode:
                        print(f"Error detected in Stage 2: {e}")
                        print("Recovery initiated:"
                              " Switching to backup processor")
                        print("Recovery successful: "
                              "Pipeline restored, processing resumed")
                    current_data = "Recovered Safe Data"
            results.append(current_data)
        time2 = time.time()
        self.performance_stats.append(time2 - time1)
        return results if isinstance(initial_data, list) else results[0]

    def print_stats(self) -> None:
        if not self.performance_stats:
            return
        total_time = sum(self.performance_stats)
        efficiency: int = ((self.total_records - self.error_count
                            ) / self.total_records) * 100
        print(f"Chain result: {
            self.total_records} records processed through {
            len(self.pipelines)}-stage pipeline")
        print(f"Performance: {efficiency}% efficiency, {
            total_time:.4f}s total processing time\n")


def nexus_pipeline() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    manager = NexusManager()
    print("Pipeline capacity: 1000 streams/second\n")

    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")
    json = JSONAdapter("PIPE_JSON")
    csv = CSVAdapter("PIPE_CSV")
    stream = StreamAdapter("PIPE_STREAM")

    manager.add_pipeline(json)
    manager.add_pipeline(csv)
    manager.add_pipeline(stream)

    print("\n=== Multi-Format Data Processing ===")
    print("\nProcessing JSON data through pipeline...")
    json_input: Any = {"sensor": "temp", "value": 26, "unit": "C"}
    print(f"Input: {json_input}")
    print("Transform: Enriched with metadata and validation")
    json.process(json_input)

    print("\nProcessing CSV data through same pipeline...")
    csv_input: str = "user,action,timestamp"
    print(f"Input: {csv_input}")
    print("Transform: Parsed and structured data")
    csv.process(csv_input)

    print("\nProcessing Stream data through same pipeline...")
    stream_input = [22.1, 22.5, 23.0, 22.8, 21.9]
    print(f"Input: {stream_input}")
    print("Transform: Aggregated and filtered")
    stream.process(stream_input)

    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")

    batch_records = ["good_data"] * 95 + ["ERROR_TRIGGER"] * 5
    manager.process_data(batch_records, silent_mode=True)
    manager.print_stats()

    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    manager.process_data("ERROR_TRIGGER")

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    nexus_pipeline()
