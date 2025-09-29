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
    #Checks for No output folder case --> creates folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
   
    #Opens video file
    vid = cv2.VideoCapture(video_path)
    
    #Checks if video file is opened --> prints error message
    if not vid.isOpened():
        print(f"Error: {video_path} cannot be opened.")
    
    
    #Save FPS of video
    fps = vid.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * interval) #Frame interval calculated from FPS and time interval
    frameCount = 0
    currentCount = 0
    
    #Loops through the video frames -- writes the frames per interval -- until it reachs the end of the video
    while True:
        ret, frame = vid.read()
        if not ret:
            break #if there are no more frames, it will exit the while loop
            
        if frameCount % frame_interval == 0:
            filename = os.path.join(output_folder, f"frame_{currentCount:04d}.jpg")
            cv2.imwrite(filename, frame)
            currentCount += 1
    
        frameCount += 1
    
    #Releases the video file
    vid.release()

    #confirmation message
    print(f"Extracted  '{currentCount}' frames to '{output_folder}'.")

def extract_audio(video_path: str, output_path: str):
    """
    Extracts the audio track from a video file and saves it as a WAV file.

    Args:
        video_path: Path to the input video file.
        output_path: Path where the extracted audio (WAV format) will be saved.

    Returns:
        None
    """

    #Makes sure the output directory exists before proceeding with audio extraction 
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    try:
        #Defines an input video file
        stream = ffmpeg.input(video_path)

        #Directing the stream to the output path in the form of WAV file
        stream = ffmpeg.output(stream, output_path, acodec='pcm_s16le')

        #Executes ffmpeg commadn to extract audio
        ffmpeg.run(stream, overwrite_output=True)
        print(f"Extracted audio to '{output_path}'.")
    
    #Catches ffmpeg errors and prints the stderr output for debugging
    except ffmpeg.Error as e:
        print("ffmpeg error occurred.")
        if hasattr(e, 'stderr') and e.stderr:
            try:
                print(e.stderr.decode())
            except Exception:
                print(e.stderr)
        else:
            print("No stderr output available.")
        raise
    
# ------------- DO NOT MODIFY BELOW -------------

video_dir = f"{DOWNLOAD_PATH}/{VIDEO_FILENAME}"
extract_frames(video_dir, FRAMES_DIR, INTERVAL)

audio_path = f"{AUDIO_DIR}/{AUDIO_FILENAME}"
extract_audio(video_dir, audio_path)