# Do NOT edit this file!
# It was generated by IdlC class idl.json.python.ProxyAsnVisitor.

#
# Section generated from "/home/nb/builds/MEGA/px2-3.1.x-branch-20150209-none-release-none-pdu-raritan/fwcomponents/mkdist/tmp/px2_final/libisys/src/idl/Security.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.event

import raritan.rpc.security


# enumeration
class IpfwPolicy(Enumeration):
    idlType = "security.IpfwPolicy:1.0.0"
    values = ["ACCEPT", "DROP", "REJECT"]

IpfwPolicy.ACCEPT = IpfwPolicy(0)
IpfwPolicy.DROP = IpfwPolicy(1)
IpfwPolicy.REJECT = IpfwPolicy(2)

# structure
class IpfwRule(Structure):
    idlType = "security.IpfwRule:1.0.0"
    elements = ["ipMask", "policy"]

    def __init__(self, ipMask, policy):
        typecheck.is_string(ipMask, AssertionError)
        typecheck.is_enum(policy, raritan.rpc.security.IpfwPolicy, AssertionError)

        self.ipMask = ipMask
        self.policy = policy

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            ipMask = json['ipMask'],
            policy = raritan.rpc.security.IpfwPolicy.decode(json['policy']),
        )
        return obj

    def encode(self):
        json = {}
        json['ipMask'] = self.ipMask
        json['policy'] = raritan.rpc.security.IpfwPolicy.encode(self.policy)
        return json

# structure
class IpFw(Structure):
    idlType = "security.IpFw:2.0.0"
    elements = ["enabled", "defaultPolicyIn", "defaultPolicyOut", "ruleSetIn", "ruleSetOut"]

    def __init__(self, enabled, defaultPolicyIn, defaultPolicyOut, ruleSetIn, ruleSetOut):
        typecheck.is_bool(enabled, AssertionError)
        typecheck.is_enum(defaultPolicyIn, raritan.rpc.security.IpfwPolicy, AssertionError)
        typecheck.is_enum(defaultPolicyOut, raritan.rpc.security.IpfwPolicy, AssertionError)
        for x0 in ruleSetIn:
            typecheck.is_struct(x0, raritan.rpc.security.IpfwRule, AssertionError)
        for x0 in ruleSetOut:
            typecheck.is_struct(x0, raritan.rpc.security.IpfwRule, AssertionError)

        self.enabled = enabled
        self.defaultPolicyIn = defaultPolicyIn
        self.defaultPolicyOut = defaultPolicyOut
        self.ruleSetIn = ruleSetIn
        self.ruleSetOut = ruleSetOut

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            enabled = json['enabled'],
            defaultPolicyIn = raritan.rpc.security.IpfwPolicy.decode(json['defaultPolicyIn']),
            defaultPolicyOut = raritan.rpc.security.IpfwPolicy.decode(json['defaultPolicyOut']),
            ruleSetIn = [raritan.rpc.security.IpfwRule.decode(x0, agent) for x0 in json['ruleSetIn']],
            ruleSetOut = [raritan.rpc.security.IpfwRule.decode(x0, agent) for x0 in json['ruleSetOut']],
        )
        return obj

    def encode(self):
        json = {}
        json['enabled'] = self.enabled
        json['defaultPolicyIn'] = raritan.rpc.security.IpfwPolicy.encode(self.defaultPolicyIn)
        json['defaultPolicyOut'] = raritan.rpc.security.IpfwPolicy.encode(self.defaultPolicyOut)
        json['ruleSetIn'] = [raritan.rpc.security.IpfwRule.encode(x0) for x0 in self.ruleSetIn]
        json['ruleSetOut'] = [raritan.rpc.security.IpfwRule.encode(x0) for x0 in self.ruleSetOut]
        return json

# enumeration
class RoleAccessPolicy(Enumeration):
    idlType = "security.RoleAccessPolicy:1.0.0"
    values = ["ALLOW", "DENY"]

