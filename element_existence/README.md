# Element Existence Test

このディレクトリでは、画面上の特定要素（ボタン、リンク、テキストなど）が  
存在しているかどうか確認するためのテストコードを管理しています。

主に、ページの構成チェックや、  
要素の有無による画面制御テストを目的としています。

## 📚 現在のテスト一覧
- `check_login_button.py`
  ログインページにある「ログイン」ボタンが存在するか確認します。
- `check_nav_after_login.py`
  ログイン後にナビゲーションリンク「マイページ」と
  「ログアウト」ボタンがあるか同時に確認します。

## 🛠 使用技術・ツール
- Python 
- Selenium
- ChromeDriver

## ✍️ 学んだこと
- By.LINK_TEXT：表示されているリンクテキストを簡単に検出！日本語もOK
- try / except：見つからなかった場合の処理
- 直接 `button` を探すのではなく、`form` 内の `button` を狙う形に変更 
- `driver.current_url` を利用してURLの確認を実施。
  - ログイン後の遷移先URLが意図したものと異なり、  クエリパラメータが付与されるケースがあった。
- `WebDriverWait` を用いることで、タイミングのズレに対応できるようになった。
  - ページ遷移後、要素が表示されるまでの待機処理を追加。  


## 🔥 今後追加予定のテスト案
- ログイン後に表示されるナビゲーションリンクの存在確認
 - 複数リンク（例：「予約一覧」など）も同様に確認
- エラー画面に表示される「戻るボタン」の存在確認
- 特定モーダルウィンドウの出現チェック
- 遷移URLの確認テスト

---

## ✍️ 作者
Chihiro（[@chr02-git](https://github.com/chr02-git)）  
学習記録を兼ねてコツコツ少しずつ公開しています📚
