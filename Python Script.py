import snap7
from snap7.util import *
import struct
import time
plc_ip = '10.200.1.130'
client = snap7.client.Client()
db_num = 1
offset = 1
try:
client.connect(plc_ip, 0, 1)
if client.get_connected():
print("Подключено к ПЛК")
cpu_state = client.get_cpu_state()
print(f"Статус ПЛК: {cpu_state}")
if cpu_state != 'S7CpuStatusRun':
client.disconnect()
exit()
try:
new_value = 2 # %DB1.%D1.1
data_to_write = bytearray(struct.pack('<h', new_value))
client.db_write(db_num, offset, data_to_write)
print(f"Новое значение {new_value} успешно записано в DB{db_num}, Offset {offset}.")
except Exception as e_write:
print(f"Ошибка записи: {e_write}")
client.disconnect()
exit()
else:
print(f"Не удалось подключиться к ПЛК")
except Exception as e:
print(f"Exception; {e}")
finally:
if client.get_connected():
client.disconnect()
print("Отключено от ПЛК")
