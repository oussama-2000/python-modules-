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
    def __init__(self):
        super().__init__()

    def process(self, data) -> str:

        print(f"Processing data: {data}")

        data_string = ""
        if data:
            try:
                for i in data:
                    data_string += str(i)
            except TypeError:
                pass

        validation = self.validate(data)
        if validation:
            print("Validation: Numeric data verified")
            print(self.format_output(data))
        else:
            print("Validation: Numeric data not verified")
        return data_string

    def validate(self, data) -> bool:
        try:
            for i in data:
                int(i)
        except (ValueError, TypeError):
            return False
        return True

    def format_output(self, result):
        length = len(result)
        summ = sum(result)
        avg = summ / length
        return (f"Output: Processed {length} numeric values"
                f",sum={summ}, avg={avg}")


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def process(self, data) -> str:

        print(f"Processing data: \"{data}\"")

        validation = self.validate(data)
        if validation:
            print("Validation: Text data verified")
            print(self.format_output(data))
        else:
            print("Validation: Text data not verified")

        return data

    def validate(self, data) -> bool:
        if type(data) is str:
            return True
        return False

    def format_output(self, result):
        characters_count = len(result)
        words_count = len(result.split(" "))
        return (f"Output: Processed text {characters_count} characters"
                f", {words_count} words")


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def process(self, data) -> str:

        print(f"Processing data: \"{data}\"")

        validation = self.validate(data)
        if validation:
            print("Validation: Log entry verified")
            print(self.format_output(data))
        else:
            print("Validation: Log entry not verified")
        return data

    def validate(self, data) -> bool:
        if type(data) is not str:
            return False
        if ":" not in data:
            return False
        if len(data.split(":")) != 2:
            return False
        return True

    def format_output(self, result):
        log = result.split(":")
        log_type = log[0]
        log_message = log[1]

        return (f"Output: [ALERT] {log_type} level detected:"
                f"{log_message}")


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("Initializing Numeric Processor...")
    num = NumericProcessor()
    result = num.process([1, 2, 3, 4, 5])

    print()
    print("Initializing Text Processor...")
    text = TextProcessor()
    result = text.process("Hello Nexus World")

    print()
    print("Initializing Log Processor...")
    log = LogProcessor()
    log.process("ERROR: Connection timeout")