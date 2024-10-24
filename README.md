# これはなに
- 指定したGitHubリポジトリをクローンし、リポジトリ内に含まれるすべての`.md` を検索して、その内容をJSON形式に変換して保存します。
- ユーザーがリポジトリのURL、クローン先のディレクトリ、および出力するJSONファイルを指定することが可能です。

## 機能
- GitHubリポジトリをクローンする
- `.md`を再帰的に検索
- `.md`の内容をJSON形式で保存

## 必要条件
- Python 3.x
- [GitPython](https://gitpython.readthedocs.io/en/stable/) 

# 使い方
- `main.py`の以下の部分にそれぞれGitHubリポジトリのURLとクローン先のディレクトリ、JSONファイル名を入力してください

```
repo_url = 'REPO_URL'
clone_dir = 'CLONE_REPO_DIR'  
json_file = 'YOUR_JSON_FILE_NAME'  
```