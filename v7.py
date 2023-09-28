import tkinter as tk
from tkinter import filedialog
import os
import pathlib
import subprocess

root = tk.Tk()
root.geometry("500x400")
root.title("Video Splitter")

label_input = tk.Label(root, text="Input video file:")
label_input.place(x=20, y=20)

input_path = tk.StringVar()
input_entry = tk.Entry(root, width=50, textvariable=input_path)
input_entry.place(x=150, y=20)

browse_btn = tk.Button(root, text="Browse", command=lambda: get_input_video_file())
browse_btn.place(x=450, y=20)

save_label = tk.Label(root, text="Output directory:")
save_label.place(x=20, y=80)

save_path = tk.StringVar()
save_entry = tk.Entry(root, width=50, textvariable=save_path)
save_entry.place(x=150, y=80)

save_btn = tk.Button(root, text="Browse", command=lambda: get_save_directory())
save_btn.place(x=450, y=80)

split_btn = tk.Button(root, text="Split", command=lambda: split_video())
split_btn.place(x=350, y=140)

def get_input_video_file():
    filename = filedialog.askopenfilename(title="Select input video file", filetypes=[('Video Files', '*.mp4 *.ts')])
    input_path.set(filename)

def get_save_directory():
    save_directory = filedialog.askdirectory(title="Select output directory")
    save_entry.delete(0, tk.END)
    save_entry.insert(0, save_directory)

def split_video():
    global input_path, save_path
    input_path = pathlib.Path(input_path.get())
    save_path = pathlib.Path(save_path.get())

    # Check if the input video file exists
    if not input_path.is_file():
        raise FileNotFoundError("Input video file does not exist")

    # Check if the output directory exists
    if not save_path.is_dir():
        save_path.mkdir(parents=True)

    # Convert TS files to MP4 if necessary
    if input_path.suffix.lower() == '.ts':
        temp_mp4_path = save_path / 'temp.mp4'
        convert_to_mp4(input_path, temp_mp4_path)
        input_path = temp_mp4_path

    # Calculate the fragment duration for exactly 10 files
    fragment_duration = get_video_duration(input_path) / 12

    # Split the video into fragments
    command = f'ffmpeg -i "{input_path}" -f segment -segment_time {fragment_duration} -c copy "{save_path}/fragment_%02d.mp4"'
    subprocess.call(command, shell=True)

def get_video_duration(video_path):
    ffprobe_command = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{video_path}"'
    duration_str = subprocess.check_output(ffprobe_command, shell=True).decode().strip()
    return float(duration_str)

def convert_to_mp4(input_file, output_file):
    command = f'ffmpeg -i "{input_file}" -c:v copy -c:a copy -bsf:a aac_adtstoasc "{output_file}"'
    subprocess.call(command, shell=True)

root.mainloop()