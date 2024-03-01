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
Data analyzed

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

### Error Handling
If an invalid hexadecimal string is provided or the packet structure doesn't match any supported protocol, it raises a ValueError.
Feel free to modify and adapt this script according to your requirements!