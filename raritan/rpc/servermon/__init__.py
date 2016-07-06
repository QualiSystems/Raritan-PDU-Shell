# Do NOT edit this file!
# It was generated by IdlC class idl.json.python.ProxyAsnVisitor.

#
# Section generated from "/home/nb/builds/MEGA/px2-3.1.x-branch-20150209-none-release-none-pdu-raritan/fwcomponents/mkdist/tmp/px2_final/libidl_client/servermon/idl/ServerMonitor.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.servermon


# interface
class ServerMonitor(Interface):
    idlType = "servermon.ServerMonitor:2.0.0"

    # enumeration
    class ServerReachability(Enumeration):
        idlType = "servermon.ServerMonitor.ServerReachability:1.0.0"
        values = ["WAITING", "REACHABLE", "UNREACHABLE", "ERROR"]

    ServerReachability.WAITING = ServerReachability(0)
    ServerReachability.REACHABLE = ServerReachability(1)
    ServerReachability.UNREACHABLE = ServerReachability(2)
    ServerReachability.ERROR = ServerReachability(3)

    # structure
    class ServerSettings(Structure):
        idlType = "servermon.ServerMonitor.ServerSettings:1.0.0"
        elements = ["host", "enabled", "pingInterval", "retryInterval", "activationCount", "failureCount", "resumeDelay", "resumeCount"]

        def __init__(self, host, enabled, pingInterval, retryInterval, activationCount, failureCount, resumeDelay, resumeCount):
            typecheck.is_string(host, AssertionError)
            typecheck.is_bool(enabled, AssertionError)
            typecheck.is_int(pingInterval, AssertionError)
            typecheck.is_int(retryInterval, AssertionError)
            typecheck.is_int(activationCount, AssertionError)
            typecheck.is_int(failureCount, AssertionError)
            typecheck.is_int(resumeDelay, AssertionError)
            typecheck.is_int(resumeCount, AssertionError)

            self.host = host
            self.enabled = enabled
            self.pingInterval = pingInterval
            self.retryInterval = retryInterval
            self.activationCount = activationCount
            self.failureCount = failureCount
            self.resumeDelay = resumeDelay
            self.resumeCount = resumeCount

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                host = json['host'],
                enabled = json['enabled'],
                pingInterval = json['pingInterval'],
                retryInterval = json['retryInterval'],
                activationCount = json['activationCount'],
                failureCount = json['failureCount'],
                resumeDelay = json['resumeDelay'],
                resumeCount = json['resumeCount'],
            )
            return obj

        def encode(self):
            json = {}
            json['host'] = self.host
            json['enabled'] = self.enabled
            json['pingInterval'] = self.pingInterval
            json['retryInterval'] = self.retryInterval
            json['activationCount'] = self.activationCount
            json['failureCount'] = self.failureCount
            json['resumeDelay'] = self.resumeDelay
            json['resumeCount'] = self.resumeCount
            return json

    # structure
    class ServerStatus(Structure):
        idlType = "servermon.ServerMonitor.ServerStatus:1.0.0"
        elements = ["reachable", "lastRequest", "lastResponse", "requests", "responses", "failures", "resumes"]

        def __init__(self, reachable, lastRequest, lastResponse, requests, responses, failures, resumes):
            typecheck.is_enum(reachable, raritan.rpc.servermon.ServerMonitor.ServerReachability, AssertionError)
            typecheck.is_time(lastRequest, AssertionError)
            typecheck.is_time(lastResponse, AssertionError)
            typecheck.is_int(requests, AssertionError)
            typecheck.is_int(responses, AssertionError)
            typecheck.is_int(failures, AssertionError)
            typecheck.is_int(resumes, AssertionError)

            self.reachable = reachable
            self.lastRequest = lastRequest
            self.lastResponse = lastResponse
            self.requests = requests
            self.responses = responses
            self.failures = failures
            self.resumes = resumes

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                reachable = raritan.rpc.servermon.ServerMonitor.ServerReachability.decode(json['reachable']),
                lastRequest = raritan.rpc.Time.decode(json['lastRequest']),
                lastResponse = raritan.rpc.Time.decode(json['lastResponse']),
                requests = json['requests'],
                responses = json['responses'],
                failures = json['failures'],
                resumes = json['resumes'],
            )
            return obj

        def encode(self):
            json = {}
            json['reachable'] = raritan.rpc.servermon.ServerMonitor.ServerReachability.encode(self.reachable)
            json['lastRequest'] = raritan.rpc.Time.encode(self.lastRequest)
            json['lastResponse'] = raritan.rpc.Time.encode(self.lastResponse)
            json['requests'] = self.requests
            json['responses'] = self.responses
            json['failures'] = self.failures
            json['resumes'] = self.resumes
            return json

    # structure
    class Server(Structure):
        idlType = "servermon.ServerMonitor.Server:1.0.0"
        elements = ["settings", "status"]

        def __init__(self, settings, status):
            typecheck.is_struct(settings, raritan.rpc.servermon.ServerMonitor.ServerSettings, AssertionError)
            typecheck.is_struct(status, raritan.rpc.servermon.ServerMonitor.ServerStatus, AssertionError)

            self.settings = settings
            self.status = status

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                settings = raritan.rpc.servermon.ServerMonitor.ServerSettings.decode(json['settings'], agent),
                status = raritan.rpc.servermon.ServerMonitor.ServerStatus.decode(json['status'], agent),
            )
            return obj

        def encode(self):
            json = {}
            json['settings'] = raritan.rpc.servermon.ServerMonitor.ServerSettings.encode(self.settings)
            json['status'] = raritan.rpc.servermon.ServerMonitor.ServerStatus.encode(self.status)
            return json

    ERR_NO_SUCH_ID = 1

    ERR_INVALID_SETTINGS = 2

    ERR_DUPLICATE_HOSTNAME = 3

    ERR_MAX_SERVERS_REACHED = 4

    def addServer(self, settings):
        agent = self.agent
        typecheck.is_struct(settings, raritan.rpc.servermon.ServerMonitor.ServerSettings, AssertionError)
        args = {}
        args['settings'] = raritan.rpc.servermon.ServerMonitor.ServerSettings.encode(settings)
        rsp = agent.json_rpc(self.target, 'addServer', args)
        _ret_ = rsp['_ret_']
        id = rsp['id']
        typecheck.is_int(_ret_, DecodeException)
        typecheck.is_int(id, DecodeException)
        return (_ret_, id)

    def modifyServer(self, id, settings):
        agent = self.agent
        typecheck.is_int(id, AssertionError)
        typecheck.is_struct(settings, raritan.rpc.servermon.ServerMonitor.ServerSettings, AssertionError)
        args = {}
        args['id'] = id
        args['settings'] = raritan.rpc.servermon.ServerMonitor.ServerSettings.encode(settings)
        rsp = agent.json_rpc(self.target, 'modifyServer', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def deleteServer(self, id):
        agent = self.agent
        typecheck.is_int(id, AssertionError)
        args = {}
        args['id'] = id
        rsp = agent.json_rpc(self.target, 'deleteServer', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def getServer(self, id):
        agent = self.agent
        typecheck.is_int(id, AssertionError)
        args = {}
        args['id'] = id
        rsp = agent.json_rpc(self.target, 'getServer', args)
        _ret_ = rsp['_ret_']
        server = raritan.rpc.servermon.ServerMonitor.Server.decode(rsp['server'], agent)
        typecheck.is_int(_ret_, DecodeException)
        typecheck.is_struct(server, raritan.rpc.servermon.ServerMonitor.Server, DecodeException)
        return (_ret_, server)

    def listServers(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'listServers', args)
        _ret_ = dict([(
            elem['key'],
            raritan.rpc.servermon.ServerMonitor.Server.decode(elem['value'], agent))
            for elem in rsp['_ret_']])
        return _ret_
