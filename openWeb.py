

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
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=580&doclibId=3&pubId=&resourceId=56733c5e-9b0a-4e8c-b222-d8a9400e7a72':13.22, # 红色保密 百年征程 0.3
# 第2课 传承红色基因 弘扬保密传统
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=578&doclibId=3&pubId=&resourceId=b2358834-c24c-41db-bdb6-cbc473c75f1b':6.30, # 1.党的保密工作优良传统 0.14
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=576&doclibId=3&pubId=&resourceId=6270c6f3-fae7-4625-9b1b-fc5764bbde01':4.50, # 2.坚定的理想信念 0.1
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=574&doclibId=3&pubId=&resourceId=374a7ddd-49b5-4a70-890f-9f727d789342':3.52, # 3.强烈的忧患意识 0.08
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=572&doclibId=3&pubId=&resourceId=2af1231f-997e-450b-9b1c-6973a7229a2b':4.42, # 4.严格的纪律约束 0.1
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=570&doclibId=3&pubId=&resourceId=91f436db-4fa6-49c2-8347-8d9628c9c9fa':4.38, # 5.紧紧地依靠人民 0.1
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=568&doclibId=3&pubId=&resourceId=97080222-7653-4100-9587-7421556977e5':5.05, # 6.持续的技术对抗 0.1
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=566&doclibId=3&pubId=&resourceId=25d0e1a9-dbbf-44b5-ac19-9c004f9f3407':4.57, # 7.领导的率先垂范 0.1
# 第3课 “党史上的保密印记”系列
# 'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=592&doclibId=3&pubId=&resourceId=1ac1cf02-5182-40b5-bb20-b2e1686cf57b':2.13, # 1.誓与密码共存亡 0.05
# 'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=590&doclibId=3&pubId=&resourceId=70f222a1-5441-497c-8f84-6105dadd3737':3.40, # 2.革命航船破浪启航 0.08
# 'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=588&doclibId=3&pubId=&resourceId=2a065b94-2a7d-4b8f-b581-1504a2451799':3.40, # 3.手摇发电机的长征之路 0.08
# 'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=586&doclibId=3&pubId=&resourceId=4ed78416-c441-4328-8f64-407d5adfec4b':4.25, # 4.西安事变前夕 0.1
# 'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=584&doclibId=3&pubId=&resourceId=22b35616-8830-400b-a74b-89bfd525f828':4.28, # 5.共和国的谍战玫瑰 0.1
# 'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=582&doclibId=3&pubId=&resourceId=8e703fa2-1592-4c78-8670-e346ff8e9ee5':3.51, # 6.一苏大的保密空城计 0.08

# ［必修］第1课 红线不能触碰底线不能逾越
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=644&doclibId=3&pubId=&resourceId=a91aafa5-d9b7-422e-aaa9-0e0c3045345c':5.47, # 1.利欲熏心窃秘密 锒铛入狱悔莫及
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=642&doclibId=3&pubId=&resourceId=5a744db1-ebb1-440f-91d4-6c29467008a7':6.29, # 2.出售废品莫大意 认真清点防泄密
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=640&doclibId=3&pubId=&resourceId=a3e4d860-934c-4f65-a799-74df608bd250':7.33, # 3.密件岂能随便邮 快递传密栽跟头
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=638&doclibId=3&pubId=&resourceId=1204e5fb-bdee-4a81-8f78-2354634465a1':5.31, # 4.擅携密件出国境 麻痹侥幸毁前程
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=636&doclibId=3&pubId=&resourceId=5ae3afab-bb82-4e78-bed3-beb2384f0ad5':6.39, # 5.私自留存隐患多 贪图方便酿恶果
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=634&doclibId=3&pubId=&resourceId=75029480-ec24-4439-a293-f9a37bec7d8d':5.37, # 6.私人交往有禁忌 泄露秘密违法纪
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=632&doclibId=3&pubId=&resourceId=ab6473b5-a9a7-4001-a89f-9c78441b410f':5.53, # 7.公共网络很便利 严禁使用传秘密
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=628&doclibId=3&pubId=&resourceId=2491d0da-35c7-44b2-b7f1-673c4f25c010':5.52, # 8.违规联网为红颜 依法判刑悔已晚
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=626&doclibId=3&pubId=&resourceId=ad1820c6-079f-48ae-ade7-1f5b2c034359':7.20, # 9.涉密非密有界限 交叉互联埋隐患
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=624&doclibId=3&pubId=&resourceId=c3ba5041-cee1-45e2-944d-b711775eb6c0':5.47, # 10.非密电脑存秘密 拱手相送犯大忌
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=622&doclibId=3&pubId=&resourceId=f585b736-1515-4f22-af37-4e077b6a4f57':7.03, # 11.安全程序防攻击 擅自卸载违法纪
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=620&doclibId=3&pubId=&resourceId=3594f4df-a8e8-43fe-9f94-af2e898b7fba':7.07, # 12.涉密设备要淘汰 擅自处理不应该


# ［必修］第1课 “秒懂保密”系列之涉密人员保密管理
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=514&doclibId=3&pubId=&resourceId=9b84efe2-f8af-47b0-b030-d9d7bbe29a6b':1.58, # 1.涉密人员与涉密岗位
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=516&doclibId=3&pubId=&resourceId=4f19e38c-be2d-4484-8dc5-175abe12038d':2.32, # 2.涉密人员保密审查
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=518&doclibId=3&pubId=&resourceId=9e519ac1-eb92-46ac-b25f-a3d13cf71ce8':2.35, # 3.涉密人员上岗前保密管理
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=520&doclibId=3&pubId=&resourceId=6c52f617-a459-4d7d-b5b9-77995f86872b':2.31, # 4.涉密人员在岗培训、复审与重大事项报告
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=522&doclibId=3&pubId=&resourceId=b381bbf7-1f8e-41e4-9f23-0e9ec53e8908':3.10, # 5.涉密人员出国（境）管理
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=530&doclibId=3&pubId=&resourceId=38d66f3f-e25e-4eb8-a28d-84f1d173767c':2.26, # 6.涉密人员离岗离职保密管理
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=526&doclibId=3&pubId=&resourceId=3bd3300e-8561-4186-ba02-b6323248e9d4':3.10, # 7.涉密人员脱密期管理
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=528&doclibId=3&pubId=&resourceId=1f415688-9796-4495-8910-3c24d05b4540':1.50, # 8.涉密人员义务与权益保障

#［必修］第1课 风险四伏的办公自动化设备
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=3083&doclibId=3&pubId=&resourceId=a347302e-4518-45c3-b565-c638e12dbdfd':31.46, #

# ［必修］ 第1课“密”案解读——保密警示案例专题片
'http://www.baomi.org.cn/bmVideo?id=fc5489db-34c7-4db1-a856-96d501ea5a78&docId=3144&doclibId=3&pubId=&resourceId=4387e160-ae6c-4f89-8be3-291a3ab1da67':27.34

# 这些就有4.38学时了

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
            time.sleep(1)
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
    time.sleep(4)
    
    # 创建子线程
    thread1 = childThread(1, "chrome", url)
    thread2 = childThread(2, "play", url)

    # 开启线程
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    

print("Exiting Main Thread")
