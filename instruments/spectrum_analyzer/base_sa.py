from ..base_instrument import BaseInstrument

class BaseSpectrumAnalyzer(BaseInstrument):
    def set_center_span(self, center_hz: float, span_hz: float):
        raise NotImplementedError

    def set_rbw(self, rbw_hz: float):
        raise NotImplementedError

    def start_sweep(self):
        raise NotImplementedError

    def fetch_trace_ascii(self):
        raise NotImplementedError
