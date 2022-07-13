
import sys
from kintone_sdk4python import Kintone

import spidev
import time

# kintone connect settings
kintone = Kintone()
kintone.set_domain('{subdomain}.cybozu.com')
kintone.set_token_auth('token1234')
kintone_appid = 1234

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
spi.bits_per_word=8

print('start... 30sec left')

def measure():
    dummy = 0xff
    start = 0x47
    sgl = 0x20
    msbf = 0x08
    ch = 0x10
    ad = spi.xfer2([( start + sgl + ch + msbf ), dummy])
    val = (((( ad[0] & 0x03) << 8) + ad[1]) * 3.3 ) / 1023
    return val

# start pulse check of 30sec
pulsecount = 0
prevpulse = 0
for i in range(300):
    mes_ch = measure()
    print 'ch = %2.2f' % mes_ch,'[V]'

    if (i == 100):
        print('******************* 20sec left')
    if (i == 200):
        print('******************* 10sec left')
    if (i == 250):
        print('******************* 5sec left')
    # pulse count
    if (float(prevpulse) < 2.8 and float(mes_ch) >= 2.8):
        pulsecount = pulsecount + 1
        print('******************* pulsecount = %d' % pulsecount)

    prevpulse = mes_ch
   # sleep 0.1sec
    time.sleep(0.1)

# create kitnone request body
request_body = {
    "pulse": {
        "value": pulsecount * 2
    }
}

# post kintone request
post_record_resp = kintone.post_record(kintone_appid, request_body)

print('finish')
spi.close()
