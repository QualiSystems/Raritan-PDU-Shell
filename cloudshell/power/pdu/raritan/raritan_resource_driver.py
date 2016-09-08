from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.context_utils import context_from_args
from cloudshell.shell.core.driver_bootstrap import DriverBootstrap
from cloudshell.power.pdu.raritan.raritan_handler import RaritanHandler
from cloudshell.power.pdu.power_resource_driver_interface import PowerResourceDriverInterface


class RaritanDriver(ResourceDriverInterface, PowerResourceDriverInterface):
    def __init__(self):
        bootstrap = DriverBootstrap()
        bootstrap.initialize()
        self.handler = RaritanHandler()

    @context_from_args
    def initialize(self, context):
        """
        :type context: cloudshell.shell.core.driver_context.InitCommandContext
        """
        self.handler.initialize(context)
        return 'Finished initializing'

    # Destroy the driver session, this function is called every time a driver instance is destroyed
    # This is a good place to close any open sessions, finish writing to log files
    def cleanup(self):
        pass

    @context_from_args
    def get_inventory(self, context):
        """ Returns device resource, sub-resources and attributes

        :type context: cloudshell.shell.core.driver_context.AutoLoadCommandContext
        :rtype: cloudshell.shell.core.driver_context.AutoLoadDetails
        """
        return self.handler.get_inventory(context=context)

    @context_from_args
    def PowerOn(self, context, ports):
        """ Powers on outlets on the managed PDU

        :type context: cloudshell.shell.core.driver_context.ResourceRemoteCommandContext
        :param ports: full addresses of outlets on PDU, example: ['192.168.30.128/4', '192.168.30.128/6']
        :type ports: str
        :return: command result message
        :rtype: str
        """
        return self.handler.power_on(context, ports)

    @context_from_args
    def PowerOff(self, context, ports):
        """ Powers off outlets on the managed PDU

        :type context: cloudshell.shell.core.driver_context.ResourceRemoteCommandContext
        :param ports: full addresses of outlets on PDU, example: ['192.168.30.128/4', '192.168.30.128/6']
        :type ports: str
        :return: command result message
        :rtype: str
        """
        return self.handler.power_off(context, ports)

    @context_from_args
    def PowerCycle(self, context, ports, delay=0):
        """ Powers off outlets, waits during delay, then powers outlets on

        :type context: cloudshell.shell.core.driver_context.ResourceRemoteCommandContext
        :param ports: full addresses of outlets on PDU, example: ['192.168.30.128/4', '192.168.30.128/6']
        :type ports: str
        :param delay: seconds to wait after power off
        :type delay: int
        :return: command result message
        :rtype: str
        """
        return self.handler.power_cycle(context, ports)
