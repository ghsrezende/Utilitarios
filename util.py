def bytes_to_latitude(byte_value):
    """Converts a byte array representing latitude to a decimal value.
    Args:
        byte_value: A byte array containing the latitude data.
    Returns:
        The latitude in degrees as a float.
    """
    # Convert the 4 bytes to an integer.
    integer_value = int.from_bytes(byte_value, byteorder='big')

    # Divide by the scaling factor (30000).
    scaled_value = integer_value / 30000

    # Calculate the latitude in degrees (0° to 90°).
    latitude_decimal = scaled_value / 60

    return latitude_decimal

def bytes_to_longitude(byte_value):
    """Converts a byte array representing longitude to a decimal value.
    Args:
        byte_value: A byte array containing the longitude data.
    Returns:
        The longitude in degrees as a float.
    """
    # Convert the 4 bytes to an integer.
    integer_value = int.from_bytes(byte_value, byteorder='big')

    # Divide by the scaling factor (30000).
    scaled_value = integer_value / 30000

    # Calculate the longitude in degrees (0° to 180°).
    longitude_decimal = scaled_value / 60

    return longitude_decimal

def timestamp(byte_value):
    """Extracts a timestamp from a byte array.
    Args:
        byte_value: A byte array containing the timestamp data.
    Returns:
        The timestamp in the format "YYYY-MM-DD HH:MM:SS".
    """
    year = byte_value[0]
    month = byte_value[1]
    day = byte_value[2]
    hour = byte_value[3]
    minute = byte_value[4]
    second = byte_value[5]

    return f"{year}-{month}-{day} {hour}:{minute}:{second}"

def course_status(byte_array):
    """Parses a byte array representing the course status and returns a dictionary.
    Args:
        byte_array: A byte array containing the course status data.
    Returns:
        A dictionary containing information about the course status, including:
            * Value Hex: The hexadecimal representation of the byte array.
            * Value Binary: The binary representation of the byte array.
            * Descriptions and values for each bit in the byte array.
    """
    # Convert the byte array to a hexadecimal string.
    byte_value = int(byte_array.hex(), 16)
    
    # Convert the byte value to a binary string
    binary_string = bin(byte_value)[2:].zfill(16)  # 16 bits to represent 2 bytes

    # Map each binary digit to its corresponding description in the dictionary
    binary_mapping = {
        "Value Hex": f"0x{byte_array.hex()}",
        "Value Binary": binary_string,
        "BYTE_1 Bit7": "Not used",
        "BYTE_1 Bit6": {
            "Description": "Input On" if binary_string[1] == '1' else "Input Off",
            "Value": binary_string[1],
        },
        "BYTE_1 Bit5": {
            "Description": "GPS Real Time" if binary_string[2] == '1' else "GPS Differential Positioning",
            "Value": binary_string[2],
        },
        "BYTE_1 Bit4": {
            "Description": "GPS Fixed" if binary_string[3] == '1' else "GPS Not Fixed",
            "Value": binary_string[3],
        },
        "BYTE_1 Bit3": {
            "Description": "West Longitude" if binary_string[4] == '1' else "East Longitude",
            "Value": binary_string[4],
        },
        "BYTE_1 Bit2": {
            "Description": "North Latitude" if binary_string[5] == '1' else "South Latitude",
            "Value": binary_string[5],
        },
        "BYTE_1 Bit1 to BYTE_2 [0:7]": {  # Faixa de bits corrigida
            "Description": "Course",
            "Value Binary": binary_string[6:],  # Nomenclatura consistente
            "Value": int(binary_string[6:], 2),  # Conversão interna
        },
    }

    return binary_mapping

def device_information(byte_array):
    """Extracts device information from a byte array and returns a dictionary.
    Args:
        byte_array: A byte array containing the device information data.
    Returns:
        A dictionary containing information about the device, including:
            * Value Hex: The hexadecimal representation of the byte array.
            * Value Binary: The binary representation of the byte array.
            * Descriptions and values for each bit in the byte array.
    """
    # Convert the byte value to a binary string with zero-padding to 8 bits.
    binary_string = bin(byte_array)[2:].zfill(8)  # Use first byte for device info

    # Map each binary digit to its corresponding description in the dictionary.
    binary_mapping = {
        "Value Hex": f"0x{byte_array:02X}",
        "Value Binary": binary_string,
        "Bit0": {
            "Description": "Fortified" if binary_string[7] == '1' else "Not fortified",
            "Value": binary_string[7],
        },
        "Bit1": {
            "Description": "ACC ON" if binary_string[6] == '1' else "ACC OFF",
            "Value": binary_string[6],
        },
        "Bit2": {
            "Description": "Charged" if binary_string[5] == '1' else "Not Charged",
            "Value": binary_string[5],
        },
        "Bit3 to Bit5": {
            "Description": {
                "000": "Normal",
                "001": "Vibration alarm",
                "010": "Cut-off alarm",
                "011": "Low-power alarm",
                "100": "SOS alarm",
            }[binary_string[2:5]],
            "Value": binary_string[2:5],
        },
        "Bit6": {
            "Description": "GPS Fix" if binary_string[1] == '1' else "GPS Not Fix",
            "Value": binary_string[1],
        },
        "Bit7": {
            "Description": "Output On" if binary_string[0] == '1' else "Output Off",
            "Value": binary_string[0],
        },
    }
    
    return binary_mapping

