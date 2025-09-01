# Onboarding Project
Welcome to the ClipABit team!

As part of your onboarding, we want to make sure you are familiar with the software development lifecycle and caught up on the basics of building software in a team. This includes working with Git, writing Python code, testing, and submitting a PR. By the end of this task, you should be refreshed/taught all foundational software skills you will need to be a contributing member to the team.

**TODO: Make a branch**

## Overview
The first step in our search engine's pipeline is processing videos. To do that we need to extract indivdual frames and audio transcriptions from our clips. You will be creating a slightly modified version of that. The goal is to open a video file, extract frames at a fixed interval, create an audio transcription of the entire clip and then save it to an output directory.

## Setup
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


**TODO: Make a PR**