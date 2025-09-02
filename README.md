# Onboarding Project
Welcome to the ClipABit team!

As part of your onboarding, we want to make sure you are familiar with the software development lifecycle and caught up on the basics of building software in a team. This includes working with Git, writing Python code, testing, and submitting a PR. By the end of this task, you should be refreshed/taught all foundational software skills you will need to be a contributing member to the team.

**TODO: Instructions telling them to make a branch from git**

## Overview
The first step in our search engine's pipeline is processing videos. To do that we need to extract indivdual frames and audio transcriptions from our clips. You will be creating a slightly modified version of that. The goal is to open a video file, extract frames at a fixed interval, create an audio transcription of the entire clip and then save it to an output directory.

## Workspace Setup
Before beginning, please make a new branch from `main` for you to work on.
1. Clone the repository onto your local computer
2. Open a new terminal and create a new branch using  
    ```bash
    git checkout -b "FirstName_LastName_Onboarding"
    ```
    - Replace `FirstName` and `LastName` appropriately
3. As you work through this exercise, please make sure you push and commit your changes to save your work. Everything moving forward should be done in your branch.

## Environment Setup
Before you can do any video processing, you need to setup your environment and download the video to your project. 

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