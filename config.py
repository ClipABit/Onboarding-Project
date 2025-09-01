import os
import cv2
import math
import ffmpeg
from pytubefix import YouTube

VIDEO_URL = 'https://www.youtube.com/watch?v=mOQXmDvg5AI'
DOWNLOAD_PATH = 'video'  # directory to save video to
FRAMES_DIR = 'output/frames'  # directory to save frames to
AUDIO_DIR = 'output/audio'  # directory to save audio to
VIDEO_FILENAME = "PeterGriffin.mp4"  # name of the video file
AUDIO_FILENAME = "audio.wav"  # name of the audio file

# Feel free to tweek this number to test robustness.
INTERVAL = 1  # number of seconds between each frame extraction