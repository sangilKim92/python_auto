import pyautogui
import time

print('node_js, node_web, python_auto, restApi, gitHub, BlockchainGame')
gitRepo=input('주소위치를 입력하시오')
pyautogui.moveTo(356,1056)

pyautogui.click()

time.sleep(1)

pyautogui.typewrite('git bash')
time.sleep(1)
pyautogui.typewrite(['enter'])

time.sleep(3)

pyautogui.typewrite('cd ')
pyautogui.typewrite(gitRepo)
pyautogui.typewrite(['enter'])

time.sleep(1)
pyautogui.typewrite('git add .')
pyautogui.typewrite(['enter'])

time.sleep(4)
pyautogui.moveTo(502,404)
pyautogui.click()

pyautogui.typewrite('git commit -m "push to github using auto_python"')
pyautogui.typewrite(['enter'])
time.sleep(4)


pyautogui.typewrite('git push -u origin master')
pyautogui.typewrite(['enter'])

time.sleep(4)
pyautogui.typewrite('sangilKim92')
pyautogui.typewrite(['enter'])

time.sleep(3)
pyautogui.typewrite('VLsbfX39pWjHxW')
pyautogui.typewrite(['enter'])






