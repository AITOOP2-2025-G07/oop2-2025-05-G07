
import sys
import os
import numpy as np
import cv2

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_module.K24107.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    if google_img is None:
        raise FileNotFoundError("images/google.png が見つかりません。")
    
    capture_img: cv2.Mat = app.get_img()
    if capture_img is None:
        raise ValueError("カメラ画像が取得できませんでした。'q'キーで撮影を完了してください。")


    g_height, g_width, g_channel = google_img.shape
    c_height, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    # 出力画像のコピーを作成
    new_img = google_img.copy()

    for x in range(g_width):
        for y in range(g_height):
            g, b, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                # 高さや幅が合わないので、capture_imgを繰り返すために高さを高さで割って、幅を幅で割る
                new_img[y, x] = capture_img[y % c_height, x % c_width]


    cv2.imwrite('output_images/lecture05_01_k24107.png', new_img)
    print(" 完了: output_images/lecture05_01_k24107.png に保存しました。")

if __name__ == "__main__":
    lecture05_01()
