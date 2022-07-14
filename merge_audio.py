
"""
import moviepy.editor as mpe

my_clip = mpe.VideoFileClip('vid1_compressed.mp4')
audio_background = mpe.AudioFileClip('my_result.mp3')
#final_audio = mpe.CompositeAudioClip([my_clip.audio, audio_background])
final_clip = my_clip.set_audio(audio_background)
"""

import moviepy.editor as mp

audio = mp.AudioFileClip("my_result.mp3")
video1 = mp.VideoFileClip("vid1_compressed.mp4")
final = video1.set_audio(audio)
final.write_videofile("output.mp4",codec= 'mpeg4' ,audio_codec='libvorbis')