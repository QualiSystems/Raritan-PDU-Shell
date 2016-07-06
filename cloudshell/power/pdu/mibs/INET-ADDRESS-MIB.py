#
# PySNMP MIB module INET-ADDRESS-MIB (http://pysnmp.sf.net)
# ASN.1 source file://\Users\nahum-t\Documents\libsmi-0.4.3-win32\smi\mibs\ietf\INET-ADDRESS-MIB
# Produced by pysmi-0.0.6 at Tue Jun 28 18:47:55 2016
# On host ? platform ? version ? by user ?
# Using Python version 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)]
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, mib_2, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "mib-2", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
inetAddressMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 76)).setRevisions(("2002-05-09 00:00", "2000-06-08 00:00",))
class InetAddressType(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+SingleValueConstraint(0, 1, 2, 3, 4, 16,)
    namedValues = NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2), ("ipv4z", 3), ("ipv6z", 4), ("dns", 16),)

class InetAddress(OctetString, TextualConvention):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)

class InetAddressIPv4(OctetString, TextualConvention):
    displayHint = '1d.1d.1d.1d'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(4,4)
    fixedLength = 4

class InetAddressIPv6(OctetString, TextualConvention):
    displayHint = '2x:2x:2x:2x:2x:2x:2x:2x'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(16,16)
    fixedLength = 16

class InetAddressIPv4z(OctetString, TextualConvention):
    displayHint = '1d.1d.1d.1d%4d'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(8,8)
    fixedLength = 8

class InetAddressIPv6z(OctetString, TextualConvention):
    displayHint = '2x:2x:2x:2x:2x:2x:2x:2x%4d'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(20,20)
    fixedLength = 20

class InetAddressDNS(OctetString, TextualConvention):
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,255)

class InetAddressPrefixLength(Unsigned32, TextualConvention):
    pass

class InetPortNumber(Unsigned32, TextualConvention):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,65535)

class InetAutonomousSystemNumber(Unsigned32, TextualConvention):
    pass

mibBuilder.exportSymbols("INET-ADDRESS-MIB", InetAddressPrefixLength=InetAddressPrefixLength, InetAddressIPv4=InetAddressIPv4, InetAddressIPv6z=InetAddressIPv6z, PYSNMP_MODULE_ID=inetAddressMIB, InetAddressIPv6=InetAddressIPv6, InetAddressDNS=InetAddressDNS, InetPortNumber=InetPortNumber, InetAddress=InetAddress, inetAddressMIB=inetAddressMIB, InetAutonomousSystemNumber=InetAutonomousSystemNumber, InetAddressType=InetAddressType, InetAddressIPv4z=InetAddressIPv4z)
