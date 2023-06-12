espnow docs: https://docs.micropython.org/en/latest/library/espnow.html

# Hardware

[Lolin D1 Mini board: esp8266](https://www.wemos.cc/en/latest/d1/d1_mini.html)

- Firmware installed: [MicroPython v1.20.0-189-gfd277704c ESP module with ESP8266 2MiB+](https://micropython.org/download/esp8266/) (nightly build)
  - If installing new micropython firmware, must be **newer** than v1.20.0-189 nightly or **newer** than 1.20.0 stable for espnow support

[Lolin S2 Mini board: esp32-s2](https://www.wemos.cc/en/latest/s2/s2_mini.html)

- Firmware installed: [MicroPython v1.20.0-189-gfd277704c LOLIN_S2_MINI with ESP32-S2FN4R2](https://micropython.org/download/LOLIN_S2_MINI/) (nightly build)
  - If installing new micropython firmware, must be **newer** than v1.20.0-189 nightly or **newer** than 1.20.0 stable for espnow support
  - Firmware installation [https://www.wemos.cc/en/latest/tutorials/d1/get_started_with_micropython_d1.html](instructions)

# Tools to install:

- [`ampy`](https://github.com/scientifichackers/ampy) - ESP device file management

  ```sh
  pip install adafruit-ampy
  python -m ampy.cli --help
  ```

- [`esptool`](https://docs.espressif.com/projects/esptool/en/latest/esp32/) - ESP firmware management
  ```sh
  pip install esptool
  python -m esptool --help
  ```
