import os
from datetime import datetime


def get_screenshot_files(src_folder):
    """指定したフォルダからスクリーンショットファイルのリストを取得する"""
    files = [file for file in os.listdir(src_folder) if "スクリーンショット" in file]
    print(
        f"'スクリーンショット'という名前が含まれるファイルを{len(files)}個、{src_folder}から見つけました。"
    )
    return files


def rename_files(src_folder, dst_folder, files):
    """ファイルを新しい名前でリネームする"""
    for file in files:
        src_path = os.path.join(src_folder, file)
        creation_time = os.path.getctime(src_path)
        formatted_time = datetime.fromtimestamp(creation_time).strftime(
            "typing-%Y-%m%d-%H%M"
        )
        new_file_name = f"{formatted_time}.png"
        dst_path = os.path.join(dst_folder, new_file_name)
        os.rename(src_path, dst_path)
        # 20文字以上の場合は省略して表示
        dst_folder_display = (
            (dst_folder[:20] + "...") if len(dst_folder) > 20 else dst_folder
        )
        print(
            f"ファイル'{file}'を'{new_file_name}'にリネームし、'{dst_folder_display}'に移動しました。"
        )


def main():
    src_folder = (
        r"C:\Users\x22u016\OneDrive - 船橋情報ビジネス専門学校\画像\スクリーンショット"
    )
    # 保存先は変更しない
    dst_folder = src_folder
    # 保存先フォルダが存在しない場合は作成する
    os.makedirs(dst_folder, exist_ok=True)
    print(
        f"保存先にフォルダが存在しないため、{dst_folder}という名前のフォルダを作成しました。"
    )
    # スクリーンショットファイルのリストを取得
    screenshot_files = get_screenshot_files(src_folder)
    # スクリーンショットファイルをリネーム
    rename_files(src_folder, dst_folder, screenshot_files)
    print("スクリーンショットファイルの抽出と名前変更の処理が完了しました。")


# このスクリプトを直接実行する場合にのみmain関数を呼び出す
if __name__ == "__main__":
    main()
