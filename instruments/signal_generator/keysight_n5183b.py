from ..base_instrument import BaseInstrument

class KeysightN5183B(BaseInstrument):
    def set_frequency(self, hz):
        self.write(f"FREQ {hz}")

    def set_power_dbm(self, dbm):
        self.write(f"POW {dbm}")

    def output_on(self):
        self.write("OUTP ON")

    def output_off(self):
        self.write("OUTP OFF")
