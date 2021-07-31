import requests, json
import time


webhook_url = 'https://discord.com/api/webhooks/869158930960482304/UpaG7D8lJQmp8--FVmOzzOyFTt3vTwddLOHzQf5xgKj3j3NZJEp5zAiDrip8-RnlrUmm'
main_content = {'content': '送るテキスト'}
headers = {'Content-Type': 'application/json'}

for i in range(10):
    response = requests.post(webhook_url, json.dumps(main_content), headers=headers)
    time.sleep(5)