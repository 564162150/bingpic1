import urllib.request
import requests
import os.path
import ctypes

def save_img(img_url,dirname):
    try:
        #保存图片到磁盘文件夹dirname中
        if not os.path.exists(dirname):
            print('文件夹',dirname,'不存在，请重新建立')
            os.makedirs(dirname)
        #获得图片文件名，包括后缀
        basename=os.path.basename(img_url)
        #拼接目录与文件名，得到图片路径
        basename=basename.replace('th?id=OHR.','')
        basename=basename.replace('&rf=LaDigue_1920x1080.jpg&pid=hp','')
        filepath=os.path.join(dirname,basename)
        #下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url,filepath)

    except IOError as e:
        print('文件操作失败',e)
    except Exception as e:
        print('错误',e)
    print('Save',filepath,'successfully!')

    return filepath

def get_img_url(raw_img_url="https://area.sinaapp.com/bingImg/"):
    r=requests.get(raw_img_url)
    img_url=r.url#"https://cn.bing.com/th?id=OHR.OldPatriarchTree_ZH-CN8818146190_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp"##得到图片文件的网址
    print('img_url:',img_url)
    return img_url

def set_img_as_wallpaper(filepath):
    ctypes.windll.user32.SystemParametersInfoW(20,0,filepath,0)

if __name__ == '__main__':
    dirname='D:/CODE/bingpic/bingimg/'#图片保存位置
    img_url=get_img_url()
    filepath =save_img(img_url,dirname)
    set_img_as_wallpaper(filepath)