RoleAccessPolicy.ALLOW = RoleAccessPolicy(0)
RoleAccessPolicy.DENY = RoleAccessPolicy(1)

# structure
class RoleAccessRule(Structure):
    idlType = "security.RoleAccessRule:1.0.0"
    elements = ["startIp", "endIp", "roleId", "policy"]

    def __init__(self, startIp, endIp, roleId, policy):
        typecheck.is_string(startIp, AssertionError)
        typecheck.is_string(endIp, AssertionError)
        typecheck.is_int(roleId, AssertionError)
        typecheck.is_enum(policy, raritan.rpc.security.RoleAccessPolicy, AssertionError)

        self.startIp = startIp
        self.endIp = endIp
        self.roleId = roleId
        self.policy = policy

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            startIp = json['startIp'],
            endIp = json['endIp'],
            roleId = json['roleId'],
            policy = raritan.rpc.security.RoleAccessPolicy.decode(json['policy']),
        )
        return obj

    def encode(self):
        json = {}
        json['startIp'] = self.startIp
        json['endIp'] = self.endIp
        json['roleId'] = self.roleId
        json['policy'] = raritan.rpc.security.RoleAccessPolicy.encode(self.policy)
        return json

# structure
class RoleAccessControl(Structure):
    idlType = "security.RoleAccessControl:1.0.0"
    elements = ["enabled", "defaultPolicy", "rules"]

    def __init__(self, enabled, defaultPolicy, rules):
        typecheck.is_bool(enabled, AssertionError)
        typecheck.is_enum(defaultPolicy, raritan.rpc.security.RoleAccessPolicy, AssertionError)
        for x0 in rules:
            typecheck.is_struct(x0, raritan.rpc.security.RoleAccessRule, AssertionError)

        self.enabled = enabled
        self.defaultPolicy = defaultPolicy
        self.rules = rules

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            enabled = json['enabled'],
            defaultPolicy = raritan.rpc.security.RoleAccessPolicy.decode(json['defaultPolicy']),
            rules = [raritan.rpc.security.RoleAccessRule.decode(x0, agent) for x0 in json['rules']],
        )
        return obj

    def encode(self):
        json = {}
        json['enabled'] = self.enabled
        json['defaultPolicy'] = raritan.rpc.security.RoleAccessPolicy.encode(self.defaultPolicy)
        json['rules'] = [raritan.rpc.security.RoleAccessRule.encode(x0) for x0 in self.rules]
        return json

# structure
class PasswordSettings(Structure):
    idlType = "security.PasswordSettings:1.0.0"
    elements = ["enableAging", "agingInterval", "enableStrongReq", "minPwLength", "maxPwLength", "enforceLower", "enforceUpper", "enforceNumeric", "enforceSpecial", "pwHistoryDepth"]

    def __init__(self, enableAging, agingInterval, enableStrongReq, minPwLength, maxPwLength, enforceLower, enforceUpper, enforceNumeric, enforceSpecial, pwHistoryDepth):
        typecheck.is_bool(enableAging, AssertionError)
        typecheck.is_int(agingInterval, AssertionError)
        typecheck.is_bool(enableStrongReq, AssertionError)
        typecheck.is_int(minPwLength, AssertionError)
        typecheck.is_int(maxPwLength, AssertionError)
        typecheck.is_bool(enforceLower, AssertionError)
        typecheck.is_bool(enforceUpper, AssertionError)
        typecheck.is_bool(enforceNumeric, AssertionError)
        typecheck.is_bool(enforceSpecial, AssertionError)
        typecheck.is_int(pwHistoryDepth, AssertionError)

        self.enableAging = enableAging
        self.agingInterval = agingInterval
        self.enableStrongReq = enableStrongReq
        self.minPwLength = minPwLength
        self.maxPwLength = maxPwLength
        self.enforceLower = enforceLower
        self.enforceUpper = enforceUpper
        self.enforceNumeric = enforceNumeric
        self.enforceSpecial = enforceSpecial
        self.pwHistoryDepth = pwHistoryDepth

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            enableAging = json['enableAging'],
            agingInterval = json['agingInterval'],
            enableStrongReq = json['enableStrongReq'],
            minPwLength = json['minPwLength'],
            maxPwLength = json['maxPwLength'],
            enforceLower = json['enforceLower'],
            enforceUpper = json['enforceUpper'],
            enforceNumeric = json['enforceNumeric'],
            enforceSpecial = json['enforceSpecial'],
            pwHistoryDepth = json['pwHistoryDepth'],
        )
        return obj

    def encode(self):
        json = {}
        json['enableAging'] = self.enableAging
        json['agingInterval'] = self.agingInterval
        json['enableStrongReq'] = self.enableStrongReq
        json['minPwLength'] = self.minPwLength
        json['maxPwLength'] = self.maxPwLength
        json['enforceLower'] = self.enforceLower
        json['enforceUpper'] = self.enforceUpper
        json['enforceNumeric'] = self.enforceNumeric
        json['enforceSpecial'] = self.enforceSpecial
        json['pwHistoryDepth'] = self.pwHistoryDepth
        return json

