def parse_hex_string(hex_string):
    hex_string = hex_string.lower().replace(" ", "")
    if len(hex_string) % 2 != 0:
        raise ValueError("Hexadecimal string must have an even number of digits.")

    byte_array = bytearray.fromhex(hex_string)
    protocol_number = byte_array[3]

    common_fields = {
        "Start Bit": byte_array[:2].hex(),
        "Packet Length": f"0x{byte_array[2]:02X}",
        "Protocol Number": f"0x{protocol_number:02X}",
    }

    specific_fields = {}

    # Login Packet
    if protocol_number == 0x01:
        specific_fields = {
            "Device ID": byte_array[4:12].hex(),
            "Serial Number": byte_array[12:14].hex(),
            "CRC": byte_array[14:16].hex(),
            "End Bit": byte_array[16:].hex()
        }

    # Heartbeat Packet
    elif protocol_number == 0x13:
        specific_fields = {
            "Status Information": {
                "Device Information": f"0x{byte_array[4]:02X}",
                "Battery Voltage Level": f"0x{byte_array[5]:02X}",
                "GSM Signal": f"0x{byte_array[6]:02X}",
                "External Voltage": f"0x{byte_array[7]:02X}",
                "Language": f"0x{byte_array[8]:02X}",
            },
            "Serial Number": byte_array[9:11].hex(),
            "CRC": byte_array[11:13].hex(),
            "End Bit": byte_array[13:].hex()
        }

    # Packet Replied by Device
    elif protocol_number == 0x15:

        i = int(f"0x{byte_array[4]:02X}", 16)
        j = i - 4

        specific_fields = {
            "Lenght of Command": f"0x{byte_array[4]:02X}",
            "Server Flag Bit": byte_array[5:9].hex(),
            "Command Content": byte_array[9:j+9].hex(),
            "Reserved": byte_array[j+9:j+11].hex(),
            "Serial Number": byte_array[j+11:j+13].hex(),
            "CRC": byte_array[j+13:j+15].hex(),
            "End Bit": byte_array[j+15:].hex()
        }
    
    # Alarm Packet
    elif protocol_number == 0x16:
        specific_fields = {
            "GPS information" : {   
                "Date Time": byte_array[4:10].hex(),
                "Number Satellites": f"0x{byte_array[10]:02X}",
                "Latitude": byte_array[11:15].hex(),
                "Longitude": byte_array[15:19].hex(),
                "Speed": f"0x{byte_array[19]:02X}",
                "Course Status": byte_array[20:22].hex()
            },
            "LBS Information":  {            
                "LBS": f"0x{byte_array[22]:02X}",
                "MCC": byte_array[23:25].hex(),
                "MNC": f"0x{byte_array[25]:02X}",
                "LAC": byte_array[26:28].hex(),
                "Cell ID": byte_array[28:31].hex()
            },
            "Status Information": {
                "Device Information": f"0x{byte_array[31]:02X}",
                "Battery Voltage Level": f"0x{byte_array[32]:02X}",
                "GSM Signal": f"0x{byte_array[33]:02X}",
                "Alarm Packet": f"0x{byte_array[34]:02X}",
                "Language": f"0x{byte_array[35]:02X}",
                "Battery Voltage": byte_array[36:38].hex(),
                "External Voltage": byte_array[38:40].hex()
            },
            "Mileage": byte_array[40:44].hex(),
            "Horimeter": byte_array[44:48].hex(),
            "Serial Number": byte_array[48:50].hex(),
            "CRC": byte_array[50:52].hex(),
            "End Bit": byte_array[52:].hex(),
        }

    # Location Data Packet
    elif protocol_number == 0x17:
        specific_fields = {
            "GPS information" : {   
                "Date Time": byte_array[4:10].hex(),
                "Number Satellites": f"0x{byte_array[10]:02X}",
                "Latitude": byte_array[11:15].hex(),
                "Longitude": byte_array[15:19].hex(),
                "Speed": f"0x{byte_array[19]:02X}",
                "Course Status": byte_array[20:22].hex()
            },
            "LBS Information":  {
                "MCC": byte_array[22:24].hex(),
                "MNC": f"0x{byte_array[24]:02X}",
                "LAC": byte_array[25:27].hex(),
                "Cell ID": byte_array[27:30].hex()
            },
            "Status Information":{
                "Device Information": f"0x{byte_array[30]:02X}",
                "Battery Voltage Level": f"0x{byte_array[31]:02X}",
                "GSM Signal": f"0x{byte_array[32]:02X}",
                "Battery Voltage": byte_array[33:35].hex(),
                "External Voltage": byte_array[35:37].hex()
            },
            "Mileage": byte_array[37:41].hex(),
            "Horimeter": byte_array[41:45].hex(),
            "Serial Number": byte_array[45:47].hex(),
            "CRC": byte_array[47:49].hex(),
            "End Bit": byte_array[49:].hex(),
        }

    # Packet send by Server
    elif protocol_number == 0x80:

        i = int(f"0x{byte_array[4]:02X}", 16)
        j = i - 4

        specific_fields = {
            "Lenght of Command": f"0x{byte_array[4]:02X}",
            "Server Flag Bit": byte_array[5:9].hex(),
            "Command Content": byte_array[9:j+9].hex(),
            "Serial Number": byte_array[j+9:j+11].hex(),
            "CRC": byte_array[j+11:j+13].hex(),
            "End Bit": byte_array[j+13:].hex(),
        }

    # ICCID Packet
    elif protocol_number == 0x94:
        specific_fields = {
            "FLAG": f"0x{byte_array[5]:02X}",
            "IMEI":byte_array[6:14].hex(),
            "IMSI":byte_array[14:22].hex(),
            "ICCID":byte_array[22:32].hex(),
            "Serial Number": byte_array[32:34].hex(),
            "CRC": byte_array[34:36].hex(),
            "End Bit": byte_array[36:].hex(),
        }


    else:
        raise ValueError("Unknown packet. Supports only packets 0x01, 0x13, 0x15, 0x16, 0x17, 0x80, and 0x94.")

    common_fields.update(specific_fields)
    parse_packet = {**common_fields}

    return parse_packet

hex_input = input("Enter the packet to parse (or 'exit' to quit): ")

while hex_input.lower() != 'sair':
    try:
        result = parse_hex_string(hex_input)
        for key, value in result.items():
            if isinstance(value, dict):
                print(f'{key}:')
                for sub_key, sub_value in value.items():
                    print(f'    {sub_key}: {sub_value}')
            else:
                print(f'{key}: {value}')
    except ValueError as e:
        print("Erro:", e)

    hex_input = input("Enter the packet to parse (or 'exit' to quit): ")
