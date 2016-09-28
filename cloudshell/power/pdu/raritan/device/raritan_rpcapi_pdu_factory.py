from raritan import rpc
from raritan.rpc import pdumodel, HttpException

from cloudshell.shell.core.driver_context import AutoLoadDetails, AutoLoadResource, AutoLoadAttribute
from cloudshell.power.pdu.raritan.device.rpcapi_outlet import RPCAPIOutlet
from cloudshell.power.pdu.device.pdu_factory import PDUFactory


class RaritanRpcApiPduFactory(PDUFactory):
    def __init__(self, context):
        self._agent = rpc.Agent("https", context.host, context.user, context.password)
        self._pdu_handler = pdumodel.Pdu('model/pdu/0', self._agent)

    def get_outlets(self):
        return [RPCAPIOutlet(x) for x in self._pdu_handler.getOutlets()]

    def get_inventory(self):
        try:
            metadata = self._pdu_handler.getMetaData()
        except HttpException as e:
            if 'unauthorized' in e.message:
                error_msg = 'User is unauthorized to access PDU with supplied password'
            else:
                error_msg = 'Unable to access PDU. Check if PDU address is valid.'
            raise Exception(error_msg)

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
                     for x, val in enumerate(self.get_outlets())]
        return resources
