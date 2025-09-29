from config import *



def extract_frames(video_path: str, output_folder: str, interval: int):
    """
    Extracts frames from a video at a fixed interval and saves them to a specified directory.

    Args:
        video_path: Path to the input video file.
        output_folder: Path to the folder where frames will be saved.
        interval: How often to extract a frame (in seconds).

    Returns:
        None
    """
    # Your code starts here...

    # load video
    video = cv2.VideoCapture(video_path)

    # get fps and total # of frames
    fps = video.get(cv2.CAP_PROP_FPS)
    total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    
    # create folder to save the frames if not exist
    os.makedirs(output_folder, exist_ok=True)

    count, success = 0, True
    while success:
        success, image = video.read()   # read a frame
        if (count % (fps * interval) == 0):    # save the frame once every interval seconds
            cv2.imwrite(f"{output_folder}/frame{count}.jpg", image) 
        count += 1

    video.release()

    pass


def extract_audio(video_path: str, output_path: str):
    """
    Extracts the audio track from a video file and saves it as a WAV file.

    Args:
        video_path: Path to the input video file.
        output_path: Path where the extracted audio (WAV format) will be saved.

    Returns:
        None
    """
    # Your code starts here...

    # create directory to save the audio if not exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)


    (
        ffmpeg
        .input(video_path)
        .output(output_path, format='wav')
        .run()
    )

    pass


# ------------- DO NOT MODIFY BELOW -------------

video_dir = f"{DOWNLOAD_PATH}/{VIDEO_FILENAME}"
extract_frames(video_dir, FRAMES_DIR, INTERVAL)

audio_path = f"{AUDIO_DIR}/{AUDIO_FILENAME}"
extract_audio(video_dir, audio_path)