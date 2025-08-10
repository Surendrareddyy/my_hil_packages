from .base_sa import BaseSpectrumAnalyzer

class RSSMBV100A(BaseSpectrumAnalyzer):
    def set_center_span(self, center_hz, span_hz):
        self.write(f"FREQ:CENT {center_hz}")
        self.write(f"FREQ:SPAN {span_hz}")

    def set_rbw(self, rbw_hz):
        self.write(f"BAND:RES {rbw_hz}")

    def start_sweep(self):
        self.write("INIT")

    def fetch_trace_ascii(self):
        raw = self.query(':TRACE:DATA? TRACE1')
        vals = [v for v in raw.replace('\n','').split(',') if v.strip()]
        return [float(x) for x in vals]
