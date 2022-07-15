import cv2
import sys
import os
import moviepy.editor as mp


file = "vid2.mp4"
name = file.split(".")[0]
c = 50


t = str(file).split(".")
def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim)


cap = cv2.VideoCapture(str(file))
width  = (cap.get(3) * int(c))/ 100
height = (cap.get(4) * int(c))/ 100

compressed_file = str(t[0]+'_compressed.mp4')
out_video = cv2.VideoWriter(compressed_file,0x7634706d, 20.0, (int(width), int(height)),True)
while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            frameX = rescale_frame(frame,int(c))
            out_video.write(frameX) 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
cap.release()
cv2.destroyAllWindows()





my_clip = mp.VideoFileClip(file)
audio_clip = f"{name}_audio.mp3"
my_clip.audio.write_audiofile(audio_clip)

