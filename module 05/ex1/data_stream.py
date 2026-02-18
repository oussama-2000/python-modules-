from abc import ABC , abstractmethod
from typing import List, Any, Optional, Dict, Union

class DataStream(ABC):

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
        = None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass

class SensorStream(DataStream):
    def __init__(self, stream_id: int) -> None:
        super().__init__(self, stream_id)
        pass

class TransactionStream(DataStream):
        def __init__(self, stream_id: int) -> None:
            super().__init__(self, stream_id)
        pass

class EventStream(DataStream):
        def __init__(self, stream_id: int) -> None:
            super().__init__(self, stream_id)
        pass
