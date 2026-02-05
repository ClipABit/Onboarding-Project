# Onboarding Project
Welcome to the ClipABit team!

As part of your onboarding, we want to make sure you are familiar with the software development lifecycle and caught up on the basics of building software in a team. This includes working with Git, writing Python code, testing, and submitting a PR. By the end of this task, you should be refreshed/taught all foundational software skills you will need to be a contributing member to the team.

## Overview
The first step in our search engine's pipeline is processing videos. To do that we need to extract indivdual frames and audio transcriptions from our clips. You will be creating a slightly modified version of that. The goal is to open a video file, extract frames at a fixed interval, create an audio transcription of the entire clip and then save it to an output directory.

## Workspace Setup
The first thing you need to do is clone the repository. Ensure that you have Python and Git installed on your computer. On your computer, please run the following command:
```bash
git clone https://github.com/ClipABit/Onboarding-Project.git
```
Next, open the project, and before doing anything else, please make a new branch from `main` for you to work on.
1. Open a new terminal and create a new branch using  
    ```bash
    git checkout -b "FirstName_Onboarding"
    ```
    - Replace `FirstName` appropriately
2. As you work through this exercise, please make sure you push and commit your changes to save your work. Everything moving forward should be done in your branch.

## Environment Setup
Before you can do any video processing, you need to set up your environment and download the video to your project. 

1. Check your Python installation and version:
    #### MacOS/Linux
    ```bash
    python3 --version
    ```
    #### Windows
    ```bash
    python --version
    ```
    Make sure Python 3.7 or higher is installed.

2. (macOS only) If you encounter SSL certificate errors when running Python scripts, run:
    ```bash
    /Applications/Python\ 3.x/Install\ Certificates.command
    ```
    Replace `3.x` with your installed Python version (e.g., `3.12`).

3. Open a new terminal and make sure you are in the root directory of the project. ``~/Onboarding-Project``
4. Create and start a new virtual environment with the following commands.

    #### MacOS/Linux
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    #### Windows
    ```cmd
    python -m venv .venv
    .venv\Scripts\activate
    ```

    To deactivate the virtual environment when you are done, run:
    ```bash
    deactivate
    ```
5. After activation, install dependencies with:
    ```bash
    pip install -r requirements.txt
    ```
Note : Why just downloading the package won't work:

  ffmpeg-python is a Python wrapper library that builds FFmpeg commands in    
  Python. FFmpeg itself is written in C/C++ - the Python library just
  constructs commands and asks the FFmpeg installed on your machine to run    
  them.

  For example, this Python code:
  ffmpeg.input("video.mp4").output("audio.mp3", vn=True).run()

  Simply constructs and runs this shell command:
  ffmpeg -i video.mp4 -vn audio.mp3

  Flow:
  Python Code → ffmpeg-python library → System FFmpeg executable
                                                ↓
                                 ❌ NOT included in pip install
                                 ✅ Must install separately
                                 
  So you need to install ffmpeg on your system to run it as well , 
  Installation instructions:

  Windows:
  # Using chocolatey
  choco install ffmpeg

  # Or using winget
  winget install ffmpeg

  Mac:
  brew install ffmpeg

  Linux:
  sudo apt install ffmpeg

  Verify installation:
  ffmpeg -version

  If it prints version info, you're good to go.
6. Download the sample footage by running
    ```bash
    python download_video.py
    ```
    You should see a new directory ``/video`` appear with a file ``PeterGriffin.mp4``

7. You are now ready to begin! Open ``main.py`` and proceed

## Instructions
You will notice there are two functions left blank. Those are what you will be working on. Please refer to `config.py` to see all the available libraries to use.
1. The function `extract_frames()` should read a video from the directory `/video` and extract frames every `interval` seconds. These frames should then be saved as a `.jpg` in the output directory. Hint: you will need to use the `cv2` library. 
2. The function `extract_audio()` should transcribe the audio from the video and save it to the output directory. Hint: you will need to use the `ffmpeg` library.

## Guidelines
You are provided the skeleton code containing the necessary imports and the function signature, you only need to implement the body of the function. You may author the function as you like and should be able to do so used the provided outline. _You do not need to modify any code outside the function body._

This excersise is to get everyone on the same page high quality software. Your code should be robust, including error handling and comments where appropriate. You may use AI, but make sure you understand the code deeply and ensure it is of high quality. (Think: Would this code be suitable for a production environment?)

## Testing

Unit tests are provided in `test_main.py` using pytest.

To run the tests go the root directory of the project and run 
```bash
pytest test_main.py
```

If you see that all tests pass then you have successfully completed the project.

Note: if you get any incompatible architecture errors, run ```pip cache purge``` and try again.

## Submitting
Once you have finished, you will need to submit a *Pull Request* for us to review. On Github, open an new PR from your branch to `main`. Send us a message on discord attaching the link to the PR
