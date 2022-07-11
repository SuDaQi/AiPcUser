import pyautogui
import time
import xlrd
import pyperclip
import random

#鼠标点击事件
def mouseClick(img):
    clickTimes=0.5
    offsetStrength=0.25
    imgPos = pyautogui.locateCenterOnScreen(img, confidence=0.9)
    if imgPos is not None:
        size = pyautogui.locateOnScreen(img, confidence=0.9)
        offset = (int(size[2] * offsetStrength), int(size[3] * offsetStrength))
        pyautogui.click(random.randint(imgPos.x - offset[0], imgPos.x + offset[0]),
                        random.randint(imgPos.y - offset[1], imgPos.y + offset[1]),
                        clicks=clickTimes, interval=0.2,duration=0.2, button="left")
    print("定位错误")
    time.sleep(0.5)


#遍历图片并定位----------------
flie = "1.png"
img=('111.jpg-222.jpg-333.jpg')
imgList=list(str(img).split('-'))
print(imgList)
def TotalLevelSeek(imgList):
    i=0
    while i<len(imgList):
        img = pyautogui.locateCenterOnScreen(imgList[i], confidence=0.9)
        if img is not True:
            return True
        i+=1
        return False
#-----------------------
#逻辑定位
def TotalLevelSeek(imgNumTotal):
    i=0
    Leve=0
    while i<imgNumTotal+1:
        imgPos=pyautogui.locateCenterOnScreen(imgList,confidence=0.9)
        if imgPos is not None:
            Leve=1
            print(f"当前游戏的进度,{i},{Leve}.")
            break
        i+=1
        if i==imgNumTotal:
            print(f"没有监测到游戏窗口,{i},{Leve}.")

def LocationLevelSeek(imgNumLocation):

    pass

def GameGoOn(Level):

    pass


