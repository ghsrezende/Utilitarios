import sys
sys.path.append('./packets')

import login
import location
import heartbeat
import replied_by_device
import send_by_server
import iccid
import alarm
import status

def parse_hex_string_translated(hex_string):
    hex_string = hex_string.lower().replace(" ", "")
    if len(hex_string) % 2 != 0:
        raise ValueError("Hexadecimal string must have an even number of digits.")

    byte_array = bytearray.fromhex(hex_string)
    protocol_number = byte_array[3]

    # Seleciona a função correta com base no protocolo
    packet_parsers = {
        0x01: login.login_packet,
        0x13: heartbeat.heartbeat_packet,
        0x15: replied_by_device.replied_by_device,
        0x16: alarm.alarm_packet,
        0x17: location.location_packet,
        0x30: status.status_device_packet,
        0x80: send_by_server.send_by_server,
        0x94: iccid.iccid_packet,
    }

    # Obtém a função correta do dicionário
    parse_packet_func = packet_parsers.get(protocol_number)
    if parse_packet_func:
        return parse_packet_func(byte_array)
    
    raise ValueError(
        "Unknown packet type. Supported packet types are: 0x01, 0x13, 0x15, 0x16, 0x17, 0x30, 0x80, and 0x94."
    )
