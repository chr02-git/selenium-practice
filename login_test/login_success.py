from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chromeドライバーの起動
driver = webdriver.Chrome()

# ログインページへアクセス
driver.get("https://hotel-example-site.takeyaqa.dev/ja/login.html")

# 要素を取得して入力
driver.find_element(By.NAME, "email").send_keys("ichiro@example.com")
driver.find_element(By.NAME, "password").send_keys("password")

# ログインボタンをクリック（buttonタグのtype="submit"）
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

# 少し待機して、ログイン後の画面確認
time.sleep(3)

# ブラウザを閉じる
input("ブラウザを確認したらEnterを押してください")
driver.quit()

