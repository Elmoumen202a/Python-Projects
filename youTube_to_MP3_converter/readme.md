# YouTube to MP3 Converter

A simple Python script to convert YouTube videos to MP3.

## Usage

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the script using `python main.py`.

## Requirements

- Python 3.12.2
- See `requirements.txt` for Python package dependencies.

## Explanation

### Modules

- **os Module:**
  - The `os` module provides a way of interacting with the operating system, allowing you to perform operations such as path manipulation and file management.

- **pytube Module:**
  - The `pytube` module is used for downloading YouTube videos. It simplifies the process of interacting with YouTube's API to fetch video data and streams.

- **moviepy Module:**
  - The `moviepy` module provides functionalities for video editing and manipulation. In this project, it is used to extract audio from a video file and save it as an MP3 file.

### Functions

- **download_video Function:**
  - Downloads a YouTube video using the provided URL and saves it to the specified output path.

- **convert_to_mp3 Function:**
  - Converts a video file to MP3 format and saves the audio to the specified output path.

- **main Function:**
  - The main function to orchestrate the YouTube video download and conversion to MP3.

  Parameters:
  - None

  Returns:
  - None

## Example

To run the project:

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Update the `youtube_url` variable in `main.py` with the desired YouTube video URL.
4. Run the script: `python main.py`

Please note that this example uses the `pytube` and `moviepy` libraries. You may need to handle potential exceptions and edge cases based on your specific requirements.
