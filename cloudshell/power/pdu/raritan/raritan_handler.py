import time

from cloudshell.power.pdu.managed_devices.connected_to_pdu_resource import ConnectedToPduResource
from cloudshell.power.pdu.raritan.device.raritan_rpcapi_pdu_factory import RaritanRpcApiPduFactory
from cloudshell.power.pdu.raritan.device.factory_context import FactoryContext
from cloudshell.power.pdu.raritan.shell_helper import get_outlets_by_address


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
        return self.pdu.get_inventory()

    def power_on(self, context, ports):
        rr = ConnectedToPduResource(context.remote_endpoints)
        for o in get_outlets_by_address(ports):
            o.power_on
        return rr.online()

    def power_off(self, context, ports):
        rr = ConnectedToPduResource(context.remote_endpoints)
        for o in get_outlets_by_address(ports):
            o.power_off
        return rr.offline()

    def power_cycle(self, context, ports, delay=0):
        if delay < 0:
            delay = 0
        self.power_off(context, ports)
        time.sleep(delay)
        self.power_on(context, ports)
        return 'Power cycle complete'
















































    # SNMP legacy code
    #
    # import os
    # from cloudshell.configuration.cloudshell_snmp_configuration import SNMP_HANDLER
    #
    # @property
    # def snmp(self):
    #     if self._snmp is None:
    #         self._snmp = SNMP_HANDLER()
    #         path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mibs'))
    #         self._snmp.update_mib_sources(path)
    #     return self._snmp
    #
    # def _autoload_resources_by_snmp(self):
    #     outlets = self._get_outlets()
    #     resources = [AutoLoadResource('Generic Socket',
    #                                   'Socket ' + outlets[outlet]['outletLabel'],
    #                                   outlets[outlet]['outletLabel'])
    #                  for outlet in self.outlets]
    #     return resources
    #
    # def _get_outlets(self):
    #     return self.snmp.get_table('PDU2-MIB', 'outletConfigurationTable')



