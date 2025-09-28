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
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created directory: {output_folder}")
    
    # OpenCV VideoCapture: Opens and reads video files
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return
    
    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps
    
    print(f"Video FPS: {fps}, Total frames: {total_frames}, Duration: {duration:.2f}s")
    
    # Calculate frame interval: interval (seconds) * fps = frames to skip
    frame_interval = int(interval * fps)
    
    frame_count = 0
    saved_count = 0
    
    while True:
        # Read the next frame
        ret, frame = cap.read()
        
        if not ret:  # No more frames
            break
            
        # Save frame if it's at the right interval
        if frame_count % frame_interval == 0:
            frame_filename = f"frame_{saved_count:04d}.jpg"
            frame_path = os.path.join(output_folder, frame_filename)
            
            # cv2.imwrite() saves the frame as an image file
            cv2.imwrite(frame_path, frame)
            saved_count += 1
            print(f"Saved frame {saved_count} at {frame_count/fps:.2f}s")
        
        frame_count += 1
    
    # Clean up resources
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
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
    
    try:
        # Use imageio-ffmpeg (bundled FFmpeg)
        import imageio_ffmpeg as ffmpeg_exe
        
        # Get the FFmpeg executable path from imageio-ffmpeg
        ffmpeg_path = ffmpeg_exe.get_ffmpeg_exe()
        print(f"Using bundled FFmpeg: {ffmpeg_path}")
        
        # Create FFmpeg stream pipeline
        input_stream = ffmpeg.input(video_path)
        audio_stream = input_stream.audio
        
        output_stream = ffmpeg.output(
            audio_stream, 
            output_path,
            acodec='pcm_s16le',  # Audio codec for WAV
            ar=44100,            # Sample rate 44.1kHz
            ac=2                 # Stereo channels
        )
        
        # Run with the bundled FFmpeg executable
        ffmpeg.run(output_stream, cmd=ffmpeg_path, overwrite_output=True, quiet=True)
        
        print(f"✅ Audio extracted successfully!")
        print(f"📁 Saved to: {output_path}")
        
        # Verify the file was created and has real content
        if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
            file_size = os.path.getsize(output_path) / (1024 * 1024)  # Convert to MB
            print(f"📊 Audio file size: {file_size:.2f} MB")
        else:
            raise Exception("Audio file not created or is too small")
            
    except ImportError:
        raise Exception("imageio-ffmpeg is required but not installed. Run: pip install imageio-ffmpeg")
    except Exception as e:
        print(f"❌ Audio extraction failed: {e}")
        raise e


# ------------- DO NOT MODIFY BELOW -------------

video_dir = f"{DOWNLOAD_PATH}/{VIDEO_FILENAME}"
extract_frames(video_dir, FRAMES_DIR, INTERVAL)

audio_path = f"{AUDIO_DIR}/{AUDIO_FILENAME}"
extract_audio(video_dir, audio_path)