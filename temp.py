import time
import busio
import board
import adafruit_amg88xx

import matplotlib.pyplot as plt

# I2Cバス、センサーの初期化
i2c_bus = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_amg88xx.AMG88XX(i2c_bus, addr=0x69)

# ちょっと待つ
time.sleep(.1)

# ループ開始
while True:
    # データ取得
    sensordata = sensor.pixels

    # bicubicのデータ
    fig = plt.imshow(sensordata, cmap="inferno", interpolation="bicubic")
    plt.colorbar()

    # wait代わりに pause
    plt.pause(.1)
    plt.clf()