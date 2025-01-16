# My Python Project

This project is designed to retrieve metadata from movie files and split them into segments. It utilizes `ffprobe` for metadata extraction and `ffmpeg` for video processing.

## Project Structure

```
my-python-project
├── src
│   ├── main.py          # Entry point of the application
│   ├── utils
│   │   ├──  # Marks the utils directory as a package
│   │   ├movie_split.py   # Contains function to get movie metadata
│   │   └──      # Contains function to split movies into segments
├── requirements.txt      # Lists project dependencies
└── README.md             # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-python-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure that `ffmpeg` and `ffprobe` are installed on your system and accessible from the command line.

## Usage

To run the application, execute the following command:
```
python src/main.py <path_to_movie_file> <output_folder> <segment_time>
```

Replace `<path_to_movie_file>`, `<output_folder>`, and `<segment_time>` with the appropriate values.

## License

