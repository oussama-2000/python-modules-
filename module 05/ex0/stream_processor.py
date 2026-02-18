from typing import Any, List, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        pass

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

    def process(self, data: Any, show: bool) -> str:
        if show:
            print(f"Processing data: {data}")

        validation = self.validate(data)
        if not validation:
            print("Validation: Numeric data not verified")
            return (self.format_output("Invalid numeric data"))
        if show:
            print("Validation: Numeric data verified")

        length = len(data)
        summ = sum(data)
        if length != 0:
            avg = summ / length
        else:
            avg = 0
        result =  (f"Processed {length} numeric values"
                    f",sum={summ}, avg={avg}")
        if show:
            print(f"Output: {self.format_output(result)}")
        else:
            print(self.format_output(result))

        return f"Output: {self.format_output(result)}"

    def validate(self, data: Any) -> bool:
        try:
            for i in data:
                int(i)
        except (ValueError, TypeError):
            return False
        return True

    def format_output(self, result: str) -> str:
        return result


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any, show: bool) -> str:
        if show:
            print(f"Processing data: \"{data}\"")

        validation = self.validate(data)
        if not validation:
            print("Validation: Text data not verified")
            return self.format_output("Invalid text data")
        if show:
            print("Validation: Text data verified")

        characters_count = len(data)
        words_count = len(data.split(" "))
        result = (f"Processed text {characters_count} characters"
                    f", {words_count} words")
        if show:
            print(f"Output: {self.format_output(result)}")
        else:
            print(self.format_output(result))


        return f"Output: {self.format_output(result)}"

    def validate(self, data: Any) -> bool:
        if type(data) is str:
            return True
        return False

    def format_output(self, result: str) -> str:
        return result


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any, show: bool) -> str:
        if show:
            print(f"Processing data: \"{data}\"")

        validation = self.validate(data)
        if not validation:
            print("Validation: Log entry not verified")
            return self.format_output("Invalid log data")
        if show:
            print("Validation: Log entry verified")

        log = data.split(":")
        log_type = log[0]
        log_message = log[1]

        result = (f"[ALERT] {log_type} level detected:"
                    f"{log_message}")
        if show:
            print(f"Output: {self.format_output(result)}")
        else:
            print(self.format_output(result))

        return f"Output: {self.format_output(result)}"

    def validate(self, data: Any) -> bool:
        if type(data) is not str:
            return False
        if ":" not in data:
            return False
        if len(data.split(":")) != 2:
            return False
        return True

    def format_output(self, result: str) -> str:
        return result

if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("Initializing Numeric Processor...")
    num = NumericProcessor()
    result = num.process([1, 2, 3, 4, 5], True)

    print()
    print("Initializing Text Processor...")
    text = TextProcessor()
    result = text.process("Hello Nexus World", True)

    print()
    print("Initializing Log Processor...")
    log = LogProcessor()
    log.process("ERROR: Connection timeout", True)

    print()
    print("=== Polymorphic Processing Demo ===")
    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    data : List[Any] = [
        [2, 2, 2],
        "aaaaaa aaaaa",
        "INFO: System ready"
    ]
    i = 0
    for processor in processors:
        print(f"Result {i + 1}: ", end="")
        processor.process(data[i], False)
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")

