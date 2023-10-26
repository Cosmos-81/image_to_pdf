from PIL import Image
import os

def image_to_pdf(input_folder_path, output_folder_path):

    # フォルダ内のjpgファイルを取得
    jpg_files = [f for f in os.listdir(input_folder_path) if f.endswith('.jpg')]

    # ファイル名(昇順)にソート
    jpg_files.sort()

    pdf_filename = os.path.basename(input_folder_path) + ".pdf"
    pdf_filename = os.path.join(output_folder_path, pdf_filename)

    # 画像をPDFに変換
    images = []
    for file_name in jpg_files:
        file_path = os.path.join(input_folder_path, file_name)
        img = Image.open(file_path)
        if img.mode == "RGBA":
            img = img.convert("RGB")
        images.append(img)
    images[0].save(pdf_filename, save_all=True, append_images=images[1:])