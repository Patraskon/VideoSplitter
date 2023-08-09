# VideoSplitter
The main functionality of the script revolves around splitting a video file into multiple fragments. Here's an overview of the script's structure and key components:

    GUI Components:
        label_input: A label indicating the purpose of the corresponding input entry field.
        input_entry: An entry field for displaying the path of the input video file.
        browse_btn: A button that triggers a file dialog for selecting the input video file.
        save_label: A label indicating the purpose of the corresponding save entry field.
        save_entry: An entry field for displaying the path of the output directory for saving the video fragments.
        save_btn: A button that triggers a directory dialog for selecting the output directory.
        split_btn: A button that initiates the video splitting process.

    Helper Functions:
        get_input_video_file(): Opens a file dialog for selecting the input video file and updates the input_entry field with the selected file's path.
        get_save_directory(): Opens a directory dialog for selecting the output directory and updates the save_entry field with the selected directory's path.
        split_video(): Performs the actual video splitting process.

    Video Splitting Process:
        The split_video() function is triggered when the "Split" button is clicked.
        The function retrieves the paths entered in the input and save entry fields using input_path.get() and save_path.get().
        It checks if the input video file exists and raises a FileNotFoundError if not.
        It checks if the output directory exists and creates it if necessary.
        It uses FFprobe to determine the duration of the input video file.
        It calculates the fragment duration by dividing the total duration by 10.
        It uses FFmpeg to split the video into fragments, where each fragment has a duration equal to the calculated fragment duration. The fragments are saved in the specified output directory with filenames in the format "fragment_01.mp4", "fragment_02.mp4", and so on.
