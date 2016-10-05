import unittest
from cloudshell.power.pdu.raritan.shell_helper import get_outlets_by_address


class TestShellHelper(unittest.TestCase):

    def test_get_outlets_by_address(self):
        outlets = ['outlet' + str(x) for x in range(8)]
        ports = ['192.168.30.128/4', '192.168.30.128/6']
        result = get_outlets_by_address(outlets, ports)
        self.assertEqual(result, ['outlet3', 'outlet5'])
