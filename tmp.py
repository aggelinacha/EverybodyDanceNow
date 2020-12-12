import os
import cv2

for name in os.listdir("results/transfer_all/transfer_all/test_img_1024/"):
    print(name)
    path = os.path.join("results/transfer_all/transfer_all/test_img_1024/", name)
    img = cv2.imread(path)
    res = cv2.resize(img, (512, 256))
    cv2.imwrite(os.path.join("results/transfer_all/transfer_all/test_img_512/", name),
                res)
