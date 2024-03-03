import sys
sys.path.append('./Utilitarios/packets')

import login
import location
import heartbeat
import replied_by_device
import send_by_server
import iccid
import alarm

def parse_hex_string_translated(hex_string):
    hex_string = hex_string.lower().replace(" ", "")
    if len(hex_string) % 2 != 0:
        raise ValueError("Hexadecimal string must have an even number of digits.")

    byte_array = bytearray.fromhex(hex_string)
    protocol_number = byte_array[3]

    # Login Packet
    if protocol_number == 0x01:
        parse_packet = login.login_packet(byte_array)
        return parse_packet

    # Heartbeat Packet
    elif protocol_number == 0x13:
        parse_packet = heartbeat.heartbeat_packet(byte_array)
        return parse_packet

    # Packet Replied by Device
    elif protocol_number == 0x15:
        parse_packet = replied_by_device.replied_by_device(byte_array)
        return parse_packet
    
    # Alarm Packet
    elif protocol_number == 0x16:
        parse_packet = alarm.alarm_packet(byte_array)
        return parse_packet
    
    # Location Data Packet
    elif protocol_number == 0x17:
        parse_packet = location.location_packet(byte_array)
        return parse_packet
    
    # Packet send by Server
    elif protocol_number == 0x80:
        parse_packet = send_by_server.send_by_server(byte_array)
        return parse_packet

    # ICCID Packet
    elif protocol_number == 0x94:
        parse_packet = iccid.iccid_packet(byte_array)
        return parse_packet

    else:
        raise ValueError("Unknown packet. Supports only packets 0x01, 0x13, 0x15, 0x16, 0x17, 0x80, and 0x94.")
