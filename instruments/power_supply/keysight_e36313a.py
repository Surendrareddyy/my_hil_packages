from ..base_instrument import BaseInstrument

class KeysightE36313A(BaseInstrument):
    def set_voltage_current(self, v, i):
        self.write(f"SOUR:VOLT {v}")
        self.write(f"SOUR:CURR {i}")

    def output_on(self):
        self.write("OUTP ON")

    def output_off(self):
        self.write("OUTP OFF")

    def measure(self):
        v = float(self.query("MEAS:VOLT?"))
        i = float(self.query("MEAS:CURR?"))
        return v, i
