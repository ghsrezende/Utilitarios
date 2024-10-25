from util import battery_voltage, bytes_to_latitude, bytes_to_longitude, external_voltage, device_information, timestamp, horimeter, course_status, gps_information, battery_voltage_level, hex_to_ascii

def status_device_packet(byte_array):
    if len(byte_array) < 174:
        raise ValueError(f"O array de bytes está incompleto. Tamanho atual: {len(byte_array)} bytes")

    parse_packet = {
        "Start Bit": byte_array[:2].hex(),
        "Packet Length": {
            "Value Hex": f"0x{byte_array[2]:02X}",
            "Value": int(f"0x{byte_array[2]:02X}", 16),
        },
        "Protocol Number": {
            "Value Hex": f"0x{byte_array[3]:02X}",
            "Value": "Location Data Packet",
        },
        "Device ID": byte_array[4:12].hex(),
        "GPS information": {
            "Date Time": {
                "Value Hex": f"0x{byte_array[12:18].hex()}",
                "Value": timestamp(byte_array[12:18]),
            },
            "Number Satellites": {
                "Value Hex": f"0x{byte_array[18]:02X}",
                "GPS Information": gps_information(f"0x{byte_array[18]:02X}"),
            },
            "Latitude": {
                "Value Hex": f"0x{byte_array[19:23].hex()}",
                "Value": bytes_to_latitude(byte_array[19:23]),
            },
            "Longitude": {
                "Value Hex": f"0x{byte_array[23:27].hex()}",
                "Value": bytes_to_longitude(byte_array[23:27]),
            },
            "Speed": {
                "Value Hex": f"0x{byte_array[27]:02X}",
                "Value": int(f"0x{byte_array[27]:02X}", 16),
            },
            "Course Status": course_status(byte_array[28:30]),
        },
        "Status Information": {
            "Device Information": device_information(byte_array[30]),
            "Battery Voltage Level": battery_voltage_level(f"0x{byte_array[31]:02X}"),
            "GSM Signal": {
                "Value Hex": f"0x{byte_array[32]:02X}",
                "Value": int(f"0x{byte_array[32]:02X}", 16),
            },
            "Battery Voltage": {
                "Value Hex": f"0x{byte_array[33:35].hex()}",
                "Value": battery_voltage(byte_array[33:35]),
            },
            "External Voltage": {
                "Value Hex": f"0x{byte_array[35:37].hex()}",
                "Value": external_voltage(byte_array[35:37]),
            },
        },
        "Mileage": {
            "Value Hex": f"0x{byte_array[37:41].hex()}",
            "Value": int(f"0x{byte_array[37:41].hex()}", 16),
        },
        "Horimeter": {
            "Value Hex": f"0x{byte_array[41:45].hex()}",
            "Value": horimeter(byte_array[41:45]),
        },
        "Connection Mode": {
            "Value Hex": f"0x{byte_array[45]:02X}",
            "Value": int(f"0x{byte_array[45]:02X}", 16),
        },
        "Resets Count": {
            "Value Hex": f"0x{byte_array[46:48].hex()}",
            "Value": int(f"0x{byte_array[46:48].hex()}", 16),
        },
        "ICCID": {
            "Value Hex": f"0x{byte_array[48:58].hex()}",
            "Value": hex_to_ascii(byte_array[48:58]),
        },
        "MAIN SERVER": {
            "Value Hex": f"0x{byte_array[58:93].hex()}",
            "Value": hex_to_ascii(byte_array[58:93]),
        },
        "APN": {
            "Value Hex": f"0x{byte_array[93:128].hex()}",
            "Value": hex_to_ascii(byte_array[93:128]),
        },
        "HW Version": {
            "Value Hex": f"0x{byte_array[128:148].hex()}",
            "Value": hex_to_ascii(byte_array[128:148]),
        },
        "SW Version": {
            "Value Hex": f"0x{byte_array[148:168].hex()}",
            "Value": hex_to_ascii(byte_array[148:168]),
        },
        "Serial Number": {
            "Value Hex": f"0x{byte_array[168:170].hex()}",
            "Value": int(f"0x{byte_array[168:170].hex()}", 16)
        },
        "CRC": byte_array[170:172].hex(),
        "End Bit": byte_array[172:].hex(),
    }

    return parse_packet
