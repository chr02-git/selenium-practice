from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# ログインが成功したページの推移先が正しいか確認
print("現在のURL:", driver.current_url)

# 要素の確認
links_to_check = [
    {"type": "link", "text": "マイページ"},
    {"type": "button", "selector": "button.btn btn-outline-success my-2 my-sm-0"}
]

for link in links_to_check:
    try:
        # リンクの場合
        if link["type"] == "link":
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, link["text"]))
            )
            print(f"✅ '{link['text']}' が見つかりました！")
        
        # ボタンの場合
        elif link["type"] == "button":
        # form 内の button を取得
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form#logout-form button"))
        )
            print("✅ ログアウトボタンが見つかりました！")
    
    except:
        print(f"❌ '{link['text'] if 'text' in link else 'ボタン'}' が見つかりませんでした")

# 少し待機して、ログイン後の画面確認
time.sleep(3)

# ブラウザを閉じる
input("ブラウザを確認したらEnterを押してください")
driver.quit()

