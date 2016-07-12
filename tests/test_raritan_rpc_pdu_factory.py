import unittest
from mock import Mock, patch

from cloudshell.power.pdu.raritan.device.raritan_rpcapi_pdu_factory import RaritanRpcApiPduFactory
from cloudshell.power.pdu.raritan.device.rpcapi_outlet import RPCAPIOutlet
from raritan.rpc.pdumodel import Pdu

FW_VERSION = '3.1.0.5-42165'
MANUFACTURER = 'Raritan'
MODEL = 'PX3-5145R'


class TestRaritanRpcApiPduFactory(unittest.TestCase):

    def setUp(self):
        context = Mock()
        self.factory = RaritanRpcApiPduFactory(context)

    @patch.object(Pdu, 'getOutlets')
    def test_get_outlets(self, mock_getOutlets):
        outlets = [Mock(), Mock()]
        mock_getOutlets.return_value = outlets
        result = self.factory.get_outlets()
        self.assertTrue(all([isinstance(outlet, RPCAPIOutlet) for outlet in result]))

    @patch.object(Pdu, 'getOutlets')
    @patch.object(Pdu, 'getMetaData')
    def test_get_inventory_attributes(self, mock_metadata, mock_getOutlets):
        mock_getOutlets.return_value = [RPCAPIOutlet(outlet_handler=Mock())]
        mock_metadata.return_value = Mock(fwRevision=FW_VERSION,
                                          nameplate=Mock(manufacturer=MANUFACTURER,
                                                         model=MODEL))
        result = self.factory.get_inventory()

        firmware_version = (x for x in result.attributes if x.attribute_name == 'Firmware Version').next()
        vendor = (x for x in result.attributes if x.attribute_name == 'Vendor').next()
        model_attr = (x for x in result.attributes if x.attribute_name == 'Model').next()

        self.assertTrue(firmware_version.attribute_value == FW_VERSION)
        self.assertTrue(vendor.attribute_value == MANUFACTURER)
        self.assertTrue(model_attr.attribute_value == MODEL)

        self.assertEqual(firmware_version.relative_address, '')
        self.assertEqual(vendor.relative_address, '')
        self.assertEqual(model_attr.relative_address, '')

    @patch.object(Pdu, 'getOutlets')
    @patch.object(Pdu, 'getMetaData')
    def test_get_inventory_resources(self, mock_metadata, mock_getOutlets):
        outlets = [RPCAPIOutlet(outlet_handler=Mock()), RPCAPIOutlet(outlet_handler=Mock())]
        mock_getOutlets.return_value = outlets
        mock_metadata.return_value = Mock(fwRevision=FW_VERSION,
                                          nameplate=Mock(manufacturer=MANUFACTURER,
                                                         model=MODEL))
        result = self.factory.get_inventory()

        self.assertEqual(len(result.resources), len(outlets))
        self.assertTrue(all([res.model == 'Generic Power Socket' for res in result.resources]))
        self.assertTrue(all(['Socket' in res.name for res in result.resources]))
        self.assertTrue(any([res.relative_address == '1' for res in result.resources]))
        self.assertTrue(any([res.relative_address == '2' for res in result.resources]))


