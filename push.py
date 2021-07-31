# coding:utf-8
import os
from platform import system

pf = system()
if pf == "Darwin":
    os.system("osascript -e 'display notification \"こんにちは世界\"'")