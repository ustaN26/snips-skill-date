#!/usr/bin/env python3
import serial

try:
	ser = serial.Serial(
		port='/dev/ttyACM0',
		baudrate = 9600,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
		timeout=1
	)
	ser.write(serial.to_bytes([0x01,0x09,0x30,0x30,0x10,0x30,0x34,0x4D,0x0D,0x0A]))
	ser.close()
except:
	ser.close()
