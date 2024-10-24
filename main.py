import os
import json
from git import Repo
from tqdm import tqdm  # プログレスバー用

def clone_repository(repo_url, clone_dir):
    """GitHubリポジトリをクローン"""
    print("Cloning the repository...")
    Repo.clone_from(repo_url, clone_dir)
    print("Repository cloned successfully!")

def find_md_files(dir_path):
    """指定されたディレクトリ内のすべての.mdファイルを検索"""
    md_files = {}
    # 正確に.mdファイルの総数をカウント
    total_files = sum(1 for _, _, files in os.walk(dir_path) for f in files if f.endswith('.md'))
    
    with tqdm(total=total_files, desc="Processing .md files", unit="file") as pbar:
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            # ファイルの相対パスをキーに使用
                            relative_path = os.path.relpath(file_path, dir_path)
                            md_files[relative_path] = f.read()
                        print(f"Processed file: {relative_path}")  # 処理されたファイルを表示
                    except Exception as e:
                        print(f"Error processing file {file_path}: {e}")  # エラーメッセージを表示
                    pbar.update(1)  # プログレスバーの更新
    return md_files

def save_to_json(data, json_file):
    """データをJSONファイルとして保存"""
    print("Saving to JSON...")
    try:
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data saved to {json_file}")
    except Exception as e:
        print(f"Error saving JSON file {json_file}: {e}")

def main(repo_url, clone_dir, json_file):
    # クローン処理
    clone_repository(repo_url, clone_dir)

    # .mdファイルを探してプログレスバー付きで処理
    md_files = find_md_files(clone_dir)

    # JSONファイルとして保存
    save_to_json(md_files, json_file)

if __name__ == "__main__":
    # ここで設定
    repo_url = 'REPO_URL'
    clone_dir = 'CLONE_REPO_DIR'  
    json_file = 'YOUR_JSON_FILE_NAME'  

    main(repo_url, clone_dir, json_file)
