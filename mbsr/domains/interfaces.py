from abc import ABC, abstractmethod
from typing import Iterator
from .models import PLCState, RTCData

class IPLCGateway(ABC):
    @abstractmethod
    def sync_rtc(self, rtc: RTCData, device_ip: str) -> bool:
        """Sincroniza o relógio do PLC."""
        pass

    @abstractmethod
    def stream_data(self, device_ip: str, interval_ms: int) -> Iterator[PLCState]:
        """Stream de dados do PLC."""
        pass
