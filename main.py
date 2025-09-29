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
    # make output_folder directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # open the video file using VideoCapture class
    capture = cv2.VideoCapture(video_path)
    if not capture.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return
    
    # get framerate of the video
    fps = capture.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * interval)    # frames between captures
    frame_count = 0     # total frames processed
    saved_count = 0     # total frames saved

    while True:
        # get next video frame
        retval, image = capture.read()
        if not retval:  
            break   # end of video

        if frame_count % frame_interval == 0:
            frame_filename = f"{output_folder}/frame_{saved_count}.jpg"     # filename based on saved_count
            saved_count += 1    # update saved frames
            cv2.imwrite(frame_filename, image)    # saves image to file
        frame_count += 1    # update total frames processed
    
    # Close the video file
    capture.release()
    print(f"Finished extracting {saved_count} frames into {output_folder}")

def extract_audio(video_path: str, output_path: str):
    """
    Extracts the audio track from a video file and saves it as a WAV file.

    Args:
        video_path: Path to the input video file.
        output_path: Path where the extracted audio (WAV format) will be saved.

    Returns:
        None
    """
    # Create directory for output_path if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    try:
        # Use ffmpeg to extract audio and save as WAV
        (
            ffmpeg
            .input(video_path)
            .output(output_path, format='wav')
            .run()
        )
        print(f"Audio extracted and saved to {output_path}")
    except ffmpeg.Error as e:
        print(f"An error occurred while extracting audio: {e.stderr.decode()}")

# ------------- DO NOT MODIFY BELOW -------------

video_dir = f"{DOWNLOAD_PATH}/{VIDEO_FILENAME}"
extract_frames(video_dir, FRAMES_DIR, INTERVAL)

audio_path = f"{AUDIO_DIR}/{AUDIO_FILENAME}"
extract_audio(video_dir, audio_path)