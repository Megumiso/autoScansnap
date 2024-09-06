import pyautogui
import time

print('スクリプトを開始します')

while True:
    # 1.pngが見つかるまでループ
    loc1 = None

    while True:
        try:
            loc1 = pyautogui.locateOnScreen('1.png', confidence=0.9)
        except:
            pass
        if loc1 is not None:
            break
        #見つからなかったら5s待機
        time.sleep(5)

    # 1.pngが見つかったらクリック
    pyautogui.click(loc1)
    print('1.pngをクリックしました')

    # 2.pngが見つかるまでループ
    loc2 = None

    while True:
        try:
            loc2 = pyautogui.locateOnScreen('2.png', confidence=0.9)
        except:
            pass
        if loc2 is not None:
            break
        #見つからなかったら5s待機
        time.sleep(5)

    # 2.pngが見つかったらクリック
    pyautogui.click(loc2)
    print('2.pngをクリックしました')

    # 3.pngが見つかるまでループ
    loc3 = None

    while True:
        try:
            loc3 = pyautogui.locateOnScreen('3.png', confidence=0.9)
        except:
            pass
        if loc3 is not None:
            break
        #見つからなかったら5s待機
        time.sleep(5)

    # 3.pngが見つかったらクリック
    pyautogui.click(loc3)
