# coding: utf-8
import discord
from discord.ext import tasks

TOKEN = "ODY4Mzc5MzI0OTM0NDE0Mzg2.YPuzRA.H-vAvv76eWQpM14oBmeI48DOp2g" #トークン
CHANNEL_ID = 865848605238493207 #チャンネルID

#接続に必要なオブジェクトを生成
client = discord.Client()
print(vars(client))
# 60秒に一回ループ
@tasks.loop(seconds=10)
async def loop():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send("時間だよ")

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)



# discord_webhook_url = 'https://discord.com/api/webhooks/865849265682513921/9Fv7jOzLllR1Ky4I7YC3mqyw8WgrlPhwTFEtQjKY2PRhIs9GVdgxyIsdGcQY_EpoxfST'
#
# data = {"content": "aaaaaaaa"}
# requests.post(discord_webhook_url, data=data)