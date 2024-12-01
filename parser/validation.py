def validate_hex_string(hex_string):

    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string.")

    hex_string = hex_string.lower().replace(" ", "")

    if len(hex_string) % 2 != 0:
        raise ValueError("Hexadecimal string must have an even number of characters.")

    if not all(c in "0123456789abcdef" for c in hex_string):
        raise ValueError("String contains invalid hexadecimal characters.")

    return hex_string

def validate_packet_length(byte_array, expected_length):

    if len(byte_array) != expected_length:
        raise ValueError(f"Packet length is invalid. Expected {expected_length} bytes, got {len(byte_array)} bytes.")
    return True


def validate_protocol(byte_array, valid_protocols):

    protocol_number = byte_array[3]
    if protocol_number not in valid_protocols:
        raise ValueError(f"Invalid protocol number: {protocol_number}. Supported protocols: {valid_protocols}")
    return True

def validate_packet_format(byte_array, expected_format):

    if len(byte_array) != len(expected_format):
        raise ValueError(f"Invalid packet length. Expected {len(expected_format)} bytes, got {len(byte_array)} bytes.")

    for i, expected_byte in enumerate(expected_format):
        if byte_array[i] != expected_byte:
            raise ValueError(f"Invalid byte at position {i}. Expected {expected_byte}, got {byte_array[i]}.")

    return True
