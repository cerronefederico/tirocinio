from pymodbus.client import ModbusTcpClient
client = ModbusTcpClient('192.168.1.100', port=502)
if client.connect():
    print("Connection established")
else:
    print("Connection failed")  