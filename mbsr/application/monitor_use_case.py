from typing import Iterator
from domains.interfaces import IPLCGateway
from domains.models import PLCState, RTCData

class MonitorPLCUseCase:
    def __init__(self, gateway: IPLCGateway):
        self.gateway = gateway

    def execute(self, device_ip: str, sync_rtc: bool = True) -> Iterator[PLCState]:
        if sync_rtc:
            rtc_now = RTCData.from_now()
            self.gateway.sync_rtc(rtc_now, device_ip)
        
        return self.gateway.stream_data(device_ip, interval_ms=500)
