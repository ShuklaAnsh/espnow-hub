import json
import network
import ubinascii
import espnow


def init_espnow(peer_macs: list[bytes] = []):
    """
    Initializes espnow and, if ssid and pw provided, wifi connection
    """

    # A WLAN interface must be active to send()/recv()
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # espnow can't work while wlan connected
    wlan.disconnect()

    conn = espnow.ESPNow()
    conn.active(True)

    for mac in peer_macs:
        conn.add_peer(mac)

    return conn


def read_config():
    """
    Reads in the config file. Expected fields:
    - `DISCORD_WEBHOOK_URL`
    - `WLAN_PW`
    - `WLAN_SSID`
    - `RECV_MAC_ADDR`

    :returns dict:
    """
    f = open("conf.json")
    data = json.load(f)
    f.close()
    return data


def mac_bytes_to_string(mac: bytes) -> str:
    return ubinascii.hexlify(mac, ':').decode().upper()


def mac_string_to_bytes(mac: str) -> bytes:
    return ubinascii.unhexlify(mac.replace(':', ''))
