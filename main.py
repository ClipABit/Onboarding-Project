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
    # Create output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return
    
    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps
    
    print(f"Video duration: {duration:.2f} seconds")
    print(f"FPS: {fps}")
    print(f"Extracting frames every {interval} seconds...")
    
    frame_count = 0
    saved_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Calculate current time in seconds
        current_time = frame_count / fps
        
        # Check if we should extract this frame
        if int(current_time) % interval == 0 and current_time >= 0:
            # Save frame as JPEG
            frame_filename = f"frame_{int(current_time):04d}s.jpg"
            frame_path = os.path.join(output_folder, frame_filename)
            cv2.imwrite(frame_path, frame)
            saved_count += 1
            print(f"Saved frame at {current_time:.2f}s: {frame_filename}")
        
        frame_count += 1
    
    # Release the video capture object
    cap.release()
    print(f"Extraction complete! Saved {saved_count} frames to {output_folder}")


def extract_audio(video_path: str, output_path: str):
    """
    Extracts the audio track from a video file and saves it as a WAV file.

    Args:
        video_path: Path to the input video file.
        output_path: Path where the extracted audio (WAV format) will be saved.

    Returns:
        None
    """
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        print(f"Extracting audio from {video_path}...")
        
        # Use ffmpeg to extract audio from video
        (
            ffmpeg
            .input(video_path)
            .output(output_path, acodec='pcm_s16le', ac=1, ar='16k')  # 16kHz mono WAV
            .overwrite_output()  # Overwrite if file exists
            .run(quiet=True)  # Suppress ffmpeg output
        )
        
        print(f"Audio extraction complete! Saved to {output_path}")
        
    except ffmpeg.Error as e:
        print(f"Error extracting audio: {e}")
        if e.stderr:
            print(f"FFmpeg stderr: {e.stderr.decode()}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# ------------- DO NOT MODIFY BELOW -------------

video_dir = f"{DOWNLOAD_PATH}/{VIDEO_FILENAME}"
extract_frames(video_dir, FRAMES_DIR, INTERVAL)

audio_path = f"{AUDIO_DIR}/{AUDIO_FILENAME}"
extract_audio(video_dir, audio_path)