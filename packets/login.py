def translated_login_packet(byte_array):
    parse_packet = {
        "Start Bit": byte_array[:2].hex(),
        "Packet Length": {
            "Value Hex": f"0x{byte_array[2]:02X}",
            "Value": int(f"0x{byte_array[2]:02X}", 16),
        },
        "Protocol Number": {
            "Value Hex": f"0x{byte_array[3]:02X}",
            "Value": "Login Packet",
        },
            "Device ID": byte_array[4:12].hex(),
            "Serial Number": {
            "Value Hex": f"0x{byte_array[12:14].hex()}",
            "Value": int(f"0x{byte_array[12:14].hex()}", 16),
        },
            "CRC": byte_array[14:16].hex(),
            "End Bit": byte_array[16:].hex()
    }
    return parse_packet


def parse_login_packet(byte_array):
    parse_packet = {
        "Start Bit": byte_array[:2].hex(),
        "Packet Length": f"0x{byte_array[2]:02X}",
        "Protocol Number": f"0x{byte_array[3]:02X}",
        "Device ID": byte_array[4:12].hex(),
        "Serial Number": byte_array[12:14].hex(),
        "CRC": byte_array[14:16].hex(),
        "End Bit": byte_array[16:].hex()
    }

    return parse_packet