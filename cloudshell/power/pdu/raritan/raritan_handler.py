import os
import inject
import time

from cloudshell.configuration.cloudshell_snmp_configuration import SNMP_HANDLER
from cloudshell.shell.core.driver_context import AutoLoadDetails, AutoLoadResource, AutoLoadAttribute
from cloudshell.shell.core.context_utils import get_attribute_by_name
from cloudshell.api.cloudshell_api import CloudShellAPISession
from cloudshell.power.pdu.raritan.api.raritan_rpc_api import RaritanRpcApi
from cloudshell.power.pdu.managed_devices.connected_to_pdu_resource import ConnectedToPduResource

from raritan import rpc
from raritan.rpc import pdumodel


class RaritanHandler:
    def __init__(self):
        self._snmp = None
        self._agent = None
        self._pdu = None
        self._user = None
        self._password = None
        self._outlets = []

    @property
    def snmp(self):
        if self._snmp is None:
            self._snmp = SNMP_HANDLER()
            path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mibs'))
            self._snmp.update_mib_sources(path)
        return self._snmp

    @property
    def pdu(self):
        if self._pdu is None:
            self._pdu = pdumodel.Pdu('model/pdu/0', self.agent)
        return self._pdu

    @property
    def outlets(self):
        # uses raritan RPC api
        if not self._outlets:
            self._outlets = self.pdu.getOutlets()
        return self._outlets

    def initialize(self, context):
        user = get_attribute_by_name('User', context)
        password = self._get_decrypted_password(context)
        rari_api = RaritanRpcApi(context.resource.address, user, password)
        self._pdu = rari_api.pdu_handler()

    def power_on(self, context, ports):
        rr = ConnectedToPduResource(context.remote_endpoints)
        from debug_utils import debugger
        debugger.attach_debugger()
        result = True
        for o in self._get_outlets_by_address(ports):
            o.setPowerState(pdumodel.Outlet.PowerState.PS_ON)
            result = o.getState()
            print result
        return rr.online()

    def power_off(self, context, ports):
        rr = ConnectedToPduResource(context.remote_endpoints)
        for o in self._get_outlets_by_address(ports):
            o.setPowerState(pdumodel.Outlet.PowerState.PS_OFF)
        return rr.offline()

    def power_cycle(self, context, ports, delay=0):
        if delay < 0:
            delay = 0
        self.power_off(context, ports)
        time.sleep(delay)
        self.power_on(context, ports)
        return 'Power cycle complete'

    def get_inventory(self, context):
        metadata = self.pdu.getMetaData()
        resources = self._autoload_resources_by_rpc()
        attributes = [AutoLoadAttribute('', 'Firmware Version', metadata.fwRevision),
                      AutoLoadAttribute('', 'Vendor', metadata.nameplate.manufacturer),
                      AutoLoadAttribute('', 'Model', metadata.nameplate.model)]
        result = AutoLoadDetails(resources, attributes)
        return result

    def _autoload_resources_by_rpc(self):
        resources = [AutoLoadResource('Generic Power Socket',
                                      'Socket ' + str(x+1),
                                      str(x+1))
                     for x, val in enumerate(self.outlets)]
        return resources

    def _autoload_resources_by_snmp(self):
        outlets = self._get_outlets()
        resources = [AutoLoadResource('Generic Socket',
                                      'Socket ' + outlets[outlet]['outletLabel'],
                                      outlets[outlet]['outletLabel'])
                     for outlet in self.outlets]
        return resources

    def _get_outlets(self):
        return self.snmp.get_table('PDU2-MIB', 'outletConfigurationTable')

    def _get_outlets_by_address(self, ports):
        # ports: ['192.168.30.128/4']

        def socket(x):
            n = int(x.split('/')[-1])
            return self.outlets[n-1]

        return [socket(x) for x in ports]

    def _get_decrypted_password(self, context):
        password = get_attribute_by_name('Password', context)
        api = inject.instance('api')
        return api.DecryptPassword(password).Value


