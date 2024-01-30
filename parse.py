def parse_hex_string(hex_string):
    if len(hex_string) % 2 != 0:
        raise ValueError("A string hexadecimal deve ter um número par de dígitos.")

    byte_array = bytearray.fromhex(hex_string)
    protocol_number = byte_array[3]

    if protocol_number == 0x16:
        if len(byte_array) < 54:
            raise ValueError("A string hexadecimal para byte 0x16 deve ter pelo menos 54 bytes.")

        start_bit = byte_array[:2]
        packet_length = byte_array[2]
        date_time = byte_array[4:10]
        number_satellites = byte_array[10]
        latitude = byte_array[11:15]
        longitude = byte_array[15:19]
        speed = byte_array[19]
        course_status = byte_array[20:22]
        lbs_length = byte_array[22]
        mcc = byte_array[23:25]
        mnc = byte_array[25]
        lac = byte_array[26:28]
        cell_id = byte_array[28:31]
        device_information = byte_array[31]
        battery_voltage_level = byte_array[32]
        gsm_signal = byte_array[33]
        alarm_packet = byte_array[34]
        language = byte_array[35]
        battery_voltage = byte_array[36:38]
        external_voltage = byte_array[38:40]
        mileage = byte_array[40:44]
        horimeter = byte_array[44:48]
        serial_number = byte_array[48:50]
        crc = byte_array[50:52]
        end_bit = byte_array[52:]

        parse_packet = {
            "Start Bit": start_bit.hex(),
            "Packet Length": hex(packet_length),
            "Protocol Number": hex(protocol_number),
            "Date Time": date_time.hex(),
            "Number Satellites": hex(number_satellites),
            "Latitude": latitude.hex(),
            "Longitude": longitude.hex(),
            "Speed": hex(speed),
            "Course Status": course_status.hex(),
            "LBS Length": hex(lbs_length),
            "MCC": mcc.hex(),
            "MNC": hex(mnc),
            "LAC": lac.hex(),
            "Cell ID": cell_id.hex(),
            "Device Information": hex(device_information),
            "Battery Voltage Level": hex(battery_voltage_level),
            "GSM Signal": hex(gsm_signal),
            "Alarm Packet": hex(alarm_packet),
            "Language": hex(language),
            "Battery Voltage": battery_voltage.hex(),
            "External Voltage": external_voltage.hex(),
            "Mileage": mileage.hex(),
            "Horimeter": horimeter.hex(),
            "Serial Number": serial_number.hex(),
            "CRC": crc.hex(),
            "End Bit": end_bit.hex()
        }

    elif protocol_number == 0x17:
        if len(byte_array) < 51:
            raise ValueError("A string hexadecimal para byte 0x17 deve ter pelo menos 51 bytes.")

        start_bit = byte_array[:2]
        packet_length = byte_array[2]
        date_time = byte_array[4:10]
        number_satellites = byte_array[10]
        latitude = byte_array[11:15]
        longitude = byte_array[15:19]
        speed = byte_array[19]
        course_status = byte_array[20:22]
        mcc = byte_array[22:24]
        mnc = byte_array[24]
        lac = byte_array[25:27]
        cell_id = byte_array[27:30]
        device_information = byte_array[30]
        battery_voltage_level = byte_array[31]
        gsm_signal = byte_array[32]
        battery_voltage = byte_array[33:35]
        external_voltage = byte_array[35:37]
        mileage = byte_array[37:41]
        horimeter = byte_array[41:45]
        serial_number = byte_array[45:47]
        crc = byte_array[47:49]
        end_bit = byte_array[49:]

        parse_packet = {
            "Start Bit": start_bit.hex(),
            "Packet Length": hex(packet_length),
            "Protocol Number": hex(protocol_number),
            "Date Time": date_time.hex(),
            "Number Satellites": hex(number_satellites),
            "Latitude": latitude.hex(),
            "Longitude": longitude.hex(),
            "Speed": hex(speed),
            "Course Status": course_status.hex(),
            "MCC": mcc.hex(),
            "MNC": hex(mnc),
            "LAC": lac.hex(),
            "Cell ID": cell_id.hex(),
            "Device Information": hex(device_information),
            "Battery Voltage Level": hex(battery_voltage_level),
            "GSM Signal": hex(gsm_signal),
            "Battery Voltage": battery_voltage.hex(),
            "External Voltage": external_voltage.hex(),
            "Mileage": mileage.hex(),
            "Horimeter": horimeter.hex(),
            "Serial Number": serial_number.hex(),
            "CRC": crc.hex(),
            "End Bit": end_bit.hex()
        }

    else:
        raise ValueError("Pacote desconhecido. Suporta apenas os pacotes 0x16 e 0x17.")

    return parse_packet

hex_input = input("Insira o pacote para parsear: ")

try:
    result = parse_hex_string(hex_input)

    for key, value in result.items():
        print(f"{key}: {value}")
except ValueError as e:
    print("Erro:", e)