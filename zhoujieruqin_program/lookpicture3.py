# encoding=utf-8
import os

def main():
    ## 图片目录
    all_picture = []
    for root, dirs, files in os.walk("jiance"):
        for f in files:
            all_picture.append(os.path.join(root, f))

    ## 获得大小图显示
    all_picture.sort()
    num = 0
    for file_path in all_picture:
        if len(file_path.split("_")) == 7: #找小图
            base_name = os.path.basename(file_path)
            items = base_name.split("_")
            if str(items[-3]) == "1" or str(items[-3]) == "2" or str(items[-3]) == "4":
                continue
            else:
                num += 1
    print("剔除掉检测为红、白、黄安全帽之后的数量：",num)


if __name__ == "__main__":
    main()
