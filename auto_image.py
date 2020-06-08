#주석처리

import pyautogui


pyautogui.screenshot('ran.png', region=(400,300,30,30)) #특정위치 400,300 에 30,30,만큼 스크린샷을 찍는다.

i = pyautogui.locateCenterOnScreen('이미지.png') #이미지의 위치를 찾아서 return

pyautogui.click(i) #찾은 이미지를 클릭한다.

