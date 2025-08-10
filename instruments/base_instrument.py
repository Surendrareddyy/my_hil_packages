import pyvisa

class BaseInstrument:
    """Lightweight base wrapper. Can operate in simulation mode when session is provided by a mock."""
    def __init__(self, session=None, ip=None, port=None, resource_string=None, timeout_ms=5000):
        self.session = session
        self.ip = ip
        self.port = port
        self.resource_string = resource_string
        self.timeout_ms = timeout_ms

    def connect_via_ip(self, ip=None, port=None, resource_string=None):
        rm = pyvisa.ResourceManager()
        if resource_string:
            rs = resource_string
        elif ip and port:
            rs = f"TCPIP0::{ip}::{port}::SOCKET"
        elif ip:
            rs = f"TCPIP0::{ip}::inst0::INSTR"
        else:
            raise ValueError("Provide ip+port or resource_string")
        self.session = rm.open_resource(rs)
        self.session.timeout = self.timeout_ms
        return self.session

    def write(self, cmd: str):
        return self.session.write(cmd)

    def query(self, cmd: str) -> str:
        return self.session.query(cmd)

    def read_raw(self):
        return self.session.read_raw()

    def close(self):
        try:
            self.session.close()
        except Exception:
            pass
