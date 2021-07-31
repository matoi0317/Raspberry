# coding:utf-8
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A3, portrait
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
import speech_recognition as sr
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

r = sr.Recognizer()
with sr.AudioFile("sample2.wav") as source:
    audio = r.record(source)
text = r.recognize_google(audio, language="ja-JP")

class Test():
    def __init__(self):
        self.c = canvas.Canvas("test.pdf", pagesize=portrait(A3))
        self.height, self.width = A3
        self.fontname = 'hogehoge'
        # pdfmetrics.registerFont(TTFont(self.fontname, "C:\\Windows\\Fonts\\msgothic.ttc"))
        self.c.setFont(self.fontname, 10)

    # def __del__(self):
    #     del self.c
    #
    # def drawText(self):
    #     self.c.drawString(0, self.height - 5 * mm, "ああああ")
    def drawTable(self):
        pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
        pdf.setFont('HeiseiKakuGo-W5', 12)
        style = ParagraphStyle(name='Normal', fontName=self.fontname, fontSize=20, leading=20)
        line1 = Paragraph(text,style)
        data = [
            [line1],
        ]

        table = Table(data,colWidths=(20*mm,30*mm,40*mm))

        table.setStyle(TableStyle([
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))

        table.wrapOn(self.c, 50*mm, 10*mm)
        table.drawOn(self.c, 50*mm, 10*mm)

if __name__== '__main__':
    test = Test()
    test.drawText()
    test.drawTable()
    test.c.save()
    del test