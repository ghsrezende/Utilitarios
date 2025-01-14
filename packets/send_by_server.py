from utils.util import hex_to_ascii

def translated_send_by_server(byte_array):
    
    i = int(f"0x{byte_array[4]:02X}", 16)
    j = i - 4
    
    parse_packet = {
        "Start Bit": byte_array[:2].hex(),
        "Packet Length": {
            "Value Hex": f"0x{byte_array[2]:02X}",
            "Value": int(f"0x{byte_array[2]:02X}", 16),
        },
        "Protocol Number": {
            "Value Hex": f"0x{byte_array[3]:02X}",
            "Value": "Send by Server Packet",
        },
        "Lenght of Command": {
            "Value Hex": f"0x{byte_array[4]:02X}",
            "Value": int(f"0x{byte_array[4]:02X}", 16),
        },
        "Server Flag Bit": {
                "Value Hex": f"0x{byte_array[5:9].hex()}",
                "Value": int(f"0x{byte_array[5:9].hex()}",16),
            },
        "Command Content": {
                "Value Hex": byte_array[9:j+9].hex(),
                "Command Sent": hex_to_ascii(byte_array[9:j+9]),
            },
        "Serial Number": {
                "Value Hex": f"0x{byte_array[j+9:j+11].hex()}",
                "Value": int(f"0x{byte_array[j+9:j+11].hex()}", 16),
            },
        "CRC": byte_array[j+11:j+13].hex(),
        "End Bit": byte_array[j+13:].hex(),
    }
    return parse_packet

def parse_packet_sent_by_server(byte_array):
    i = int(f"0x{byte_array[4]:02X}", 16)
    j = i - 4

    parse_packet = {
        "Start Bit": byte_array[:2].hex(),
        "Packet Length": f"0x{byte_array[2]:02X}",
        "Protocol Number": f"0x{byte_array[3]:02X}",
        "Length of Command": f"0x{byte_array[4]:02X}",
        "Server Flag Bit": byte_array[5:9].hex(),
        "Command Content": byte_array[9:j+9].hex(),
        "Serial Number": byte_array[j+9:j+11].hex(),
        "CRC": byte_array[j+11:j+13].hex(),
        "End Bit": byte_array[j+13:].hex(),
    }

    return parse_packet