# coding:utf-8
import speech_recognition as sr
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4, portrait


r = sr.Recognizer()
with sr.AudioFile("sample2.wav") as source:
    audio = r.record(source)
text = r.recognize_google(audio, language="ja-JP")
# word = [text[i: i+3] for i in range(0, len(text), 20)]
# print(word)

file_name = 'audio.pdf'    # ファイル名を設定
pdf = canvas.Canvas(file_name, pagesize=portrait(A4))    # PDFを生成、サイズはA4
pdf.saveState()    # セーブ
pdf.setAuthor('sample')
pdf.setTitle('TEST')
pdf.setSubject('TEST')
### フォント、サイズを設定 ###
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
pdf.setFont('HeiseiKakuGo-W5', 12)

### 文字を描画 ###
pdf.drawString(1*cm, 26*cm, text)

pdf.setFont('HeiseiKakuGo-W5', 12)    # フォントサイズの変更
width, height = A4  # A4用紙のサイズ
pdf.drawCentredString(width / 2, height - 2*cm, 'HelloWorld')


pdf.restoreState()
pdf.save()