import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODY4Mzc5MzI0OTM0NDE0Mzg2.YPuzRA.H-vAvv76eWQpM14oBmeI48DOp2g'
CHANNEL_ID = 865848605238493207 #チャンネルID

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

# 任意のチャンネルで挨拶する非同期関数を定義
async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('おはよう！')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)