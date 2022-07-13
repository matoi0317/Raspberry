# coding: utf-8
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont
import datetime
from functions.firebase import send_pdf

def Create_pdf(text, text2):
    dt_now = datetime.datetime.now()
    datetime_format = dt_now.strftime("%Y%m%d%H%M%S")
    registerFont(TTFont('GenShinGothic',
                        './data/GenShinGothic-Monospace-Medium.ttf'))

    file = datetime_format + 'reportlab-test.pdf'  # 出力ファイル名を設定

    paper = canvas.Canvas(file)  # 白紙のキャンバスを用意shima-suxu
    paper.saveState()  # 初期化
    paper.setFont('GenShinGothic', 24)  # フォントを設定

    # 横wと縦hの用紙サイズを設定
    w = 210 * mm
    h = 297 * mm

    paper.setPageSize((w, h))  # 用紙のサイズをセット
    paper.drawString(10, h - 30,  # テキストの書き込み
                     'ご飯は食べましたか？>>'+text)
    paper.drawString(10, h - 60,  # テキストの書き込み
                     '起きた時間は？>>'+text2)
    paper.save()
    send_pdf(file)
