# Simple registry mapping IDN substrings to driver classes
from .spectrum_analyzer.rs_smb100b import RSSMB100B
from .spectrum_analyzer.rs_smbv100a import RSSMBV100A
from .signal_generator.keysight_n5183b import KeysightN5183B
from .power_supply.keysight_e36313a import KeysightE36313A

DEVICE_MAP = [
    ("ROHDE", "SMB100B", RSSMB100B),
    ("ROHDE", "SMBV100A", RSSMBV100A),
    ("KEYSIGHT", "N5183B", KeysightN5183B),
    ("KEYSIGHT", "E36313A", KeysightE36313A),
]


def get_driver_for_idn(idn: str):
    s = idn.upper()
    for vendor_sub, model_sub, cls in DEVICE_MAP:
        if vendor_sub in s and model_sub in s:
            return cls
    # fallback: try by vendor only
    for vendor_sub, model_sub, cls in DEVICE_MAP:
        if vendor_sub in s:
            return cls
    raise ValueError(f"No driver found for IDN: {idn}")
