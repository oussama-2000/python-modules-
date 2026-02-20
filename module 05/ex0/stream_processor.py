from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod

del Dict, Union, Optional


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.show = True

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output:{result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        if self.show:
            print("Initializing Numeric Processor...")
            print(f"Processing data: {data}")

        validation = self.validate(data)
        if not validation:
            print("Validation: Numeric data not verified")
            return (self.format_output("Invalid numeric data"))
        if self.show:
            print("Validation: Numeric data verified")
        length: int = 0
        summ: int = 0
        avg: float = 0
        if isinstance(data, list):
            length = len(data)
            summ = sum(data)
            if length != 0:
                avg = summ / length
            else:
                avg = 0
        else:
            length = 1
            summ = data
            avg = data
        result = (f"Processed {length} numeric values"
                  f",sum={summ}, avg={avg}")
        if self.show:
            print(f"Output: {self.format_output(result)}")
        else:
            print(self.format_output(result))

        return f"Output: {self.format_output(result)}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, (list, int)):
            return False
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
        return True

    def format_output(self, result: str) -> str:
        return result


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        if self.show:
            print("Initializing Text Processor...")
            print(f"Processing data: \"{data}\"")

        validation = self.validate(data)
        if not validation:
            print("Validation: Text data not verified")
            return self.format_output("Invalid text data")
        if self.show:
            print("Validation: Text data verified")

        characters_count = len(data)
        words_count = len(data.strip().split(" "))
        result = (f"Processed text {characters_count} characters"
                  f", {words_count} words")
        if self.show:
            print(f"Output: {self.format_output(result)}")
        else:
            print(self.format_output(result))

        return f"Output: {self.format_output(result)}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        if not data or data.isspace():
            return False
        return True

    def format_output(self, result: str) -> str:
        return result


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        if self.show:
            print("Initializing Log Processor...")
            print(f"Processing data: \"{data}\"")

        validation = self.validate(data)
        if not validation:
            print("Validation: Log entry not verified")
            return self.format_output("Invalid log data")
        if self.show:
            print("Validation: Log entry verified")

        log = data.split(":")
        log_type = log[0]
        log_message = log[1]

        result = (f"{'[ALERT]' if log_type.lower() == 'error' else '[INFO]'}"
                  f" {log_type} level detected:"
                  f"{log_message}")
        if self.show:
            print(f"Output: {self.format_output(result)}")
        else:
            print(self.format_output(result))

        return f"Output: {self.format_output(result)}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        if ":" not in data:
            return False
        if len(data.split(":")) != 2:
            return False
        if not data.split(":")[0] or not data.split(":")[1]:
            return False
        if data.split(":")[0].isspace() or not data.split(":")[1].isspace():
            return False
        return True

    def format_output(self, result: str) -> str:
        return result


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    num: DataProcessor = NumericProcessor()
    num.process([1, 2, 3, 4, 5])

    print()
    text: DataProcessor = TextProcessor()
    text.process("Hello Nexus World")

    print()
    log: DataProcessor = LogProcessor()
    log.process("ERROR: Connection timeout")

    print()
    print("=== Polymorphic Processing Demo ===\n")
    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    for instance in processors:
        instance.show = False

    data: List[Any] = [
        [2, 2, 2],
        "aaaaaa aaaaa",
        "INFO: System ready"
    ]
    i: int = 0
    for processor in processors:
        print(f"Result {i + 1}: ", end="")
        processor.process(data[i])
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
