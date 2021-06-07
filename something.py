import rssi
from collections import defaultdict


def detect_beacons():
    """
    this function detects our beacons
    :return: list of Beacon objects
    """


def create_server():
    """
    This function create server on this computer
    :return: Server object
    """



if __name__ == '__main__':

    interface = 'DESKTOP-9Q0LR86'

    scaner = rssi.RSSI_Scan(interface)  # наш сервер, относительно которого будем определять уровень сигнала на других машинах
    localizer = rssi.RSSI_Localizer('DESKTOP-PAP03NC')
    InfoList = scaner.getAPinfo()
    d = defaultdict(list)
    distance_list = [{item.get['ssid'].append(localizer.getDistanceFromAP(item))}  for i in range(50) for item in InfoList]






