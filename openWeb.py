

import time
import os
import io
import webbrowser
# import ddddocr
# import pyautogui
import win32api
import win32con
import math

import threading

urlAndTime = {
# ［必修］第1课 红色保密 百年征程
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=580&doclibId=3&pubId=&resourceId=56733c5e-9b0a-4e8c-b222-d8a9400e7a72':13.22, # 红色保密 百年征程
# 第2课 传承红色基因 弘扬保密传统
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=578&doclibId=3&pubId=&resourceId=b2358834-c24c-41db-bdb6-cbc473c75f1b':6.30, # 1.党的保密工作优良传统
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=576&doclibId=3&pubId=&resourceId=6270c6f3-fae7-4625-9b1b-fc5764bbde01':4.50, # 2.坚定的理想信念
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=574&doclibId=3&pubId=&resourceId=374a7ddd-49b5-4a70-890f-9f727d789342':3.52, # 3.强烈的忧患意识
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=572&doclibId=3&pubId=&resourceId=2af1231f-997e-450b-9b1c-6973a7229a2b':4.42, # 4.严格的纪律约束
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=570&doclibId=3&pubId=&resourceId=91f436db-4fa6-49c2-8347-8d9628c9c9fa':4.38, # 5.紧紧地依靠人民
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=568&doclibId=3&pubId=&resourceId=97080222-7653-4100-9587-7421556977e5':5.05, # 6.持续的技术对抗
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=566&doclibId=3&pubId=&resourceId=25d0e1a9-dbbf-44b5-ac19-9c004f9f3407':4.57, # 7.领导的率先垂范
# 第3课 “党史上的保密印记”系列
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=592&doclibId=3&pubId=&resourceId=1ac1cf02-5182-40b5-bb20-b2e1686cf57b':2.13, # 1.誓与密码共存亡
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=590&doclibId=3&pubId=&resourceId=70f222a1-5441-497c-8f84-6105dadd3737':3.40,
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=588&doclibId=3&pubId=&resourceId=2a065b94-2a7d-4b8f-b581-1504a2451799':3.40,
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=586&doclibId=3&pubId=&resourceId=4ed78416-c441-4328-8f64-407d5adfec4b':4.25,
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=584&doclibId=3&pubId=&resourceId=22b35616-8830-400b-a74b-89bfd525f828':4.28 # 5.共和国的谍战玫瑰

}

# MacOS
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
# chrome_path = 'E:/Software/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

def image2byte(image):
    '''
    图片转byte
    image: 必须是PIL格式
    image_bytes: 二进制
    '''
    # 创建一个字节流管道
    img_bytes = io.BytesIO()
    # 将图片数据存入字节流管道， format可以按照具体文件的格式填写
    image.save(img_bytes, format="JPEG")
    # 从字节流管道中获取二进制
    image_bytes = img_bytes.getvalue()
    return image_bytes

#模拟鼠标点击
def mouse_click(x, y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

# 主线程
class mainThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
    def run(self):
        # 先确保chrome被关闭了
        os.system("taskkill /im chrome.exe /f")
        time.sleep(2)

        # 创建子线程
        thread1 = childThread(1, "chrome", self.url)
        thread2 = childThread(2, "play", self.url)

        # 开启线程
        thread1.start()
        thread2.start()



# 子线程
class childThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, url):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.url = url
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        if(self.name == "chrome"):
            

            url = self.url
            chrome_path = 'E:/Software/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            print("chrome threading over")
        elif(self.name == "play"):

            # # 先给线程加一个锁
            # threading.Lock().acquire()

            # 休眠一段时间，确保chrome完全加载完成
            time.sleep(6)

            # 模拟鼠标点击
            mouse_click(443, 1001) # 点击开始播放图标 不同的人可能不太一样，我是根据我的屏幕浏览器全屏

            # 获取sleep时间
            video_time = urlAndTime[self.url]
            sleep_time = int(video_time)*60 + int(math.modf(video_time)[0]*100)
            print("sleep time = %f"%sleep_time)
            time.sleep(sleep_time + 5) # 多看5秒钟，确保容错

            


            

            ###
            # OCR准确率不够，手写吧
            ###

            # win32api.keybd_event(17,0,0,0) #ctrl键位码是17
            # win32api.keybd_event(65,0,0,0) #A键位码是65
            # time.sleep(0.1)
            # win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
            # win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)

            # img = pyautogui.screenshot(region=(450,990, 110, 34)) # 得到截图区域
            # img.save("./1.jpg")

            # ocr = ddddocr.DdddOcr()
            # video_time = ocr.classification(image2byte(img)) # 得到截图区域文本
            # print("get video time%s"%video_time)

            # 关闭chrome
            os.system("taskkill /im chrome.exe /f")

            # # 释放锁，开启下一个线程
            # threading.Lock().release()

for url in urlAndTime:
    # main_thread = childThread(2, "play", url)
    # main_thread.start()
    # main_thread.join()

    # 先确保chrome被关闭了
    os.system("taskkill /im chrome.exe /f")
    time.sleep(2)
    
    # 创建子线程
    thread1 = childThread(1, "chrome", url)
    thread2 = childThread(2, "play", url)

    # 开启线程
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    

print("Exiting Main Thread")
