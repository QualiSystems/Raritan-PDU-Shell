from raritan import rpc
from raritan.rpc import pdumodel


class RaritanRpcApi:
    def __init__(self, host, user, password):
        self._agent = rpc.Agent("https", host, user, password)

    def pdu_handler(self):
        return pdumodel.Pdu('model/pdu/0', self._agent)
