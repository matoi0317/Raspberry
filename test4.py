# coding:utf-8
import requests
import sys

def main():
    url = "https://notify-api.line.me/api/notify"
    token = 'gPTBwhxe0NON5u4NGTyTBGFLW1sTHPY7zB6bsf8Wgot'
    headers = {"Authorization" : "Bearer "+ token}

    args = sys.argv
    if args[0] == 1:
        message = '通常終了'
    else:
        message = '異常終了'
    payload = {"message" :  message}
    files = {"imageFile": open("b.png", "rb")}

    r = requests.post(url ,headers = headers ,params=payload, files=files)

if __name__ == '__main__':
    main()