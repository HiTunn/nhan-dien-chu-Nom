import numpy as np
import cv2
import time
import os


# Label: nothing là ko có gì
#label ="nothing"
label = "nhan"   #人
#label = "dai" #大
#label ="sinh" #生
#label = "mot" #𠬠

cap = cv2.VideoCapture(0)


# Biến đếm, để chỉ lưu dữ liệu sau khoảng 60 frame, tránh lúc đầu chưa kịp cầm hình
i=0
while(True):
    # Capture frame-by-frame
    #
    i+=1
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.resize(frame, dsize=None,fx=0.3,fy=0.3)

    # Hiển thị
    cv2.imshow('frame',frame)

    # Lưu dữ liệu
    if i>=60 and i<=1060:
        print("Số ảnh capture = ",i-60)
        # Tạo thư mục nếu chưa có
        if not os.path.exists('data/' + str(label)):
            os.mkdir('data/' + str(label))

        cv2.imwrite('data/' + str(label) + "/" + str(i) + ".png",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()