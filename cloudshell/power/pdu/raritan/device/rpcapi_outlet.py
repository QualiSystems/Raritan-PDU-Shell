from threading import Lock

from raritan.rpc import pdumodel
from cloudshell.power.pdu.device.outlet import Outlet


POWERED_ON = pdumodel.Outlet.PowerState.PS_ON
POWERED_OFF = pdumodel.Outlet.PowerState.PS_OFF


class RPCAPIOutlet(Outlet):
    def __init__(self, outlet_handler):
        self._handler = outlet_handler
        self.lock = Lock()

    def power_on(self):
        with self.lock:
            self._handler.setPowerState(POWERED_ON)
            if self._handler.getState().powerState != POWERED_ON:
                Exception('Ports were not powered on')

    def power_off(self):
        with self.lock:
            self._handler.setPowerState(POWERED_OFF)
            if self._handler.getState().powerState != POWERED_OFF:
                Exception('Ports were not powered off')

