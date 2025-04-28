from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ドライバー起動
driver = webdriver.Chrome()

# ログインページにアクセス
driver.get("https://hotel-example-site.takeyaqa.dev/ja/login.html")

# 少し待機
time.sleep(2)

# ログインボタンが存在するかチェック
try:
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    print("✅ ログインボタンが存在します！")
except:
    print("❌ ログインボタンが見つかりませんでした！")

input("確認できたらEnterキーで終了")
driver.quit()
