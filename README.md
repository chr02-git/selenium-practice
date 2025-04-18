# Selenium 自動テスト練習

## 📝 概要
PythonとSeleniumを使用して、Google検索を自動で実行するスクリプトです。  
自動化テストやQAエンジニアを目指す学習の一環として取り組みました。

## 💡 使用技術・ツール
- Python
- Selenium
- Google Chrome / chromedriver
- VS Code
- Git / GitHub


## 📁 含まれているテスト
- `google_search/` : Google検索自動化
   -`google_search.py` : Google検索自動化テスト(正常例)
- `login_test/`: ログインフォームの正常・異常テスト
    - `login_success.py`: 正しい認証情報でのログイン
    - `login_invalid.py`: 誤った認証情報でのエラーメッセージ検出(開発中)

## 📚 学び・気づき（Git/GitHub・構成整理）
- フォルダごとに役割を分けることで、プロジェクト全体の見通しが良くなった
  - Google検索テスト／ログインテストでフォルダを分割
  - 今回は少数の小さなテストコードなので同リポジトリで管理
- `.gitignore`を追加して不要ファイルの追跡を防止
- `git init` のタイミングと場所が重要であることを理解した（下位フォルダではなく全体を対象にする）
- `git pull` 時のマージコンフリクト（README.md）を初めて経験し、解消方法を学んだ
- GitHubで構成が崩れたとき、落ち着いて対応すること、構造と履歴を意識して整理し直す力が大切だと実感


## 🔄 今後やりたいこと
- ログイン画面の自動操作→作成中:login_test.py
- エラーメッセージの表示確認テスト
- 特定のリンクを自動クリックして動作確認
- 検索結果のスクレイピングとファイル出力（CSV保存など）


## ✍️ 作者
Chihiro（[@chr02-git](https://github.com/chr02-git)）  
学習記録を兼ねて少しずつ公開しています📚