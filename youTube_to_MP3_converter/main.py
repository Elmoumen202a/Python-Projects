import os
from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip

def download_video(url, output_path):
    """
    Downloads a YouTube video using the provided URL and saves it to the specified output path.

    Parameters:
    - url (str): The URL of the YouTube video.
    - output_path (str): The path where the downloaded video will be saved.

    Returns: None
    """
    # Create a YouTube object for the given URL
    yt = YouTube(url)

    # Get the highest resolution video stream in mp4 format
    video = yt.streams.filter(file_extension='mp4').first()

    # Download the video to the specified output path
    video.download(output_path)


def convert_to_mp3(input_path, output_path):
    """
    Converts a video file to MP3 format and saves the audio to the specified output path.

    Parameters:
    - input_path (str): The path to the input video file.
    - output_path (str): The path where the converted MP3 file will be saved.

    Returns: None
    """
    # Create a VideoFileClip object from the input video file
    video_clip = VideoFileClip(input_path)

    # Extract the audio from the video clip
    audio_clip = video_clip.audio

    # Write the audio to the specified output path in MP3 format
    audio_clip.write_audiofile(output_path)

    # Close the audio and video clips to release resources
    audio_clip.close()
    video_clip.close()

def main():
    # Set your YouTube video URL
    youtube_url = "https://www.youtube.com/watch?v=your_video_id"

    # Set the output paths
    video_output_path = "output/video.mp4"
    mp3_output_path = "output/audio.mp3"

    # Download YouTube video
    download_video(youtube_url, video_output_path)

    # Convert video to MP3
    convert_to_mp3(video_output_path, mp3_output_path)

    print("Conversion complete!")

if __name__ == "__main__":
    main()
