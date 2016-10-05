from raritan import rpc
from raritan.rpc import pdumodel, HttpException

from cloudshell.shell.core.driver_context import AutoLoadDetails, AutoLoadResource, AutoLoadAttribute
from cloudshell.power.pdu.raritan.device.rpcapi_outlet import RPCAPIOutlet
from cloudshell.power.pdu.device.pdu_factory import PDUFactory


class RaritanRpcApiPduFactory(PDUFactory):
    def __init__(self, context):
        self._context = context

    def get_outlets(self):
        handler = self._get_handler()
        return [RPCAPIOutlet(x) for x in handler.getOutlets()]

    def _get_handler(self):
        agent = rpc.Agent("https", self._context.host, self._context.user, self._context.password)
        return pdumodel.Pdu('model/pdu/0', agent)

    def get_inventory(self):
        handler = self._get_handler()
        try:
            metadata = handler.getMetaData()
        except HttpException as e:
            if 'unauthorized' in e.message.lower():
                error_msg = 'User is unauthorized to access PDU. Check if username and or password valid'
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
