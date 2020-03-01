# encoding = utf-8
import os
import cv2

def make_directory(root, name):
    filepath = os.path.join(root, name)
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    return filepath

def main():
    all_picture = []
    for root, dirs, files in os.walk("refueller_1"):
        for f in files:
            all_picture.append(os.path.join(root, f))

    i = 0
    while True:
        file_path = all_picture[i]
        img = cv2.imread(file_path)
        base_name = os.path.basename(file_path)
        print(file_path)
        cv2.imwrite("tmp.jpg" , img)
        img = cv2.imread("tmp.jpg")
        img = cv2.resize(img, (1200,680), interpolation=cv2.INTER_CUBIC)
        cv2.imshow("data_img",img)
        k = cv2.waitKey(0)
        print(k)
        # 保存到文件夹gun_in
        if k == 115:
            cv2.imwrite(make_directory(".", "gun_in") + "/" + base_name, img)
            i += 1
        #保存到文件夹gun_out
        elif k == 108:
            cv2.imwrite(make_directory(".", "gun_out") + "/" + base_name, img)
            i += 1
        #保存到文件夹hide
        elif k == 104:
            cv2.imwrite(make_directory(".", "hide") + "/" + base_name, img)
            i += 1
        elif k == ord('1'):  #左，上一张
            i -= 1
        elif k == ord('5'):  #上，上一张
            i -= 1
        elif k == ord('3'):  #右，下一张
            i += 1
        elif k == ord('2'):  #下，下一张
            i += 1
if __name__ == "__main__":
    main()