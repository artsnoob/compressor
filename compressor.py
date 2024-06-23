import os
import subprocess
from dataclasses import dataclass
import moviepy.editor as mp

@dataclass
class Compressor:
    input_file: str
    output_file: str
    target_size: int  # target size in MB

    def compress(self):
        """
        Compresses the input file and saves it as the output file.
        Deletes the log file after compression.
        """
        # Get the duration of the video in seconds
        clip = mp.VideoFileClip(self.input_file)
        duration = clip.duration

        # Calculate the target bitrate in bits/s
        target_bitrate = self.target_size * 8 * 1024 * 1024 / duration

        command_1 = f"ffmpeg -y -i {self.input_file} -c:v libx264 -preset medium -b:v {target_bitrate} -pass 1 -an -f mp4 /dev/null"
        command_2 = f"ffmpeg -i {self.input_file} -c:v libx264 -preset medium -b:v {target_bitrate} -pass 2 -c:a aac -b:a 128k {self.output_file}"
        
        try:
            subprocess.run(command_1, shell=True, check=True)
            subprocess.run(command_2, shell=True, check=True)
            
            # Delete the log file
            log_file = "ffmpeg2pass-0.log.mbtree"
            if os.path.exists(log_file):
                os.remove(log_file)
                print(f"Deleted log file: {log_file}")
            else:
                print(f"Log file not found: {log_file}")
        except subprocess.CalledProcessError as e:
            print(f"Compression failed with error: {str(e)}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

def select_file():
    """
    Prompts the user to select the .mov file to be compressed.
    """
    file_path = input("Please enter the path to the .mov file to be compressed: ")
    if not os.path.isfile(file_path):
        raise ValueError("Invalid file path.")
    if not file_path.endswith(".mov"):
        raise ValueError("Invalid file format. Only .mov files are supported.")
    return file_path

def main():
    try:
        input_file = select_file()
        output_file = input_file.replace(".mov", "_compressed.mov")
        target_size = int(input("Please enter the target size in MB for the compressed file: "))
        compressor = Compressor(input_file, output_file, target_size)
        compressor.compress()
        print(f"Compression complete. Compressed file saved as {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
