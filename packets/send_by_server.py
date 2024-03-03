from util import hex_to_ascii

def send_by_server(byte_array):
    
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