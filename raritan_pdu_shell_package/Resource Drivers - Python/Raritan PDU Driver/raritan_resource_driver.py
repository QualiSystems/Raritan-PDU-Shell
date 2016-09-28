from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.context_utils import context_from_args
from cloudshell.shell.core.driver_bootstrap import DriverBootstrap
from cloudshell.power.pdu.raritan.raritan_handler import RaritanHandler


class RaritanDriver(ResourceDriverInterface):
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
        """
        Return device structure with all standard attributes
        :return: result
        :rtype: string
        :type context: cloudshell.shell.core.driver_context.AutoLoadCommandContext
        """
        return self.handler.get_inventory(context=context)

    @context_from_args
    def PowerOn(self, context, ports):
        """
        :type context: cloudshell.shell.core.driver_context.ResourceRemoteCommandContext
        """
        return self.handler.power_on(context, ports)

    @context_from_args
    def PowerOff(self, context, ports):
        """
        :type context: cloudshell.shell.core.driver_context.ResourceRemoteCommandContext
        """
        return self.handler.power_off(context, ports)

    @context_from_args
    def PowerCycle(self, context, ports, delay=0):
        """
        :type context: cloudshell.shell.core.driver_context.ResourceRemoteCommandContext
        """
        try:
            float(delay)
        except ValueError:
            raise Exception('Delay must be empty or have a numeric value')
        return self.handler.power_cycle(context, ports, float(delay))
