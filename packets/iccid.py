def iccid_packet(byte_array):
    parse_packet = {
        "Start Bit": byte_array[:2].hex(),
        "Packet Length": f"0x{byte_array[2]:02X}",
        "Protocol Number": f"0x{byte_array[3]}",
        "FLAG": f"0x{byte_array[5]:02X}",
        "IMEI":byte_array[6:14].hex(),
        "IMSI":byte_array[14:22].hex(),
        "ICCID":byte_array[22:32].hex(),
        "Serial Number": byte_array[32:34].hex(),
        "CRC": byte_array[34:36].hex(),
        "End Bit": byte_array[36:].hex(),
    }
    return parse_packet