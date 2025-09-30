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
    os.makedirs(output_folder, exist_ok=True)
    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Cannot open video file: {video_path}")
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    f_interval = int(fps * interval)  # calculate frames to skip based on time interval
    
    f_count = saved_count = 0
    
    try:
        # check if frames exist without loading pixel data
        while cap.read()[0]:
            if f_count % f_interval == 0:
                # seek to specific frame position to avoid loading unwanted frames
                cap.set(cv2.CAP_PROP_POS_FRAMES, f_count)
                ret, frame = cap.read()
                if ret:
                    # 04d ensures consistent filename sorting (frame_0001.jpg, frame_0002.jpg, etc.)
                    cv2.imwrite(f"{output_folder}/frame_{saved_count:04d}.jpg", frame)
                    saved_count += 1
            f_count += 1
    finally:
        # clean up video capture 
        cap.release()


def extract_audio(video_path: str, output_path: str):
    """
    Extracts the audio track from a video file and saves it as a WAV file.

    Args:
        video_path: Path to the input video file.
        output_path: Path where the extracted audio (WAV format) will be saved.

    Returns:
        None
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    try:
        # use uncompressed PCM for lossless audio extraction: 
        #   pcm_s16le: 16-bit signed little-endian (standard for WAV)
        #   ar='44100': 44.1kHz sample rate (CD quality)
        #   ac=2: stereo output (2 channels)
        ffmpeg.input(video_path).output(
            output_path, acodec='pcm_s16le', ar='44100', ac=2  
        ).overwrite_output().run(quiet=True)
    except ffmpeg.Error as e:
        raise RuntimeError(f"Audio extraction failed: {e}")

# ------------- DO NOT MODIFY BELOW -------------

video_dir = f"{DOWNLOAD_PATH}/{VIDEO_FILENAME}"
extract_frames(video_dir, FRAMES_DIR, INTERVAL)

audio_path = f"{AUDIO_DIR}/{AUDIO_FILENAME}"
extract_audio(video_dir, audio_path)