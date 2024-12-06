def translated_iccid_packet(byte_array):

    parse_packet = {
        "Start Bit": byte_array[:2].hex(),
        "Packet Length": f"0x{byte_array[2]:02X}",
        "Protocol Number": f"0x{byte_array[3]}",
        "FLAG": f"0x{byte_array[4]:02X}",
        "IMEI":byte_array[5:13].hex(),
        "IMSI":byte_array[13:21].hex(),
        "ICCID":byte_array[21:31].hex(),
        "Serial Number": byte_array[31:33].hex(),
        "CRC": byte_array[33:35].hex(),
        "End Bit": byte_array[35:].hex(),
    }
    return parse_packet

def parse_iccid_packet(byte_array):

    parse_packet = {
        "Start Bit": byte_array[:2].hex(),
        "Packet Length": f"0x{byte_array[2]:02X}",
        "Protocol Number": f"0x{byte_array[3]:02X}",
        "FLAG": f"0x{byte_array[4]:02X}",
        "IMEI": byte_array[5:13].hex(),
        "IMSI": byte_array[13:21].hex(),
        "ICCID": byte_array[21:31].hex(),
        "Serial Number": byte_array[31:33].hex(),
        "CRC": byte_array[33:35].hex(),
        "End Bit": byte_array[35:].hex(),
    }

    return parse_packet