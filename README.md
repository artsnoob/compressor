# Video Compressor

This Python script provides a simple command-line interface for compressing .mov video files to a specified target size using FFmpeg.

## Features

- Compress .mov video files to a target size in MB
- Utilizes FFmpeg for efficient two-pass compression
- Automatically calculates optimal bitrate based on video duration and target size
- Preserves audio quality with a constant 128k bitrate
- Cleans up temporary log files after compression

## Requirements

- Python 3.7+
- FFmpeg
- moviepy
- dataclasses (included in Python 3.7+)

## Installation

1. Ensure you have Python 3.7 or higher installed on your system.
2. Install FFmpeg:
   - On macOS: `brew install ffmpeg`
   - On Ubuntu: `sudo apt-get install ffmpeg`
   - For other systems, please refer to the [FFmpeg documentation](https://ffmpeg.org/download.html)
3. Install the required Python packages:
   ```
   pip install moviepy
   ```

## Usage

1. Clone this repository or download the script.
2. Run the script:
   ```
   python video_compressor.py
   ```
3. Follow the prompts:
   - Enter the path to the .mov file you want to compress
   - Specify the target size in MB for the compressed file
4. The script will compress the video and save it with a "_compressed" suffix in the same directory as the input file.

## How it works

1. The script prompts the user for the input file path and target size.
2. It calculates the optimal bitrate based on the video duration and target size.
3. FFmpeg is used to perform a two-pass compression:
   - First pass: Analyzes the video without audio
   - Second pass: Compresses the video with the calculated bitrate and adds audio
4. The compressed video is saved, and temporary log files are cleaned up.

## Error Handling

The script includes error handling for:
- Invalid file paths
- Unsupported file formats (only .mov is supported)
- FFmpeg process errors
- General exceptions
