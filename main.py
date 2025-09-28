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

    if not os.path.exists(video_path):
        print(f"Error: Video file not found at '{video_path}'")
        return

    os.makedirs(output_folder, exist_ok=True);

    cap = cv2.VideoCapture(video_path)

    frame_num = 0;

    if not cap.isOpened():
        print(f"Error: Failed to open video file at '{video_path}'. Check if the video path is correct and if the file format/codec is supported by OpenCV.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            break
        
        video_time_ms = cap.get(cv2.CAP_PROP_POS_MSEC);

        if (video_time_ms%(interval*1000) == 0):
            file_name = "peter_griffin_frame_number_" + str(frame_num) + ".png"
            FULL_FILE_PATH = os.path.join(output_folder, file_name)
            cv2.imwrite(FULL_FILE_PATH, frame)

        frame_num += 1

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
    # Your code starts here...
    ffmpeg.input(video_path).output(output_path).overwrite_output().run()


# ------------- DO NOT MODIFY BELOW -------------

video_dir = f"{DOWNLOAD_PATH}/{VIDEO_FILENAME}"
extract_frames(video_dir, FRAMES_DIR, INTERVAL)

audio_path = f"{AUDIO_DIR}/{AUDIO_FILENAME}"
extract_audio(video_dir, audio_path)