# structure
class SSHSettings(Structure):
    idlType = "security.SSHSettings:1.0.0"
    elements = ["allowPasswordAuth", "allowPublicKeyAuth"]

    def __init__(self, allowPasswordAuth, allowPublicKeyAuth):
        typecheck.is_bool(allowPasswordAuth, AssertionError)
        typecheck.is_bool(allowPublicKeyAuth, AssertionError)

        self.allowPasswordAuth = allowPasswordAuth
        self.allowPublicKeyAuth = allowPublicKeyAuth

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            allowPasswordAuth = json['allowPasswordAuth'],
            allowPublicKeyAuth = json['allowPublicKeyAuth'],
        )
        return obj

    def encode(self):
        json = {}
        json['allowPasswordAuth'] = self.allowPasswordAuth
        json['allowPublicKeyAuth'] = self.allowPublicKeyAuth
        return json

# structure
class RestrictedServiceAgreement(Structure):
    idlType = "security.RestrictedServiceAgreement:1.0.0"
    elements = ["enabled", "banner"]

    def __init__(self, enabled, banner):
        typecheck.is_bool(enabled, AssertionError)
        typecheck.is_string(banner, AssertionError)

        self.enabled = enabled
        self.banner = banner

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            enabled = json['enabled'],
            banner = json['banner'],
        )
        return obj

    def encode(self):
        json = {}
        json['enabled'] = self.enabled
        json['banner'] = self.banner
        return json

# value object
class PasswordSettingsChanged(raritan.rpc.event.UserEvent):
    idlType = "security.PasswordSettingsChanged:1.0.0"

    def __init__(self, oldSettings, newSettings, actUserName, actIpAddr, source):
        super(raritan.rpc.security.PasswordSettingsChanged, self).__init__(actUserName, actIpAddr, source)
        typecheck.is_struct(oldSettings, raritan.rpc.security.PasswordSettings, AssertionError)
        typecheck.is_struct(newSettings, raritan.rpc.security.PasswordSettings, AssertionError)

        self.oldSettings = oldSettings
        self.newSettings = newSettings

    def encode(self):
        json = super(raritan.rpc.security.PasswordSettingsChanged, self).encode()
        json['oldSettings'] = raritan.rpc.security.PasswordSettings.encode(self.oldSettings)
        json['newSettings'] = raritan.rpc.security.PasswordSettings.encode(self.newSettings)
        return json

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            oldSettings = raritan.rpc.security.PasswordSettings.decode(json['oldSettings'], agent),
            newSettings = raritan.rpc.security.PasswordSettings.decode(json['newSettings'], agent),
            # for event.UserEvent
            actUserName = json['actUserName'],
            actIpAddr = json['actIpAddr'],
            # for idl.Event
            source = Interface.decode(json['source'], agent),
        )
        return obj

    def listElements(self):
        elements = ["oldSettings", "newSettings"]
        elements = elements + super(raritan.rpc.security.PasswordSettingsChanged, self).listElements()
        return elements

