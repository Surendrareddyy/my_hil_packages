import json
import time

class MockInstrument:
    def __init__(self, idn_response=None, responses=None, delay=0.0):
        # idn_response: e.g. "Rohde&Schwarz,SMB100B,1234,v1.0"
        self.idn_response = idn_response or "MOCK_VENDOR,MOCK_MODEL,0000,1.0"
        self.delay = delay
        self._responses = responses or {}

    def query(self, cmd):
        time.sleep(self.delay)
        if cmd.strip().upper() == "*IDN?":
            return self.idn_response
        # return mapped response
        key = cmd.strip()
        if key in self._responses:
            return self._responses[key]
        # default
        return "0"

    def write(self, cmd):
        print(f"[MOCK WRITE] {cmd}")

    def read_raw(self):
        return b""

    def close(self):
        print("[MOCK CLOSED]")
