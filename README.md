# Packet Parser

> This Python script allows you to parse hexadecimal packets according to predefined protocols. It reads a hexadecimal input representing different types of packets and outputs the parsed fields and their values.

## How to Use

## Prerequisites
> Python installed on your system

## Running the Script
>> 1. Clone or download this repository to your local machine.
>> 2. Navigate to the directory containing the script.
>> 3. Run the script using the following command: python packet_parser.py
>> 4. Enter the hexadecimal packet string when prompted. You can input 'exit' to quit the program.

## Understanding the Output
> The script takes a hexadecimal packet string as input and parses it according to predefined protocols.
It displays the parsed fields along with their corresponding values.
For nested fields, such as dictionaries, it displays each sub-field with proper indentation.

## Supported Protocols
>> Login Packet (Protocol Number: 0x01)
>> Heartbeat Packet (Protocol Number: 0x13)
>> Response Command Packet (Protocol Number: 0x15)
>> Alarm Packet (Protocol Number: 0x16)
>> Location Packet (Protocol Number: 0x17)
>> Command Packet (Protocol Number: 0x80)
>> ICCID Packet (Protocol Number: 0x94)

## Error Handling
> If an invalid hexadecimal string is provided or the packet structure doesn't match any supported protocol, it raises a ValueError.
Feel free to modify and adapt this script according to your requirements!