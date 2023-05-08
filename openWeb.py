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

######################
# 新的方法不用输入用户浏览器Path了，可以直接调用系统默认浏览器
# 需要用户设置的唯一参数（鼠标点击位置），即开始播放的按钮在屏幕的坐标位置
# 打开一个视频，然后全屏截图之后在画图打开，切换到画笔
# 然后看左下角显示的数字，分别就是x和y

# 有不看的视频注释即可
######################
x = 465
y = 1005

urlAndTime = {
# ［必修］第1课 红色保密 百年征程
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396235&siteId=95&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=02ad4bf6-5f14-4d4b-8b46-d215f409437a&resourceId=4b301a70-ab97-487c-ab58-9099113fa0c4':3.34, # ［必修］01 毛泽东同志的一幅题词
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&docId=9396237&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=02ad4bf6-5f14-4d4b-8b46-d215f409437a&resourceId=86439328-95e7-4423-a112-9cd7b27d539a':3.39, # ［必修］02 一个严守保密纪律的共产党员——周恩来
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&docId=9396241&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=02ad4bf6-5f14-4d4b-8b46-d215f409437a&resourceId=b29f535f-19eb-4568-ae64-308dcf0ad10b':4.09, # ［必修］03 干惊天动地事，做隐姓埋名人-黄旭华讲述保密往事
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396245&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=02ad4bf6-5f14-4d4b-8b46-d215f409437a&resourceId=406cb6c6-3fe8-4ade-a1b7-f0669e13e5ba':2.57,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396247&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=02ad4bf6-5f14-4d4b-8b46-d215f409437a&resourceId=9a75a4cc-170c-4e69-aeb7-843fe039af56':3.00,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396261&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=aa17bff0-4f56-41a4-a48b-36a3e225e4c5&resourceId=15e45aa7-b12e-43c3-8594-ae9ae9f03b2e':1.00,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396263&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=aa17bff0-4f56-41a4-a48b-36a3e225e4c5&resourceId=b0418362-a656-45e0-817a-2d29e984332b':1.00,
'http://www.baomi.org.cn/bmImage?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396291&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&resourceId=ce4915d1-24a2-4231-b917-1c3f1e0025b5':0.05,
'http://www.baomi.org.cn/bmImage?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396297&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&resourceId=3e41c7c6-df7d-4eff-aaa9-d99185c1a9fa':0.05,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396610&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=c598cb7a-1ca1-4475-a287-913a6d893e9e':1.14,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396662&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=b298555c-a51b-43ab-bfb8-637c4336f5fe':2.36,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396614&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=48a7fc91-ee46-4eae-83a0-b01c8971f42d':1.11,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396652&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=6b225d59-b72c-494c-b723-2e4776734afb':2.05,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396652&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=6b225d59-b72c-494c-b723-2e4776734afb':1.55,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396644&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=381bd65e-3e5b-437e-af0f-2ab838a87289':1.33,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396618&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=e17fc6e7-501d-440e-9b4d-1452d45e51f1':1.05,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396626&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=401d774a-2026-44f4-ae77-5934de870347':1.08,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396642&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=f96fe100-a30c-465b-8b36-782ab4784af5':1.36,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396656&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=6afdbd42-cd8d-489b-9a44-26a1303e77af':2.50,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396606&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=31abd8cc-c01a-4430-b916-f5c91ad71238':1.05,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396620&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=9aa1be35-b47e-4f8a-8a86-3abe5cd3c17c':1.31,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396650&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=33b16902-1570-4b77-b833-30619af978e3':2.44,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396616&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=80d26d36-85f1-464a-b003-c73822521f23':1.45,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396636&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=36d99c10-82ba-441d-843a-ccb076e0c244':1.31,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396630&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=e1886f5e-77fa-4617-9a01-df7bf7074417':1.32,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396624&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=66c5fcea-dd8e-45ee-b2ff-3c9a70219e63':1.26,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396608&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=6d3f2b2d-5c55-4f97-822b-0f20511565f3':1.35,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396667&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=dce76a57-cf3b-4c12-81ca-7101f92d80b9&resourceId=677cb38c-05c4-4319-9a07-28a0041261ff':5.12,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396669&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=dce76a57-cf3b-4c12-81ca-7101f92d80b9&resourceId=57778a2c-5dbd-4865-9f00-f464ec99bd8d':15.43,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396664&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=dce76a57-cf3b-4c12-81ca-7101f92d80b9&resourceId=84a676fd-d3fe-4c95-8645-0d31f4a75845':4.39,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396658&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=dce76a57-cf3b-4c12-81ca-7101f92d80b9&resourceId=a27c6d09-eac5-4f7d-b7bc-cb6218c1035d':3.28,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396646&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=dce76a57-cf3b-4c12-81ca-7101f92d80b9&resourceId=b495dc7b-ea00-4176-83d5-3d6a6c9242aa':1.46,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396660&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=dce76a57-cf3b-4c12-81ca-7101f92d80b9&resourceId=a757be22-73d4-4f5d-9691-c3c36f4f0e98':3.48,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396314&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=38745c0e-3170-40be-8b11-3314e3e71cc4&resourceId=1d2fa8ea-45a5-48eb-900f-3686f4d3dbdc':3.13,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396312&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=38745c0e-3170-40be-8b11-3314e3e71cc4&resourceId=e3966d75-811c-4acd-8078-86870b6f4c0e':3.01,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396309&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=38745c0e-3170-40be-8b11-3314e3e71cc4&resourceId=faa6e69b-ea76-4a6e-95a6-5ee4a911de65':2.57,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396307&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=38745c0e-3170-40be-8b11-3314e3e71cc4&resourceId=96a17f45-67b8-4b84-b5e1-ef628b47cea7':3.57,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396323&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=770c6f80-1836-49eb-a80d-ea729fd92659&resourceId=c51a68a7-1967-4d98-8495-ff26c70c735d':2.37,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396321&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=770c6f80-1836-49eb-a80d-ea729fd92659&resourceId=10e8e72b-5322-4d13-9a61-399ef61045b2':2.42,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396319&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=770c6f80-1836-49eb-a80d-ea729fd92659&resourceId=8a475b1d-179e-4549-a28c-e5f3e348f11a':3.46,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396317&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=770c6f80-1836-49eb-a80d-ea729fd92659&resourceId=7e07aef4-dbe0-4315-9fd1-544ae0a2845b':3.04,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396690&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=16757c09-3670-4afd-b879-e30f2c66859a&resourceId=b98980e3-eb45-43b5-89a3-c7adae15d0c3':12.36,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396682&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=16757c09-3670-4afd-b879-e30f2c66859a&resourceId=75a8d2c0-af69-4af6-aebb-0b77c1580f9a':8.14,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396688&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=16757c09-3670-4afd-b879-e30f2c66859a&resourceId=09e3de26-efcc-42cc-a897-81fac3c3ed1b':10.25,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396692&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=5b214b93-b723-4894-8ea1-fab3b4375233&resourceId=b94631f9-367c-4a43-8587-0281b8113c4e':14.17,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396684&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=5b214b93-b723-4894-8ea1-fab3b4375233&resourceId=1a00d8d3-a3cd-4f27-b7d0-d1b6003e2fb1':8.19,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396686&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=5b214b93-b723-4894-8ea1-fab3b4375233&resourceId=b90f7753-6688-49d3-87ba-b4a4de0c698c':8.58,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396589&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=5d9d4a20-6a5b-42b8-8542-dab589b8d67b':4.18,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396591&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=05506b68-b97d-4c24-8ef2-a5ac95efd445':4.33,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396587&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=b7c5fad6-6654-4cc1-ad0e-6ba6e1633b90':4.01,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396596&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=e0744709-90dd-43e5-b98c-5b243cb20fd9':3.26,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396598&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=276b6c77-e9d4-42d6-80cf-83336bed10be':3.54,
'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396600&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=b545c846-44b4-46f4-ad3b-cb7c287b2484':4.14



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
            time.sleep(0.1)
            url = self.url

            # 老方法需要填写用户本地浏览器地址，新方法直接调用用户默认浏览器
            # chrome_path = 'C://Users//CZY//AppData//Local//Google//Chrome//Application//chrome.exe %s'
            # webbrowser.get(chrome_path).open(url)

            # 新方法，用户默认打开网页就行了
            webbrowser.open(url)

            print("chrome threading over")
        elif(self.name == "play"):

            # # 先给线程加一个锁
            # threading.Lock().acquire()

            # 休眠一段时间，确保chrome完全加载完成
            time.sleep(8)

            # 模拟鼠标点击
            mouse_click(x, y) # 点击开始播放图标 不同的人可能不太一样，我是根据我的屏幕浏览器全屏

            # 获取sleep时间
            video_time = urlAndTime[self.url]
            sleep_time = int(video_time)*60 + int(math.modf(video_time)[0]*100)
            print("sleep time = %f"%sleep_time)
            time.sleep(sleep_time + 8) # 多看5秒钟，确保容错


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
    time.sleep(2.5)
    
    # 创建子线程
    thread1 = childThread(1, "chrome", url)
    thread2 = childThread(2, "play", url)

    # 开启线程
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    

print("Exiting Main Thread")
