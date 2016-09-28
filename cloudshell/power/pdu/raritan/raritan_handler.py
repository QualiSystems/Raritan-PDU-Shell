import time

from cloudshell.power.pdu.managed_devices.connected_to_pdu_resource import ConnectedToPduResource
from cloudshell.power.pdu.raritan.device.raritan_rpcapi_pdu_factory import RaritanRpcApiPduFactory
from cloudshell.power.pdu.raritan.device.factory_context import FactoryContext
from cloudshell.power.pdu.raritan.shell_helper import get_outlets_by_address
from debug_utils import debugger


class RaritanHandler:
    def __init__(self, pdu_factory=RaritanRpcApiPduFactory):
        self.pdu = None
        self._outlets = []
        self._pdu_factory = pdu_factory

    @property
    def outlets(self):
        if not self._outlets:
            self._outlets = self.pdu.get_outlets()
        return self._outlets

    def initialize(self, context):
        factory_context = FactoryContext(context)
        self.pdu = self._pdu_factory(factory_context)

    def get_inventory(self, context):
        self.initialize(context)
        return self.pdu.get_inventory()

    def power_on(self, context, ports):
        debugger.attach_debugger()
        self.initialize(context)
        rr = ConnectedToPduResource(context.remote_endpoints)
        for o in get_outlets_by_address(self.outlets, ports):
            o.power_on
        return rr.online()

    def power_off(self, context, ports):
        self.initialize(context)
        rr = ConnectedToPduResource(context.remote_endpoints)
        for o in get_outlets_by_address(self.outlets, ports):
            o.power_off
        return rr.offline()

    def power_cycle(self, context, ports, delay=0):
        self.initialize(context)
        self._validate_power_cycle_delay(delay)
        self.power_off(context, ports)
        time.sleep(delay)
        self.power_on(context, ports)
        return 'Power cycle complete'

    @staticmethod
    def _validate_power_cycle_delay(delay):
        try:
            int(delay)
            if delay < 0:
                raise ValueError('Must be non negative integer')
        except ValueError:
            raise Exception('Delay represents the seconds between power off and power on. \n'
                            'You ran the power cycle command with a delay argument of {0}, '
                            'but acceptable values are empty,'
                            '0, or a positive integer value')



