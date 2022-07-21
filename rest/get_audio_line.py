import moviepy.editor as mp

my_clip = mp.VideoFileClip(r"vid1.mp4")
my_clip.audio.write_audiofile(r"my_result.mp3")