def battery_voltage(hex_string):
    """Converts a hexadecimal string representing battery voltage to a decimal value.
    Args:
        hex_string: The hexadecimal string representing the battery voltage.
    Returns:
        The battery voltage in volts as a decimal value.
    """
    decimal_value = int(hex_string.hex(), 16)
    return decimal_value / 100

def external_voltage(hex_string):
    """Converts a hexadecimal string representing external voltage to a decimal value.
    Args:
        hex_string: The hexadecimal string representing the external voltage.
    Returns:
        The external voltage in volts as a decimal value.
    """
    decimal_value = int(hex_string.hex(), 16)
    
    return decimal_value / 100

def horimeter(hex_string):
    """Converts a hexadecimal string representing the horimeter value to hours, minutes, and seconds.
    Args:
        hex_string: The hexadecimal string representing the horimeter value.
    Returns:
        A string representing the horimeter value in the format "HH:MM:SS".
    """
    # Convert the hexadecimal value to seconds.
    int_seconds = int(hex_string.hex(), 16)

    # Convert seconds to hours, minutes, and seconds with zero-padding.
    hours = int_seconds // 3600
    minutes = (int_seconds % 3600) // 60
    seconds = int_seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def alarm_type(hex_string):
    """Determines the alarm type based on a hexadecimal string.
    Args:
        hex_string: The hexadecimal string representing the alarm code.
    Returns:
        A dictionary containing the alarm description and hexadecimal value.
    """
    alarm_mapping = {
        "0x00": {"description": "Normal", "Value Hex": "0x00"},
        "0x01": {"description": "SOS", "Value Hex": "0x01"},
        "0x02": {"description": "Power Cut Alarm", "Value Hex": "0x02"},
        "0x03": {"description": "Shock Alarm", "Value Hex": "0x03"},
        "0x04": {"description": "Fence In Alarm", "Value Hex": "0x04"},
        "0x05": {"description": "Fence Out Alarm", "Value Hex": "0x05"},
        "0x06": {"description": "Speed Alarm", "Value Hex": "0x06"},
        "0x09": {"description": "Move Alarm", "Value Hex": "0x09"},
        "0x0D": {"description": "SIMDETECT", "Value Hex": "0x0D"},
        "0x0E": {"description": "Low Battery Alarm", "Value Hex": "0x0E"},
        "0x13": {"description": "Disassemble Alarm", "Value Hex": "0x13"},
        "0x14": {"description": "ACC On Alarm", "Value Hex": "0x14"},
        "0x15": {"description": "ACC Off Alarm", "Value Hex": "0x15"},
        "0x18": {"description": "Change Status Input", "Value Hex": "0x18"},
        "0x26": {"description": "Rapid Acceleration Alarm", "Value Hex": "0x26"},
        "0x27": {"description": "Rapid Deceleration Alarm", "Value Hex": "0x27"},
        "0x28": {"description": "Sharp Turn Alarm", "Value Hex": "0x28"},
        "0x29": {"description": "Collision Alarm", "Value Hex": "0x29"},
    }

    return alarm_mapping.get(hex_string, {"description": "Unknown Alarm", "Value Hex": hex_string})

def hex_to_ascii(byte_array):
    """Converts a bytearray in hexadecimal representation to ASCII string.
    Args:
        byte_array (bytearray): A bytearray containing hexadecimal data.
    Returns:
        str: The ASCII string decoded from the hexadecimal bytearray.
            Returns None if conversion fails.
    """
    try:
        # Convert the bytearray to hexadecimal string
        hex_string = byte_array.hex()
        # Convert the hexadecimal string to ASCII
        ascii_string = bytes.fromhex(hex_string).decode('ascii')
        return ascii_string
    except Exception as e:
        print("Error:", e)
        return None
    
def language(hex_value):
    """
    Determines the language based on the hexadecimal value.
    Args:
        hex_value (str): The hexadecimal value representing the language.
    Returns:
        str: The language corresponding to the hexadecimal value.
    """
    lang = "Chinese" if hex_value == '0x01' else "English"
    return lang

def gps_information(hex_value):
    """
    Determines the length of GPS information and the number of the
    satellites join in positioning based on the hexadecimal value.
    Args:
        hex_value (str): The hexadecimal value representing the GPS information.
    Returns:
        Length of GPS information and Number of the Satellites.
    """
    decimal_mapping = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                       'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    result = {}
    result["Length in bits"] = decimal_mapping.get(hex_value[2].upper(), hex_value[2])
    result["Satellites"] = decimal_mapping.get(hex_value[3].upper(), hex_value[3])
    
    return result

def battery_voltage_level(hex_string):
    """Determines the battery voltage level based on a hexadecimal string.
    Args:
        hex_string: The hexadecimal string representing the code.
    Returns:
        A dictionary containing the battery voltage level description and hexadecimal value.
    """
    alarm_mapping = {
        "0x00": {"description": "Lowest power and power off", "Value Hex": "0x00"},
        "0x01": {"description": "Not enough power to dial a call or send messages", "Value Hex": "0x01"},
        "0x02": {"description": "Low power and alarm", "Value Hex": "0x02"},
        "0x03": {"description": "Lower power but can work normally", "Value Hex": "0x03"},
        "0x04": {"description": "Work in good condition", "Value Hex": "0x04"},
        "0x05": {"description": "Work in good condition", "Value Hex": "0x05"},
        "0x06": {"description": "Work in good condition", "Value Hex": "0x06"},
    }

    return alarm_mapping.get(hex_string, {"description": "Unknown", "Value Hex": hex_string})