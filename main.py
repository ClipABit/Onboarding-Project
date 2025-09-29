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
    # 1. Folder check
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video not found in the location: {video_path}")
    
    os.makedirs(output_folder, exist_ok=True)
    
    # 2. Open Video
    video = cv2.VideoCapture(video_path)
    
    # 3. Get Video properties 
    framespersecond = video.get(cv2.CAP_PROP_FPS)
    total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    # Frame per second = 25, Total frames = 618, Total seconds of the video = 24.72
    duration_sec = math.floor(total_frames / framespersecond)
    
    # 4. Extract frames at fixed given intervals
    idx = 0
    for t in range(0, duration_sec + 1, interval):
        video.set(cv2.CAP_PROP_POS_MSEC, t * 1000)
        ret, frame = video.read()
        if not ret or frame is None:
            continue
        out_path = os.path.join(output_folder, f"frame_{idx:05d}.jpg")
        cv2.imwrite(out_path, frame)
        idx += 1 
    
    video.release()
    
def extract_audio(video_path: str, output_path: str):
    """
    Extracts the audio track from a video file and saves it as a WAV file.

    Args:
        video_path: Path to the input video file.
        output_path: Path where the extracted audio (WAV format) will be saved.

    Returns:
        None
    """
    #1. Folder check
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video not found: {video_path}")
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    #2. Extract audio using FFMPEG library
    # It takes the input file path, Output path with some hyperparameters.
    # acodec - Encoding, ac - Audio channels, ar - Audio sample rate.
    (
        ffmpeg
        .input(video_path)
        .output(output_path, acodec='pcm_s16le', ac=2, ar='44100')
        .overwrite_output()
        .run(quiet=True)
    )


# ------------- DO NOT MODIFY BELOW -------------

video_dir = f"{DOWNLOAD_PATH}/{VIDEO_FILENAME}"
extract_frames(video_dir, FRAMES_DIR, INTERVAL)

audio_path = f"{AUDIO_DIR}/{AUDIO_FILENAME}"
extract_audio(video_dir, audio_path)