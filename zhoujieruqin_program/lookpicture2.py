# encoding=utf-8
import os
import cv2
import numpy as np


def make_directory(root, name):
    filepath = os.path.join(root, name)
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    return filepath


def concat(img1, img2):
    h1 = img1.shape[0]
    w1 = img1.shape[1]
    h2 = img2.shape[0]
    w2 = img2.shape[1]
    h = h2
    if h1 > h2:
        h = h1
    w = w1 + w2
    img = np.zeros((h, w, 3))
    img[:h1, :w1, :] = img1
    img[:h2, w1:, :] = img2
    return img


def main():
    ## 图片目录
    all_picture = []
    for root, dirs, files in os.walk("jiance"):
        for f in files:
            all_picture.append(os.path.join(root, f))

    ## 获得大小图显示
    all_picture.sort()
    all_picture2 = []
    for file_path in all_picture:
        #判断是否为小图
        '''
        img = cv2.imread(file_path)
         print(img.shape)
         if img.shape[0] < 720 or img.shape[1] < 1280:
        '''
        if len(file_path.split("_")) == 7: #判断是小图，这样处理 读图更快
            big_file_path = file_path
            dir_name = os.path.dirname(big_file_path)
            base_name = os.path.basename(big_file_path)
            items = base_name.split("_")
            if str(items[-3]) == "1" or str(items[-3]) == "2" or str(items[-3]) == "4":
                continue
            del items[-3]
            base_name = "_".join(items)
            big_file_path = os.path.join(dir_name, base_name)
            print(big_file_path)
            if not os.path.exists(big_file_path):
                continue
            all_picture2.append(file_path)

    i = 0
    while True:
        file_path = all_picture2[i]
        ## 小图
        img2 = cv2.imread(file_path)
        ## 找到大图
        # big_file_path = file_path.replace("small","big")
        big_file_path = file_path
        dir_name = os.path.dirname(big_file_path)
        base_name = os.path.basename(big_file_path)
        items = base_name.split("_")
        if str(items[-3]) == "1" or str(items[-3]) == "2" or str(items[-3]) == "4":
            continue
        del items[-3]
        base_name = "_".join(items)
        big_file_path = os.path.join(dir_name, base_name)
        print(file_path)
        print(big_file_path)
        # if not os.path.exists(big_file_path):
        #     continue
        img1 = cv2.imread(big_file_path)
        img = concat(img1, img2)
        cv2.putText(img, file_path, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # cv2.imwrite("./result/"+base_name,img)
        cv2.imwrite("tmp.jpg", img)
        img = cv2.imread("tmp.jpg")
        img = cv2.resize(img, (1200, 800), interpolation=cv2.INTER_CUBIC)
        cv2.imshow("area-img", img)

        k = cv2.waitKey(0)
        print(k)
        if k == 115:
            ## 保存图片
            cv2.imwrite(make_directory(".", "results_error") + "/" + base_name, img1)
            i += 1
        ##保存失真图片
        elif k == 100:
            cv2.imwrite(make_directory(".", "distortions_error") + "/" + base_name, img1)
            i += 1
        elif k == ord('1'):  ## 左
            i -= 1
        elif k == ord('5'):  ## 上
            i -= 1
        elif k == ord('3'):  ## 右
            i += 1
        elif k == ord('2'):  ## 下
            i += 1


if __name__ == "__main__":
    main()
