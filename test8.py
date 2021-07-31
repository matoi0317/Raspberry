#必要なモジュールをインポート
import RPi.GPIO as GPIO             #GPIO用のモジュールをインポート
import time                         #時間制御用のモジュールをインポート

#ポート番号の定義
Led_pin = 18                        #変数"Led_pin"に18を格納

#GPIOの設定
GPIO.setmode(GPIO.BCM)              #GPIOのモードを"GPIO.BCM"に設定
GPIO.setup(Led_pin, GPIO.OUT)       #GPIO18を出力モードに設定

#GPIOの電圧を制御
GPIO.output(Led_pin, GPIO.HIGH)     #GPIO18の出力をHigh(3.3V)にする
time.sleep(5)                       #5秒間待つ
GPIO.output(Led_pin, GPIO.LOW)      #GPIO18の出力をLow(0V)にする

#GPIOをクリーンアップ
GPIO.cleanup()