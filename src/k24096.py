import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def k24096():

    # 繧ｫ繝｡繝ｩ繧ｭ繝｣繝励メ繝｣螳溯｡径
    app = MyVideoCapture()
    app.run()

    # 逕ｻ蜒上ｒ繝ｭ繝ｼ繧ｫ繝ｫ螟画焚縺ｫ菫晏ｭ�
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') # 蜍穂ｽ懊ユ繧ｹ繝育畑縺ｪ縺ｮ縺ｧ謠仙�譎ゅ↓縺薙�陦後ｒ豸医☆縺薙→
    # capture_img : cv2.Mat = "implement me"

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    for x in range(g_width):
        for y in range(g_hight):
            g, b, r = google_img[y, x]
            # 繧ゅ＠逋ｽ濶ｲ(255,255,255)縺�縺｣縺溘ｉ鄂ｮ縺肴鋤縺医ｋ
            if (b, g, r) == (255, 255, 255):
                pass