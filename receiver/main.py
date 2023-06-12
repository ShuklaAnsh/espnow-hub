import json
from time import sleep_ms
import urequests
from utils import *


def send_discord_msg(msg: str, config: dict):
    """
    Sends a discord message via webook
    Connects to the wlan to send the msg and then disconnects to resume espnow

    :param str webhook_url: https://discord.com/api/webhooks/{webhook_id}/{webhook_token}
    :param str msg: The message to send to the discord server
    """

    webhook_url = config["DISCORD_WEBHOOK_URL"]
    ssid = config["WLAN_SSID"]
    pw = config["WLAN_PW"]

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    success = False

    if pw != None and ssid != None:
        if not wlan.isconnected():
            wlan.connect(ssid, pw)
            while not wlan.isconnected():
                # timeout would be good here
                pass

    error_count = 0
    while error_count <= 5:
        try:
            response = urequests.post(webhook_url, headers={
                                      "Connection": "Close"}, json={"content": msg})
            response.close()  # socket must be closed after every request

            if response.status_code is 200 or response.status_code is 204:
                success = True
                break

            else:
                error_count += 1
                sleep_ms(50)

        except Exception as e:
            response.close()
            error_count += 1
            sleep_ms(50)

    # disconnect wlan to resume espnow connection
    wlan.disconnect()
    return success


def load_data(data_bytes: bytes):
    # try-catch would be good here
    data = json.loads(data_bytes)
    if "msg" not in data.keys():
        data["msg"] = "Trigger Recieved"
    return data


config = read_config()
discord_webhook_url = config["DISCORD_WEBHOOK_URL"]
esp_now = init_espnow()

while True:
    host_mac, msg = esp_now.recv()
    if msg:  # msg == None if timeout in recv()
        print(mac_bytes_to_string(host_mac), msg)
        data = load_data(msg)
        send_discord_msg(data["msg"], config)
        if msg == b'end':
            break
