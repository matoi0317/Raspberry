# coding: utf-8
# import requests
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://karute-81f3c.web.app/information")
a = driver.get_cookie("name")
print(a)

# # URLから、requestsのオブジェクト作成
# url = "https://karute-81f3c.web.app/information"
# session = requests.session()
# response = session.get(url)
#
# # cookieを取得
# cookie = response.cookies
# print(cookie)