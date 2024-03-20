from util import device_information, language
def heartbeat_packet(byte_array):
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
            "Battery Voltage Level": {
                "Value Hex": f"0x{byte_array[5]:02X}",
                "Value": int(f"0x{byte_array[5]:02X}", 16),
            },
            "GSM Signal": {
                "Value Hex": f"0x{byte_array[6]:02X}",
                "Value": int(f"0x{byte_array[6]:02X}", 16),
            },
            "External Voltage": {
                "Value Hex": f"0x{byte_array[7]:02X}",
                "Value": int(f"0x{byte_array[7]:02X}", 16),
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