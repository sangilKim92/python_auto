import os
import subprocess
import re
from pytube import YouTube
import pytube
import os

url = input('다운받을 주소를 입력하세요. 가장 좋은 화질과 소리나오는 가장 좋은 화질을 다운받습니다.')
print(url)
TITLE=YouTube(url)
print('haha')
try:
    print(TITLE.title)
except pytube.exceptions.RegexMatchError:
    print('gg')

yt=YouTube(url).streams.filter(file_extension='mp4').order_by('resolution').desc().first()
yt.download('C://Users/user/Untitled Folder/')
title=re.sub('[^a-zA-Z가-힣]','',yt.title)

os.rename(yt.default_filename, title+'nosound.mp4')
YouTube(url).streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download('C://Users/user/Untitled Folder/')

