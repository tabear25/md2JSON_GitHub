import os
import json
from git import Repo

def clone_repository(repo_url, clone_dir):
    """GitHubリポジトリをクローン"""
    Repo.clone_from(repo_url, clone_dir)

def find_md_files(dir_path):
    """指定されたディレクトリ内のすべての.mdファイルを検索"""
    md_files = {}
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    md_files[file] = f.read()
    return md_files

def save_to_json(data, json_file):
    """データをJSONファイルとして保存"""
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main(repo_url, clone_dir, json_file):
    clone_repository(repo_url, clone_dir)

    md_files = find_md_files(clone_dir)

    save_to_json(md_files, json_file)

if __name__ == "__main__":
    # ここで設定
    repo_url = 'REPO_URL'
    clone_dir = 'CLONE_REPO_DIR'  
    json_file = 'YOUR_JSON_FILE_NAME'  

    main(repo_url, clone_dir, json_file)
