import os
import subprocess

def split_movie(file_path, output_folder, segment_time):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    command = [
        "ffmpeg", "-i", file_path, "-c", "copy", "-map", "0",
        "-segment_time", str(segment_time), "-f", "segment",
        os.path.join(output_folder, "episode%03d.mp4")
    ]
    subprocess.run(command)
