from pymodbus.client import ModbusTcpClient
client = ModbusTcpClient('192.168.0.1', port=102)

try:
    client.connect()
    print("Connessione a PostgreSQL avvenuta con successo!")
except Exception:
    print("Connessione a PostgreSQL avvenuta con error!")
