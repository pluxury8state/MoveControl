from pybluez import bluetooth

"""
    This Python code looks for a nearby device with the user-friendly name ``My Phone".
"""


target_name = "My Phone"
target_address = None

nearby_devices = bluetooth.discover_devices(lookup_names=True)  # поиск ближайших устройств
                                               # сканирование идет примерно 10 секунд и возвращается список адресов

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name(bdaddr):
        target_address = bdaddr  # находит адрес с подходящим именем, который мы искали
        break

if target_address is not None:
    print("Нашел подходящее устройство с адресом ", target_address)
else:
    print("Устройства с подходящим именем были не найдены")

# PyBluez represents a bluetooth address as a string of the form ``xx:xx:xx:xx:xx",
# where each x is a hexadecimal character representing one octet of the 48-bit address,
# with most significant octets listed first.
# Bluetooth devices in PyBluez will always be identified using an address string of this form.
#
