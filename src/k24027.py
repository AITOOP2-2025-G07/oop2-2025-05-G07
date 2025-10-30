import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img: cv2.Mat = cv2.imread('images/google.png')
    capture_img: cv2.Mat = cv2.imread('images/camera_capture.png')

    if google_img is None or capture_img is None:
        print("画像の読み込みに失敗しました。")
        return

    # 画像サイズを取得
    g_height, g_width, g_channel = google_img.shape
    c_height, c_width, c_channel = capture_img.shape
    print("google.png:", google_img.shape)
    print("camera_capture.png:", capture_img.shape)

    # カメラ画像をgoogle画像サイズにリサイズ
    resized_capture = cv2.resize(capture_img, (g_width, g_height))

    # 出力画像をgoogle_imgのコピーとして初期化
    output_img = np.copy(google_img)

    # 白色部分を置換
    for y in range(g_height):
        for x in range(g_width):
            b, g, r = google_img[y, x]
            # もし白(255,255,255)ならカメラ画像の画素で置換
            if (b, g, r) == (255, 255, 255):
                output_img[y, x] = capture_img[y, x]

    # ##書き込み処理
    cv2.imwrite('output_images/merged_output.png', output_img)
    print("合成画像を保存しました → output_images/merged_output.png")