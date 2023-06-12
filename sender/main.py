import json
from utils import *

config = read_config()
peer_mac = mac_string_to_bytes(config["RECV_MAC_ADDR"])
esp_now = init_espnow([peer_mac])


def send_data(data):
    serialized_data = json.dumps(data)
    return esp_now.send(peer_mac, serialized_data, True)
