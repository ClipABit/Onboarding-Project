import shutil
import pytest
from config import *

from main import extract_frames, extract_audio

@pytest.fixture(scope="module")
def video_path():
    return os.path.join(DOWNLOAD_PATH, VIDEO_FILENAME)

@pytest.fixture(autouse=True)
def cleanup():
    TEST_ROOT = 'test'
    # Clean up test directory before testing
    if os.path.exists(TEST_ROOT):
        shutil.rmtree(TEST_ROOT)

    yield
    
    # Clean up after testing
    if os.path.exists(TEST_ROOT):
        shutil.rmtree(TEST_ROOT)


def test_extract_frames_1s(video_path):
    extract_frames(video_path, TEST_FRAMES_DIR, 1)
    assert os.path.exists(TEST_FRAMES_DIR)
    frames = [f for f in os.listdir(TEST_FRAMES_DIR) if f.endswith('.jpg') or f.endswith('.png')]
    assert len(frames) == 25, "Incorrect number of frames for 1s interval"

def test_extract_frames_5s(video_path):
    extract_frames(video_path, TEST_FRAMES_DIR, 5)
    assert os.path.exists(TEST_FRAMES_DIR)

    frames = [f for f in os.listdir(TEST_FRAMES_DIR) if f.endswith('.jpg') or f.endswith('.png')]
    assert len(frames) == 5, "Incorrect number of frames for 5s interval"

def test_extract_audio(video_path):
    output_path = os.path.join(TEST_AUDIO_DIR, AUDIO_FILENAME)
    extract_audio(video_path, output_path)
    
    assert os.path.exists(output_path), "Audio file not created"
    assert os.path.getsize(output_path) > 0, "Audio file is empty"
