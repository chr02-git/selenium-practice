from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chromeドライバーの起動
driver = webdriver.Chrome()

# ログインページへアクセス
driver.get("https://hotel-example-site.takeyaqa.dev/ja/login.html")

# 要素を取得して入力
driver.find_element(By.NAME, "email").send_keys("iro@example.com")
driver.find_element(By.NAME, "password").send_keys("pass")

# ログインボタンをクリック（buttonタグのtype="submit"）
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

# ログイン失敗時のエラー表示確認
error_message = driver.find_element(By.CLASS_NAME, "invalid-feedback").text

if "違います。" in error_message:
    print("✅ エラーメッセージ確認済み：", error_message)
else:
    print("❌ エラーが想定通りに表示されませんでした")

# 少し待機して、ログイン後の画面確認
time.sleep(3)

# ブラウザを閉じる
input("ブラウザを確認したらEnterを押してください")
driver.quit()

