import cv2

vid = cv2.VideoCapture("AnthonyShkraba.mp4")

if (vid.isOpened()== False):
    print("Unable to read the feed.")

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)

height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)

FPS = int(vid.get(cv2.CAP_PROP_FPS))
print(FPS)

out = cv2.VideoWriter("Boxing.mp4",cv2.VideoWriter_fourcc(*"DIVX"),30,(width,height))

while (True):
    ret, frame = vid.read()
    cv2.imshow("Web cam",frame)
    out.write(frame)
    if cv2.waitKey(25) == 32:
        break 
    vid.release()
    out.release()
    cv2.destroyAllWindows()