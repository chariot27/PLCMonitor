from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class RTCData:
    second: int
    minute: int
    hour: int
    day: int
    month: int
    year: int

    def to_datetime(self) -> datetime:
        # Assumindo que year é YY (ex: 26)
        full_year = 2000 + self.year if self.year < 100 else self.year
        return datetime(full_year, self.month, self.day, self.hour, self.minute, self.second)

    @classmethod
    def from_now(cls):
        now = datetime.now()
        return cls(
            second=now.second,
            minute=now.minute,
            hour=now.hour,
            day=now.day,
            month=now.month,
            year=now.year % 100
        )

@dataclass
class PLCState:
    x0: bool
    x1: bool
    y0: bool
    m1000: bool
    rtc: Optional[RTCData] = None
    clicks_x0: int = 0
    clicks_x1: int = 0
    is_real: bool = True
