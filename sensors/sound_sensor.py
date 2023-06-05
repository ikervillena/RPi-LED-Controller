import smbus
import time

ADDR_ADC121 = 0x50
REG_ADDR_RESULT = 0x00
REG_ADDR_CONFIG = 0x02

bus = smbus.SMBus(1)

class SoundSensor:
    def __init__(self):
        bus.write_byte_data(ADDR_ADC121, REG_ADDR_CONFIG, 0x20)

    def read_adc(self):
        data_list = bus.read_i2c_block_data(ADDR_ADC121, REG_ADDR_RESULT, 2)
        data = ((data_list[0] & 0x0f) << 8 | data_list[1]) & 0xfff
        return data
