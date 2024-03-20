from util import battery_voltage, bytes_to_latitude, bytes_to_longitude, external_voltage, device_information, timestamp, horimeter, course_status, alarm_type, language, gps_information, battery_voltage_level

def alarm_packet(byte_array):
    parse_packet = {
        "Start Bit": byte_array[:2].hex(),
        "Packet Length": {
            "Value Hex": f"0x{byte_array[2]:02X}",
            "Value": int(f"0x{byte_array[2]:02X}", 16),
        },
        "Protocol Number": {
            "Value Hex": f"0x{byte_array[3]:02X}",
            "Value": "Alarm Packet",
        },
        "GPS information" : {   
            "Date Time": {
                "Value Hex": f"0x{byte_array[4:10].hex()}",
                "Value": timestamp(byte_array[4:10]),
            },
            "Number Satellites": {
                "Value Hex": f"0x{byte_array[10]:02X}",
                "GPS Information" : gps_information(f"0x{byte_array[10]:02X}"),
            },
            "Latitude": {
                "Value Hex": f"0x{byte_array[11:15].hex()}",
                "Value": bytes_to_latitude(byte_array[11:15]),
            },
            "Longitude": {
                "Value Hex": f"0x{byte_array[15:19].hex()}",
                "Value": bytes_to_longitude(byte_array[15:19]),
            },
            "Speed": {
                "Value Hex": f"0x{byte_array[19]:02X}",
                "Value": int(f"0x{byte_array[19]:02X}", 16),
            },
            "Course Status": course_status(byte_array[20:22]),
        },
        "LBS Information":  {            
            "LBS": {
                "Value Hex": f"0x{byte_array[22]:02X}",
                "Value": int(f"0x{byte_array[22]:02X}", 16),
            },
            "MCC": {
                "Value Hex": f"0x{byte_array[23:25].hex()}",
                "Value": int(f"0x{byte_array[23:25].hex()}", 16),
            },
            "MNC": {
                "Value Hex": f"0x{byte_array[25]:02X}",
                "Value": int(f"0x{byte_array[25]:02X}", 16),
            },
            "LAC": {
                "Value Hex": f"0x{byte_array[26:28].hex()}",
                "Value": int(f"0x{byte_array[26:28].hex()}", 16),
            },
            "Cell ID": {
                "Value Hex": f"0x{byte_array[28:31].hex()}",
                "Value": int(f"0x{byte_array[28:31].hex()}", 16),
            },
        },
        "Status Information": {
            "Device Information": device_information(byte_array[31]),
            "Battery Voltage Level": battery_voltage_level(f"0x{byte_array[32]:02X}"),
            "GSM Signal": {
                "Value Hex": f"0x{byte_array[33]:02X}",
                "Value": int(f"0x{byte_array[33]:02X}", 16),
            },
            "Alarm Packet": alarm_type(f"0x{byte_array[34]:02X}"),
            "Language": {
                "Description": language(byte_array[35]),
                "Value Hex": f"0x{byte_array[35]:02X}",
            },
            "Battery Voltage": {
                "Value Hex": f"0x{byte_array[36:38].hex()}",
                "Value": battery_voltage(byte_array[36:38]),
            },
            "External Voltage": {
                "Value Hex": f"0x{byte_array[38:40].hex()}",
                "Value": external_voltage(byte_array[38:40]),
            },
        },
        "Mileage": {
            "Value Hex": f"0x{byte_array[40:44].hex()}",
            "Value": int(f"0x{byte_array[40:44].hex()}", 16),
        },
        "Horimeter": {
            "Value Hex": f"0x{byte_array[44:48].hex()}",
            "Value": horimeter(byte_array[44:48]),
        },
        "Serial Number": {
            "Value Hex": f"0x{byte_array[48:50].hex()}",
            "Value": int(f"0x{byte_array[48:50].hex()}", 16),
        },
        "CRC": byte_array[50:52].hex(),
        "End Bit": byte_array[52:].hex(),
    }

    return parse_packet

    