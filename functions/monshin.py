# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.pagesizes import A4, portrait
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
import datetime
from functions.firebase import send_pdf
import sys

def Create_pdf(text1, text2, text3, text4,text5,text6,text7,text8,text9,user_id,tempureture):
    dt_now = datetime.datetime.now()
    datetime_format = dt_now.strftime("%Y%m%d%H%M%S")
    registerFont(TTFont('GenShinGothic',
                        './data/GenShinGothic-Monospace-Medium.ttf'))

    file = datetime_format + 'test111.pdf'  # 出力ファイル名を設定

    paper = canvas.Canvas(file)  # 白紙のキャンバスを用意
    paper.saveState()  # 初期化
    paper.setFont('GenShinGothic', 24)  # フォントを設定

    paper.drawString(60, 770, 'わかるって　問　診　票')  # 書き出し(横位置, 縦位置, 文字)

    data = [
        ['ふりがな', '  女'],
        ['柴沼纏', ''],
        ['生年月日　　　　　　　　　　　　　　　　　　2005年　03月　　17日生　（満　　　歳）', ''],
    ]
    table = Table(data, colWidths=(100 * mm, 20 * mm), rowHeights=(7 * mm, 20 * mm, 7 * mm))
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (1, 2), 'GenShinGothic', 8),
        ('BOX', (0, 0), (1, 2), 1, colors.black),
        ('INNERGRID', (0, 0), (1, 2), 1, colors.black),
        ('SPAN', (0, 2), (1, 2)),
        ('SPAN', (1, 0), (1, 1)),
        ('VALIGN', (0, 0), (1, 2), 'MIDDLE'),
        ('VALIGN', (0, 1), (0, 1), 'TOP'),
    ]))
    table.wrapOn(paper, 20 * mm, 232 * mm)
    table.drawOn(paper, 20 * mm, 232 * mm)

    # カルテの内容
    data = [
        ['ご飯は食べましたか？', text1],
        ['何時に起きましたか？', text2],
        ['処方された薬は飲みましたか？', text3],
        ['体に何かしらの症状はありますか？', text4],
        ['熱はありますか？', text5],
        ['喉の痛みはありますか？', text6],
        ['排尿はしましたか？', text7],
        ['便秘気味ですか？', text8],
        ['お腹の痛みはありますか？', text9],
    ]
    table = Table(data, colWidths=(60 * mm, 100 * mm), rowHeights=7.5 * mm)
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'GenShinGothic', 11),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (1, 0), 'MIDDLE'),
    ]))
    table.wrapOn(paper, 20 * mm, 200 * mm)
    table.drawOn(paper, 20 * mm, 200 * mm)

    # 1枚目終了
    paper.save()
    send_pdf(file, user_id,tempureture)