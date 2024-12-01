# Packet Parser

This Python script allows you to parse hexadecimal packets according to predefined protocols. It reads a hexadecimal input representing different types of packets and outputs the parsed fields and their values.

### Specification
> ### Minimum Required Python Version
> This script requires Python 3.10 or above.
>
> ### Prerequisites
> Python 3.10 or above installed on your system

### Running the Script
1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using the following command:  
```sh 
    python packet_parser.py
```
4. Enter the hexadecimal packet string when prompted. You can input 'exit' to quit the program.

If you want to see the translation of the packages, use the command
```sh 
    python parser_packet_translated.py
```
### Understanding the Output
The script takes a hexadecimal packet string as input and parses it according to predefined protocols. It displays the parsed fields along with their corresponding values. For nested fields, such as dictionaries, it displays each sub-field with proper indentation.

### Supported Protocols
- Login Packet (Protocol Number: 0x01)
- Heartbeat Packet (Protocol Number: 0x13)
- Packet Replied by Device (Protocol Number: 0x15)
- Alarm Packet (Protocol Number: 0x16)
- Location Data Packet (Protocol Number: 0x17)
- Packet send by Server (Protocol Number: 0x80)
- IMSI Packet (Protocol Number: 0x90)
- ICCID Packet (Protocol Number: 0x94)
- Address Packet (Protocol Number: 0x1A)
- WIFI Packet (Protocol Number: 0x2C)

### Sample Usage

Below is an example of an analyzed package.

```sh
Enter the packet to parse (or 'exit' to quit): 78782e17180214133533cd02d99563053a211f68595d0000000000000000460640018c052f00315de8000343a00112073a0d0a
```
Data analyzed with packet_parser.py

```sh
Start Bit: 7878
Packet Length: 0x2E
Protocol Number: 0x17
GPS information:
    Date Time: 180214133533
    Number Satellites: 0xCD
    Latitude: 02d99563
    Longitude: 053a211f
    Speed: 0x68
    Course Status: 595d
LBS Information:
    MCC: 0000
    MNC: 0x00
    LAC: 0000
    Cell ID: 000000
Status Information:
    Device Information: 0x46
    Battery Voltage Level: 0x06
    GSM Signal: 0x40
    Battery Voltage: 018c
    External Voltage: 052f
Mileage: 00315de8
Horimeter: 000343a0
Serial Number: 0112
CRC: 073a
End Bit: 0d0a
```

Data analyzed with python parser_packet_translated.py

```sh
Start Bit: 7878
Packet Length:
    Value Hex: 0x2E
    Value: 46
Protocol Number:
    Value Hex: 0x17
    Value: Location Data Packet
GPS information:
    Date Time:
        Value Hex: 0x180214133533
        Value: 24-2-20 19:53:51
    Number Satellites:
        Value Hex: 0xCD
        Value: 205
    Latitude:
        Value Hex: 0x02d99563
        Value: 26.56332611111111
    Longitude:
        Value Hex: 0x053a211f
        Value: 48.71980388888889
    Speed:
        Value Hex: 0x68
        Value: 104
    Course Status:
        Value Hex: 0x595d
        Value Binary: 0101100101011101
        BYTE_1 Bit7: Not used
        BYTE_1 Bit6: {'Description': 'Input On', 'Value': '1'}
        BYTE_1 Bit5: {'Description': 'GPS Differential Positioning', 'Value': '0'}
        BYTE_1 Bit4: {'Description': 'GPS Fixed', 'Value': '1'}
        BYTE_1 Bit3: {'Description': 'West Longitude', 'Value': '1'}
        BYTE_1 Bit2: {'Description': 'South Latitude', 'Value': '0'}
        BYTE_1 Bit1 to BYTE_2 [0:7]: {'Description': 'Course', 'Value Binary': '0101011101', 'Value': 349}       
LBS Information:
    MCC:
        Value Hex: 0x0000
        Value: 0
    MNC:
        Value Hex: 0x00
        Value: 0
    LAC:
        Value Hex: 0x0000
        Value: 0
    Cell ID:
        Value Hex: 0x000000
        Value: 0
Status Information:
    Device Information:
        Value Hex: 0x46
        Value Binary: 01000110
        Bit0: {'Description': 'Not fortified', 'Value': '0'}
        Bit1: {'Description': 'ACC ON', 'Value': '1'}
        Bit2: {'Description': 'Not Charged', 'Value': '0'}
        Bit3 to Bit5: {'Description': 'Vibration alarm', 'Value': '001'}
        Bit6: {'Description': 'GPS Fix', 'Value': '1'}
        Bit7: {'Description': 'Output Off', 'Value': '0'}
    Battery Voltage Level:
        Value Hex: 0x06
        Value: 6
    GSM Signal:
        Value Hex: 0x40
        Value: 64
    Battery Voltage:
        Value Hex: 0x018c
        Value: 3.96
    External Voltage:
        Value Hex: 0x052f
        Value: 13.27
Mileage:
    Value Hex: 0x00315de8
    Value: 3235304
Horimeter:
    Value Hex: 0x000343a0
    Value: 59:25:20
Serial Number:
    Value Hex: 0x0112
    Value: 274
CRC: 073a
End Bit: 0d0a
```
### Error Handling
If an invalid hexadecimal string is provided or the packet structure doesn't match any supported protocol, it raises a ValueError.
Feel free to modify and adapt this script according to your requirements!