import os
from datetime import datetime
from domains.models import PLCState

class DynamicConsoleTable:
    def __init__(self, title: str):
        self.title = title
        self.last_summary = None
        self.last_heartbeat = 0
        self._print_header()

    def _print_header(self):
        print("\n" + "="*115)
        print(f"       {self.title.upper()}")
        print("="*115)
        print(f"{'TIMESTAMP':<15} | {'PLC RTC FORMATADO':<20} | {'RAW RTC':<20} | {'RUN':<4} | {'OUT':<4} | {'X0 CLICKS':<10} | {'X1 CLICKS':<10}")
        print("-" * 115)

    def update(self, state: PLCState):
        agora_ts = datetime.now().timestamp()
        hora_pc = datetime.now().strftime('%H:%M:%S.%f')[:-3]
        
        rtc_str = state.rtc.to_datetime().strftime('%d/%m/%Y %H:%M:%S') if state.rtc else "N/A"
        raw_rtc = f"{state.rtc.day:02}/{state.rtc.month:02}/{state.rtc.year:02} {state.rtc.hour:02}:{state.rtc.minute:02}:{state.rtc.second:02}" if state.rtc else "N/A"
        
        icon_run = "OK" if state.m1000 else "!!"
        icon_y0  = "(O)" if state.y0 else "( )"
        
        current_summary = (state.x0, state.x1, state.y0, state.m1000, state.clicks_x0, state.clicks_x1)
        
        if current_summary != self.last_summary or (agora_ts - self.last_heartbeat) >= 1.0:
            prefix = " >>" if current_summary != self.last_summary and self.last_summary is not None else "   "
            
            line = (f"{hora_pc:<15} | {rtc_str:<20} | {raw_rtc:<20} | {icon_run:<4} | {icon_y0:<4} | "
                    f"{state.clicks_x0:<10} | {state.clicks_x1:<10}")
            
            print(f"{prefix} {line}")
            
            self.last_summary = current_summary
            self.last_heartbeat = agora_ts
