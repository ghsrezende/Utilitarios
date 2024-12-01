from enum import Enum

class Protocols(Enum):
    LOGIN = 0x01
    HEARTBEAT = 0x13
    REPLIED_BY_DEVICE = 0x15
    ALARM = 0x16
    LOCATION = 0x17
    STATUS = 0x30
    SENT_BY_SERVER = 0x80
    ICCID = 0x94

    # GT06 específico
    LOCATION_GT06_V1 = 0x12
    LOCATION_GT06_V2 = 0x22
    LOCATION_GT06_V3 = 0x32
    LOCATION_GT06_V4 = 0x0A
    HEARTBEAT_GT06 = 0x13
    ALARM_GT06 = 0x16

    @classmethod
    def list_all(cls):

        return [protocol.value for protocol in cls]

    @classmethod
    def is_valid(cls, protocol_number):

        return protocol_number in cls.list_all()
