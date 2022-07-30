import time
import sys
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)

def measure():
    dummy = 0xff
    start = 0x47
    sgl = 0x20
    msbf = 0x08
    ch = 0x10
    ad = spi.xfer2([( start + sgl + ch + msbf ), dummy])
    val = (((( ad[0] & 0x03) << 8) + ad[1]) * 3.3 ) / 1023
    return val

pulsecount = 0
prevpulse = 0
for i in range(300):
    mes_ch = measure()
    print('ch = %2.2f' % mes_ch,'[V]')

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
# def readAdc(channel):
#     adc = spi.xfer2([1, (8 + channel)<< 4, 0])
#     data = ((adc[1] & 3) << 8) + adc[2]
#     return data
#
#
# def convertVolts(data):
#     volts = (data * 3.3) / float(1023)
#     volts = round(volts, 4)
#     return volts
#
#
# def convertTemp(volts):
#     temp = (100 * volts) - 50.0
#     temp = round(temp, 4)
#     return temp
#
#
# if __name__ == '__main__':
#     try:
#         while True:
#             data = readAdc(0)
#             print("adc  : {:8} ".format(data))
#             volts = convertVolts(data)
#             temp = convertTemp(volts)
#             print("volts: {:8.2f}".format(volts))
#             print("temp : {:8.2f}".format(temp))
#
#             time.sleep(1)
#     except KeyboardInterrupt:
#         spi.close()
#         sys.exit(0)