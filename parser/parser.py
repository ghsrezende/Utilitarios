from packets.login import parse_login_packet
from packets.login import translated_login_packet
from packets.heartbeat import parse_heartbeat_packet
from packets.heartbeat import translated_heartbeat_packet
from packets.heartbeat_gt06 import parse_heartbeat_packet_gt06
from packets.heartbeat_gt06 import translated_heartbeat_packet_gt06
from packets.alarm import parse_alarm_packet
from packets.alarm import translated_alarm_packet
from packets.alarm_gt06 import parse_alarm_packet_gt06
from packets.alarm_gt06 import translated_alarm_packet_gt06
from packets.location import parse_location_data_packet
from packets.location import translated_location_packet
from packets.location_gt06 import parse_location_data_packet_gt06_0X0A
from packets.location_gt06 import parse_location_data_packet_gt06_0x12
from packets.location_gt06 import parse_location_data_packet_gt06_0x22
from packets.location_gt06 import parse_location_data_packet_gt06_0x32
from packets.location_gt06 import translated_location_packet_gt06_0x0A
from packets.location_gt06 import translated_location_packet_gt06_0x12
from packets.location_gt06 import translated_location_packet_gt06_0x22
from packets.location_gt06 import translated_location_packet_gt06_0x32
from packets.status import parse_status_packet
from packets.status import translated_status_device_packet
from packets.iccid import parse_iccid_packet
from packets.iccid import translated_iccid_packet
from packets.replied_by_device import parse_packet_replied_by_device
from packets.replied_by_device import translated_replied_by_device
from packets.send_by_server import parse_packet_sent_by_server
from packets.send_by_server import translated_send_by_server
from .validation import validate_hex_string, validate_packet_length, validate_protocol
from .protocols import Protocols

def parse_hex_string_common(hex_string, packet_parsers):

    hex_string = validate_hex_string(hex_string)

    byte_array = bytearray.fromhex(hex_string)
    protocol_number = byte_array[3]
    valid_protocols = [protocol.value for protocol in Protocols]

    validate_protocol(byte_array, valid_protocols)

    parse_packet_func = packet_parsers.get(protocol_number)

    if parse_packet_func:
        return parse_packet_func(byte_array)

    raise ValueError(
        "Unknown packet type. Supported packet types are: 0x01, 0x12, 0x13, 0x15, 0x16, 0x17, 0x22, 0x32, 0x30, 0x80, 0x94 and 0x0A."
    )

def parse_hex_string(hex_string):
    packet_parsers = {
        0x01: parse_login_packet,
        0x13: parse_heartbeat_packet,
        0x15: parse_packet_replied_by_device,
        0x16: parse_alarm_packet,
        0x17: parse_location_data_packet,
        0x30: parse_status_packet,
        0x80: parse_packet_sent_by_server,
        0x94: parse_iccid_packet,
    }
    return parse_hex_string_common(hex_string, packet_parsers)

def parse_hex_string_gt06(hex_string):
    packet_parsers = {
        0x01: parse_login_packet,
        0x12: parse_location_data_packet_gt06_0x12,
        0x13: parse_heartbeat_packet_gt06,
        0x15: parse_packet_replied_by_device,
        0x16: parse_alarm_packet_gt06,  
        0x22: parse_location_data_packet_gt06_0x22,
        0x32: parse_location_data_packet_gt06_0x32,
        0x80: parse_packet_sent_by_server,
        0x94: parse_iccid_packet,
        0x0A: parse_location_data_packet_gt06_0X0A,
    }
    return parse_hex_string_common(hex_string, packet_parsers)

def parse_hex_string_translated(hex_string):

    packet_parsers = {
        0x01: translated_login_packet,
        0x13: translated_heartbeat_packet,
        0x15: translated_replied_by_device,
        0x16: translated_alarm_packet,
        0x17: translated_location_packet,
        0x30: translated_status_device_packet,
        0x80: translated_send_by_server,
        0x94: translated_iccid_packet,
    }
    return parse_hex_string_common(hex_string, packet_parsers)

def parse_hex_string_translated_gt06(hex_string):

    packet_parsers = {
        0x01: translated_login_packet,
        0x12: translated_location_packet_gt06_0x12,
        0x13: translated_heartbeat_packet_gt06,
        0x15: translated_replied_by_device,
        0x16: translated_alarm_packet_gt06,
        0x22: translated_location_packet_gt06_0x22,
        0x32: translated_location_packet_gt06_0x32,
        0x80: translated_send_by_server,
        0x94: translated_iccid_packet,
        0x0A: translated_location_packet_gt06_0x0A,
    }
    return parse_hex_string_common(hex_string, packet_parsers)
