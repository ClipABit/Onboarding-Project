from config import *

# Create the directory if it doesn't exist
if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)
    print(f"Created directory: {DOWNLOAD_PATH}")

try:
    # Create a YouTube object
    yt = YouTube(VIDEO_URL)

    # Get the highest resolution progressive stream (video and audio combined)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    if stream:
        print(f"Downloading: {VIDEO_FILENAME}")
        stream.download(output_path=DOWNLOAD_PATH, filename=VIDEO_FILENAME)
        print(f"Download completed successfully. Saved to: {DOWNLOAD_PATH}")
    else:
        print("No progressive stream with mp4 format found.")

except Exception as e:
    print(f"An error occurred: {e}")