# interface
class Security(Interface):
    idlType = "security.Security:3.0.0"

    ERR_INVALID_VALUE = 1

    # structure
    class Settings(Structure):
        idlType = "security.Security.Settings:1.0.0"
        elements = ["http2httpsRedir", "userBlockTimeout", "userMaxFailedLogins", "ipFw", "ipV6Fw", "roleAccessControl", "roleAccessControlV6", "pwSettings", "idleTimeout", "singleLogin", "sshSettings"]

        def __init__(self, http2httpsRedir, userBlockTimeout, userMaxFailedLogins, ipFw, ipV6Fw, roleAccessControl, roleAccessControlV6, pwSettings, idleTimeout, singleLogin, sshSettings):
            typecheck.is_bool(http2httpsRedir, AssertionError)
            typecheck.is_int(userBlockTimeout, AssertionError)
            typecheck.is_int(userMaxFailedLogins, AssertionError)
            typecheck.is_struct(ipFw, raritan.rpc.security.IpFw, AssertionError)
            typecheck.is_struct(ipV6Fw, raritan.rpc.security.IpFw, AssertionError)
            typecheck.is_struct(roleAccessControl, raritan.rpc.security.RoleAccessControl, AssertionError)
            typecheck.is_struct(roleAccessControlV6, raritan.rpc.security.RoleAccessControl, AssertionError)
            typecheck.is_struct(pwSettings, raritan.rpc.security.PasswordSettings, AssertionError)
            typecheck.is_int(idleTimeout, AssertionError)
            typecheck.is_bool(singleLogin, AssertionError)
            typecheck.is_struct(sshSettings, raritan.rpc.security.SSHSettings, AssertionError)

            self.http2httpsRedir = http2httpsRedir
            self.userBlockTimeout = userBlockTimeout
            self.userMaxFailedLogins = userMaxFailedLogins
            self.ipFw = ipFw
            self.ipV6Fw = ipV6Fw
            self.roleAccessControl = roleAccessControl
            self.roleAccessControlV6 = roleAccessControlV6
            self.pwSettings = pwSettings
            self.idleTimeout = idleTimeout
            self.singleLogin = singleLogin
            self.sshSettings = sshSettings

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                http2httpsRedir = json['http2httpsRedir'],
                userBlockTimeout = json['userBlockTimeout'],
                userMaxFailedLogins = json['userMaxFailedLogins'],
                ipFw = raritan.rpc.security.IpFw.decode(json['ipFw'], agent),
                ipV6Fw = raritan.rpc.security.IpFw.decode(json['ipV6Fw'], agent),
                roleAccessControl = raritan.rpc.security.RoleAccessControl.decode(json['roleAccessControl'], agent),
                roleAccessControlV6 = raritan.rpc.security.RoleAccessControl.decode(json['roleAccessControlV6'], agent),
                pwSettings = raritan.rpc.security.PasswordSettings.decode(json['pwSettings'], agent),
                idleTimeout = json['idleTimeout'],
                singleLogin = json['singleLogin'],
                sshSettings = raritan.rpc.security.SSHSettings.decode(json['sshSettings'], agent),
            )
            return obj

        def encode(self):
            json = {}
            json['http2httpsRedir'] = self.http2httpsRedir
            json['userBlockTimeout'] = self.userBlockTimeout
            json['userMaxFailedLogins'] = self.userMaxFailedLogins
            json['ipFw'] = raritan.rpc.security.IpFw.encode(self.ipFw)
            json['ipV6Fw'] = raritan.rpc.security.IpFw.encode(self.ipV6Fw)
            json['roleAccessControl'] = raritan.rpc.security.RoleAccessControl.encode(self.roleAccessControl)
            json['roleAccessControlV6'] = raritan.rpc.security.RoleAccessControl.encode(self.roleAccessControlV6)
            json['pwSettings'] = raritan.rpc.security.PasswordSettings.encode(self.pwSettings)
            json['idleTimeout'] = self.idleTimeout
            json['singleLogin'] = self.singleLogin
            json['sshSettings'] = raritan.rpc.security.SSHSettings.encode(self.sshSettings)
            return json

    def getSettings(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'getSettings', args)
        _ret_ = raritan.rpc.security.Security.Settings.decode(rsp['_ret_'], agent)
        typecheck.is_struct(_ret_, raritan.rpc.security.Security.Settings, DecodeException)
        return _ret_

    def setSettings(self, settings):
        agent = self.agent
        typecheck.is_struct(settings, raritan.rpc.security.Security.Settings, AssertionError)
        args = {}
        args['settings'] = raritan.rpc.security.Security.Settings.encode(settings)
        rsp = agent.json_rpc(self.target, 'setSettings', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def setHttpRedirSettings(self, http2httpsRedir):
        agent = self.agent
        typecheck.is_bool(http2httpsRedir, AssertionError)
        args = {}
        args['http2httpsRedir'] = http2httpsRedir
        rsp = agent.json_rpc(self.target, 'setHttpRedirSettings', args)

    def setIpFwSettings(self, ipFw):
        agent = self.agent
        typecheck.is_struct(ipFw, raritan.rpc.security.IpFw, AssertionError)
        args = {}
        args['ipFw'] = raritan.rpc.security.IpFw.encode(ipFw)
        rsp = agent.json_rpc(self.target, 'setIpFwSettings', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def setIpV6FwSettings(self, ipV6Fw):
        agent = self.agent
        typecheck.is_struct(ipV6Fw, raritan.rpc.security.IpFw, AssertionError)
        args = {}
        args['ipV6Fw'] = raritan.rpc.security.IpFw.encode(ipV6Fw)
        rsp = agent.json_rpc(self.target, 'setIpV6FwSettings', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def setRoleAccessControlSettings(self, settings):
        agent = self.agent
        typecheck.is_struct(settings, raritan.rpc.security.RoleAccessControl, AssertionError)
        args = {}
        args['settings'] = raritan.rpc.security.RoleAccessControl.encode(settings)
        rsp = agent.json_rpc(self.target, 'setRoleAccessControlSettings', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def setRoleAccessControlSettingsV6(self, settings):
        agent = self.agent
        typecheck.is_struct(settings, raritan.rpc.security.RoleAccessControl, AssertionError)
        args = {}
        args['settings'] = raritan.rpc.security.RoleAccessControl.encode(settings)
        rsp = agent.json_rpc(self.target, 'setRoleAccessControlSettingsV6', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def setBlockSettings(self, blockTimeout, maxFailedLogins):
        agent = self.agent
        typecheck.is_int(blockTimeout, AssertionError)
        typecheck.is_int(maxFailedLogins, AssertionError)
        args = {}
        args['blockTimeout'] = blockTimeout
        args['maxFailedLogins'] = maxFailedLogins
        rsp = agent.json_rpc(self.target, 'setBlockSettings', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def setPwSettings(self, pwSettings):
        agent = self.agent
        typecheck.is_struct(pwSettings, raritan.rpc.security.PasswordSettings, AssertionError)
        args = {}
        args['pwSettings'] = raritan.rpc.security.PasswordSettings.encode(pwSettings)
        rsp = agent.json_rpc(self.target, 'setPwSettings', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def setIdleTimeoutSettings(self, idleTimeout):
        agent = self.agent
        typecheck.is_int(idleTimeout, AssertionError)
        args = {}
        args['idleTimeout'] = idleTimeout
        rsp = agent.json_rpc(self.target, 'setIdleTimeoutSettings', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def setSingleLoginLimitation(self, singleLogin):
        agent = self.agent
        typecheck.is_bool(singleLogin, AssertionError)
        args = {}
        args['singleLogin'] = singleLogin
        rsp = agent.json_rpc(self.target, 'setSingleLoginLimitation', args)

    def getIdleTimeoutSettings(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'getIdleTimeoutSettings', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def getHttpRedirSettings(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'getHttpRedirSettings', args)
        _ret_ = rsp['_ret_']
        typecheck.is_bool(_ret_, DecodeException)
        return _ret_

    def getBlockSettings(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'getBlockSettings', args)
        blockTimeout = rsp['blockTimeout']
        maxFailedLogins = rsp['maxFailedLogins']
        typecheck.is_int(blockTimeout, DecodeException)
        typecheck.is_int(maxFailedLogins, DecodeException)
        return (blockTimeout, maxFailedLogins)

    def getSSHSettings(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'getSSHSettings', args)
        _ret_ = raritan.rpc.security.SSHSettings.decode(rsp['_ret_'], agent)
        typecheck.is_struct(_ret_, raritan.rpc.security.SSHSettings, DecodeException)
        return _ret_

    def setSSHSettings(self, settings):
        agent = self.agent
        typecheck.is_struct(settings, raritan.rpc.security.SSHSettings, AssertionError)
        args = {}
        args['settings'] = raritan.rpc.security.SSHSettings.encode(settings)
        rsp = agent.json_rpc(self.target, 'setSSHSettings', args)

    def getRestrictedServiceAgreement(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'getRestrictedServiceAgreement', args)
        _ret_ = raritan.rpc.security.RestrictedServiceAgreement.decode(rsp['_ret_'], agent)
        typecheck.is_struct(_ret_, raritan.rpc.security.RestrictedServiceAgreement, DecodeException)
        return _ret_

    def setRestrictedServiceAgreement(self, settings):
        agent = self.agent
        typecheck.is_struct(settings, raritan.rpc.security.RestrictedServiceAgreement, AssertionError)
        args = {}
        args['settings'] = raritan.rpc.security.RestrictedServiceAgreement.encode(settings)
        rsp = agent.json_rpc(self.target, 'setRestrictedServiceAgreement', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def getSupportedFrontPanelPrivileges(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'getSupportedFrontPanelPrivileges', args)
        _ret_ = [x0 for x0 in rsp['_ret_']]
        for x0 in _ret_:
            typecheck.is_string(x0, DecodeException)
        return _ret_

    def setFrontPanelPrivileges(self, privileges):
        agent = self.agent
        for x0 in privileges:
            typecheck.is_string(x0, AssertionError)
        args = {}
        args['privileges'] = [x0 for x0 in privileges]
        rsp = agent.json_rpc(self.target, 'setFrontPanelPrivileges', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def getFrontPanelPrivileges(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'getFrontPanelPrivileges', args)
        _ret_ = [x0 for x0 in rsp['_ret_']]
        for x0 in _ret_:
            typecheck.is_string(x0, DecodeException)
        return _ret_
# Do NOT edit this file!
# It was generated by IdlC class idl.json.python.ProxyAsnVisitor.

#
# Section generated from "/home/nb/builds/MEGA/px2-3.1.x-branch-20150209-none-release-none-pdu-raritan/fwcomponents/mkdist/tmp/px2_final/libisys/src/idl/ServiceAuthorization.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException

# interface
class ServiceAuthorization(Interface):
    idlType = "security.ServiceAuthorization:1.0.0"

    ERR_PASSWORD_INVALID = 1

    def setPassword(self, service, password):
        agent = self.agent
        typecheck.is_string(service, AssertionError)
        typecheck.is_string(password, AssertionError)
        args = {}
        args['service'] = service
        args['password'] = password
        rsp = agent.json_rpc(self.target, 'setPassword', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_
