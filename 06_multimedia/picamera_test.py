import picamera
import time

path = '/home/pi/src6/06_multimedia'
camera = picamera.PiCamera()


try:
    while True :
        a = int(input("photo : 1, video : 2, exit : 9 > "))
        if(a == 1) : 
            camera.resolution = (640,480)
            camera.start_preview()
            time.sleep(2)
            camera.rotation = 180
            now_str = time.strftime("%Y%m%d_%H%M%S")
            camera.capture('{}/{}.jpg'.format(path, now_str))
            print("사진 촬영")
        elif(a == 2):
            now_str = time.strftime("%Y%m%d_%H%M%S")
            camera.start_recording('{}/{}..h264'.format(path, now_str))
            time.sleep(3)
            camera.stop_recording
            print("동영상 촬영")
        elif(a == 9) :
            break
        else :
            print("incorrect commend")
    
finally:
    camera.stop_preview()
# import picamera
# import time

# path = '/home/pi/src/06_multimedia'

# camera = picamera.PiCamera()

# try:
#     camera.resolution = (640, 480)
#     camera.start_preview()
#     time.sleep(3)
#     camera.rotation = 180
#     camera.start_recording('%s/video.h264' % path)
#     time.sleep(10)
#     camera.stop_recording()

# finally:
#     camera.stop_preview()

#동영상 촬영
# import picamera
# import time

# path = '/home/pi/src6/06_multimedia'
# camera = picamera.PiCamera()


# try:
#     camera.resolution = (640,480)
#     camera.start_preview()
#     time.sleep(3)
#     camera.rotation = 180
#     #camera.capture('%s/photo.jpg' % path)
#     camera.start_recording('%s/video.h264' % path)
#     input('press enter to stop')
#     camera.stop_recording()

# finally:
#     camera.stop_preview()

# 사진찍기
# import picamera
# import time

# path = '/home/pi/src6/06_multimedia'
# camera = picamera.PiCamera()


# try:
#     camera.resolution = (640,480)
#     camera.start_preview()
#     time.sleep(3)
#     camera.rotation = 180
#     camera.capture('%s/photo.jpg' % path)

# finally:
#     camera.stop_preview()

