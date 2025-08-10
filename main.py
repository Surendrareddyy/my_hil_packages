import json
from instruments.base_instrument import BaseInstrument
from instruments.device_registry import get_driver_for_idn
from mocks.mock_instrument import MockInstrument

USE_MOCK = True

# load config
with open('config.json') as f:
    config = json.load(f)

# simple runner
for dev in config:
    print('\n---')
    print('Device config:', dev)
    if USE_MOCK:
        # choose IDN based on type/model for mock
        if dev['type'] == 'spectrum_analyzer':
            mock_idn = 'Rohde&Schwarz,SMB100B,12345,v1.0'
        elif dev['type'] == 'signal_generator':
            mock_idn = 'Keysight,N5183B,54321,v2.0'
        else:
            mock_idn = 'Keysight,E36313A,99999,v1.0'
        session = MockInstrument(idn_response=mock_idn, responses={':TRAC:DATA? TRACE1': '-10,-12,-15'})
        base = BaseInstrument(session=session)
        idn = base.query('*IDN?')
    else:
        base = BaseInstrument()
        base.connect_via_ip(ip=dev.get('ip'), port=dev.get('port'), resource_string=dev.get('resource_string'))
        idn = base.query('*IDN?')

    print('IDN:', idn)
    # pick driver
    try:
        driver_cls = get_driver_for_idn(idn)
    except Exception as e:
        print('Driver lookup failed:', e)
        base.close()
        continue

    # create device instance with same session so no new connection in mock
    device = driver_cls(session=base.session)

    # perform model-agnostic operations
    if hasattr(device, 'set_center_span'):
        device.set_center_span(1e9, 10e6)
        device.set_rbw(1e3)
        device.start_sweep()
        trace = device.fetch_trace_ascii()
        print('Trace:', trace)

    if hasattr(device, 'set_frequency'):
        device.set_frequency(1e9)
        device.set_power_dbm(-10)
        device.output_on()

    if hasattr(device, 'set_voltage_current'):
        device.set_voltage_current
