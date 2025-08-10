from .base_sa import BaseSpectrumAnalyzer

class RSSMB100B(BaseSpectrumAnalyzer):
    def set_center_span(self, center_hz, span_hz):
        self.write(f"SENS:FREQ:CENT {center_hz}")
        self.write(f"SENS:FREQ:SPAN {span_hz}")

    def set_rbw(self, rbw_hz):
        self.write(f"SENS:BAND:RES {rbw_hz}")

    def start_sweep(self):
        self.write("INIT:IMM")

    def fetch_trace_ascii(self):
        raw = self.query(':TRAC:DATA? TRACE1')
        # parse comma separated
        vals = [v for v in raw.replace('\n','').split(',') if v.strip()]
        return [float(x) for x in vals]
