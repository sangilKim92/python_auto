import cv2

cap = cv2.VideoCapture('./merry.mp4')


frame_cnt = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('총 Frame 갯수:', frame_cnt)
time =0
while True:
    time=time+1
    hasFrame, img_frame = cap.read()
    if not hasFrame:
        print('더 이상 처리할 frame이 없습니다.')
        break
    if(time==1400):
        break
    cv2.imwrite(str(time)+'.jpg',img_frame)
# end of while loop
#1138번 사진
