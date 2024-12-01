from utils.util import (
    device_information, language, battery_voltage_level, alarm_type_gtklite
)

def translated_heartbeat_packet_gt06(byte_array):
    parse_packet = {
        "Start Bit": byte_array[:2].hex(),
        "Packet Length": {
            "Value Hex": f"0x{byte_array[2]:02X}",
            "Value": int(f"0x{byte_array[2]:02X}", 16),
        },
        "Protocol Number": {
            "Value Hex": f"0x{byte_array[3]:02X}",
            "Value": "Heartbeat Packet",
        },
        "Status Information": {
            "Device Information": device_information(byte_array[4]),
            "Battery Voltage Level": battery_voltage_level(f"0x{byte_array[5]:02X}"),
            "GSM Signal": {
                "Value Hex": f"0x{byte_array[6]:02X}",
                "Value": int(f"0x{byte_array[6]:02X}", 16),
            },
            "Alarm": {
                "Value Hex": f"0x{byte_array[7]:02X}",
                "Value": alarm_type_gtklite(f"0x{byte_array[7]:02X}"),
            },
            "Language": {
                "Description": language(byte_array[8]),
                "Value Hex": f"0x{byte_array[8]:02X}",
            },
        },
        "Serial Number": {
            "Value Hex": f"0x{byte_array[9:11].hex()}",
            "Value": int(f"0x{byte_array[9:11].hex()}", 16),
        },
        "CRC": byte_array[11:13].hex(),
        "End Bit": byte_array[13:].hex(),
    }

    return parse_packet

def parse_heartbeat_packet_gt06(byte_array):

    parse_packet = {
        "Start Bit": byte_array[:2].hex(),
        "Packet Length": f"0x{byte_array[2]:02X}",
        "Protocol Number": f"0x{byte_array[3]:02X}",
        "Status Information": {
            "Device Information": f"0x{byte_array[4]:02X}",
            "Battery Voltage Level": f"0x{byte_array[5]:02X}",
            "GSM Signal": f"0x{byte_array[6]:02X}",
            "Alarm": f"0x{byte_array[7]:02X}",
            "Language": f"0x{byte_array[8]:02X}",
        },
        "Serial Number": byte_array[9:11].hex(),
        "CRC": byte_array[11:13].hex(),
        "End Bit": byte_array[13:].hex()
    }

    return parse_packet