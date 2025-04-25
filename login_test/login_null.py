from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://hotel-example-site.takeyaqa.dev/ja/login.html")

# 入力欄を空のまま送信
driver.find_element(By.NAME, "email").clear()
driver.find_element(By.NAME, "password").clear()
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# エラーメッセージの表示を待って取得
time.sleep(2)
error = driver.find_element(By.CLASS_NAME, "invalid-feedback").text
print("エラーメッセージ：", error)

# ブラウザを閉じる
input("ブラウザを確認したらEnterを押してください")
driver.quit()
